#!/usr/bin/env python3
"""Add first-turn guidance to explicit requests and supported preset intents."""

import json
import sys


CONTEXT = """<image-prompt-director-codex-hook-active>
本提示仅适用于 image-prompt-director 的图片创作或编辑请求。完整提示词须用可复制代码块连同方案设置先发送到用户可见的聊天正文，全部正文发送结束后，才能串行调用依赖该方案的选择或确认控件并等待回答；内部思考、工具参数、卡片摘要或“方案已展示”不算交付，不先弹卡再补方案。前置背景、写法澄清仍可先问；平台无法在调用控件前发送完整可见正文时，在完整正文末尾用文字提问并等待回答，不额外要求回复“继续”。若用户尚未看到并明确确认本次具体方案，不调用任何生图或图片编辑工具；漏展示或修改方案后先补齐完整正文再重新确认。若用户已在之前看到并明确确认当前具体方案，按该 skill 的确认规则继续。异步控件返回不等于用户已回答。对修改或讨论 skill 的元任务不启动创作流程。本提示不替代其他适用指令。
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
BEAD_TERMS = ("拼豆",)
SIMPLIFICATION_TERMS = (
    "简化", "精简", "减少细节", "降低细节", "大色块", "前置图", "前置插画",
    "适合拼豆", "适合做拼豆", "便于拼豆", "方便做拼豆",
)


def should_add_context(prompt):
    """Recognize explicit invocation and the two supported preset intents."""
    lowered = prompt.lower()
    if "image-prompt-director" in lowered:
        return True
    food_image = any(term in prompt for term in FOOD_TERMS) and any(
        term in prompt for term in IMAGE_TERMS
    )
    bead_simplification = any(term in prompt for term in BEAD_TERMS) and any(
        term in prompt for term in SIMPLIFICATION_TERMS
    )
    return food_image or bead_simplification


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
