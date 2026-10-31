#!/usr/bin/env python3
"""Add first-turn guidance to explicit requests and braised-food product images."""

import json
import sys


CONTEXT = """<image-prompt-director-codex-hook-active>
本提示仅适用于 image-prompt-director 的图片创作或编辑请求。若用户尚未看到并明确确认本次具体方案，本轮先按 skill 展示文字方案并等待选择及明确确认，不调用任何生图或图片编辑工具。若用户已在之前看到并明确确认当前具体方案，按该 skill 的确认规则继续；对修改或讨论 skill 的元任务不启动创作流程。本提示不替代其他适用指令。
</image-prompt-director-codex-hook-active>"""

FOOD_TERMS = (
    "卤味", "卤菜", "卤食", "卤熟食", "熟食", "卤肉", "鸭胗", "鸭肫",
    "鸭肠", "鸭脖", "鸭翅", "鸭爪", "鸭头", "鸡爪", "鸡翅", "猪蹄",
)
IMAGE_TERMS = (
    "商品图", "产品图", "主图", "规格图", "商品照", "产品照", "电商图",
    "商品摄影", "产品摄影", "食品摄影", "产品拍摄", "商品拍摄", "美食摄影", "图片", "照片", "图像", "配图",
    "生图", "出图", "做图", "画图", "制图", "摄影图", "拍图", "渲染图", "图生图", "生成图", "制作图",
)


def should_add_context(prompt):
    """Recognize explicit invocation or a food item with product-image intent."""
    lowered = prompt.lower()
    if "image-prompt-director" in lowered:
        return True
    return any(term in prompt for term in FOOD_TERMS) and any(
        term in prompt for term in IMAGE_TERMS
    )


def main():
    try:
        data = json.load(sys.stdin)
        prompt = data.get("prompt") if isinstance(data, dict) else None
        if not isinstance(prompt, str) or not should_add_context(prompt):
            return
        result = {"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": CONTEXT}}
        sys.stdout.write(json.dumps(result, ensure_ascii=True) + "\n")
    except (ValueError, OSError):
        # Invalid input must neither print user text nor block the user's turn.
        return


if __name__ == "__main__":
    main()
