#!/usr/bin/env python3
"""Inspect or register the skill's Codex user-level UserPromptSubmit hook.

Output is one JSON object; registration never asserts that Codex trusts or runs it.
"""

import argparse
import json
import os
from pathlib import Path
import shlex
import stat
import sys
import tempfile


HOOK = Path(__file__).resolve().with_name("codex_prompt_hook.py")
HOOK_NAME = HOOK.name


class InvalidConfig(Exception):
    pass


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InvalidConfig("duplicate JSON key")
        result[key] = value
    return result


def load_config(path):
    if path.is_symlink():
        raise InvalidConfig("hooks.json is a symbolic link")
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        return {}, None
    try:
        data = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=no_duplicate_keys)
    except (UnicodeError, ValueError) as exc:
        raise InvalidConfig("hooks.json is not valid UTF-8 JSON") from exc
    if not isinstance(data, dict) or not isinstance(data.get("hooks", {}), dict):
        raise InvalidConfig("hooks.json must contain a hooks object")
    groups = data.get("hooks", {}).get("UserPromptSubmit", [])
    if not isinstance(groups, list):
        raise InvalidConfig("UserPromptSubmit must be an array")
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("hooks"), list):
            raise InvalidConfig("invalid UserPromptSubmit group")
        if any(not isinstance(handler, dict) for handler in group["hooks"]):
            raise InvalidConfig("invalid UserPromptSubmit handler")
        if any("commandWindows" in handler and "command_windows" in handler for handler in group["hooks"]):
            raise InvalidConfig("duplicate Windows command aliases")
    return data, raw


def command():
    executable = str(Path(sys.executable).resolve())
    script = str(HOOK)
    if os.name == "nt":
        # Codex normally invokes the user's PowerShell on Windows. Single quotes
        # are literal in PowerShell; double apostrophes escape apostrophes.
        quote = lambda s: "'" + s.replace("'", "''") + "'"
        return "& " + quote(executable) + " " + quote(script)
    return shlex.join([executable, script])


def handler_command(handler):
    if os.name == "nt":
        return handler.get("commandWindows", handler.get("command_windows", handler.get("command", "")))
    return handler.get("command", "")


def registration(data, expected):
    for group in data.get("hooks", {}).get("UserPromptSubmit", []):
        for handler in group["hooks"]:
            cmd = handler_command(handler)
            if handler.get("type") == "command" and cmd == expected:
                return "registered"
            if isinstance(cmd, str) and HOOK_NAME in cmd:
                # Never silently rewrite an old installation or create duplicates.
                return "stale_registration"
    return "missing"


def emit(status, home, detail=None):
    result = {"status": status, "config_path": str(home / "hooks.json"), "trust": "unknown", "active": "unknown"}
    if detail:
        result["detail"] = detail
    print(json.dumps(result, ensure_ascii=True))


def run(action, home, old_command=None):
    config_path = home / "hooks.json"
    if not HOOK.is_file():
        return "unknown", "hook script is missing"
    if action == "status":
        data, _ = load_config(config_path)
        return registration(data, command()), None

    # Atomic directory creation serializes concurrent runs of this installer.
    home.mkdir(parents=True, exist_ok=True)
    lock = home / ".image-prompt-director-hook.lock"
    try:
        lock.mkdir()
    except FileExistsError:
        return "unknown", "installer lock exists; retry after the other installer finishes"
    temp_path = None
    try:
        data, original = load_config(config_path)
        state = registration(data, command())
        if action == "install":
            if state != "missing":
                return state, None
            data.setdefault("hooks", {}).setdefault("UserPromptSubmit", []).append({
                "hooks": [{"type": "command", "command": command(), "timeout": 10}]
            })
        else:
            target = old_command or command()
            if HOOK_NAME not in target:
                return "unknown", "the exact command must identify this hook script"
            groups = data.get("hooks", {}).get("UserPromptSubmit", [])
            matches = []
            for group in groups:
                for handler in group["hooks"]:
                    cmd = handler_command(handler)
                    if handler.get("type") == "command" and cmd == target:
                        matches.append((group, handler))
            if not matches:
                return "missing", None
            if len(matches) != 1:
                return "unknown", "multiple exact matches; inspect hooks.json manually"
            group, handler = matches[0]
            group["hooks"].remove(handler)
            # Preserve other groups' indices: trust is associated with a hook's
            # position. The last empty group may be removed without shifting one.
            if not group["hooks"] and set(group) == {"hooks"} and group is groups[-1]:
                groups.remove(group)
        payload = (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        fd, name = tempfile.mkstemp(prefix=".image-prompt-director-", suffix=".tmp", dir=home)
        temp_path = Path(name)
        with os.fdopen(fd, "wb") as out:
            out.write(payload)
            out.flush()
            os.fsync(out.fileno())
        if original is not None:
            os.chmod(temp_path, stat.S_IMODE(config_path.stat().st_mode))
        # Detect edits by other writers before replacement. Independent writers
        # that do not honor this lock can still race between this check and replace.
        _, current = load_config(config_path)
        if current != original:
            return "unknown", "hooks.json changed concurrently; no replacement attempted"
        os.replace(temp_path, config_path)
        temp_path = None
        return ("installed" if action == "install" else "uninstalled"), None
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
        lock.rmdir()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("status", "install", "uninstall"))
    parser.add_argument("--codex-home", help="explicit Codex home (default: CODEX_HOME or ~/.codex)")
    parser.add_argument("--command", help="exact reviewed old command for uninstall after a path change")
    args = parser.parse_args()
    if args.command and args.action != "uninstall":
        parser.error("--command is only supported by uninstall")
    home = Path(args.codex_home or os.environ.get("CODEX_HOME") or Path.home() / ".codex").expanduser().resolve()
    try:
        status, detail = run(args.action, home, args.command)
    except InvalidConfig as exc:
        status, detail = "invalid_config", str(exc)
    except PermissionError:
        status, detail = "permission_denied", "cannot access or write the Codex configuration"
    except OSError as exc:
        status, detail = "unknown", f"filesystem error: {exc.strerror or type(exc).__name__}"
    emit(status, home, detail)
    return 0 if status in ("registered", "missing", "installed", "uninstalled") else 1


if __name__ == "__main__":
    sys.exit(main())
