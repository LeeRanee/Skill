#!/usr/bin/env python3
"""Add first-turn guidance to explicitly invoked image-prompt-director requests."""

import json
import sys


CONTEXT = """<image-prompt-director-codex-hook-active>
本提示仅适用于 image-prompt-director 的图片创作或编辑请求。若用户尚未看到并明确确认本次具体方案，本轮先按 skill 展示文字方案并等待选择及明确确认，不调用任何生图或图片编辑工具。若用户已在之前看到并明确确认当前具体方案，按该 skill 的确认规则继续；对修改或讨论 skill 的元任务不启动创作流程。本提示不替代其他适用指令。
</image-prompt-director-codex-hook-active>"""


def main():
    try:
        data = json.load(sys.stdin)
        prompt = data.get("prompt") if isinstance(data, dict) else None
        if not isinstance(prompt, str) or "image-prompt-director" not in prompt.lower():
            return
        result = {"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": CONTEXT}}
        sys.stdout.write(json.dumps(result, ensure_ascii=True) + "\n")
    except (ValueError, OSError):
        # Invalid input must neither print user text nor block the user's turn.
        return


if __name__ == "__main__":
    main()
