# -*- coding: utf-8 -*-
"""AI 通俗讲解：学习卡片遇到不懂的，让 DeepSeek 换个方式讲懂它。

用法：explain_point(subject, kp_name, text) -> str（大白话讲解，可朗读）
"""
import json
import urllib.error
import urllib.request

API_KEY = "sk-b975b7c022ca4815b3c8d75c1d89c3c7"
API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-chat"

SYSTEM_PROMPT = """你是经验丰富的高中教师，最擅长把难懂的知识点用大白话讲明白。
要求：
1. 用生活化类比、具体例子帮助理解，讲清楚"是什么、为什么、怎么用"；
2. 分点讲，语言口语化、亲切，像老师当面答疑；
3. 控制在 400 字以内；
4. 直接输出讲解内容，不要标题、不要客套话、不要"以下是"之类开场白。"""


def explain_point(subject: str, kp_name: str, text: str) -> str:
    """把一句没看懂的卡片内容讲明白。text 不超过 800 字。"""
    user = f"科目：{subject}\n知识点：{kp_name}\n\n下面这句我没看懂，请讲明白：\n{text[:800]}"

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ],
        "temperature": 0.7,
        "max_tokens": 1200,
    }

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"DeepSeek API错误 {e.code}: {err_body[:200]}")
    except Exception as e:
        raise RuntimeError(f"API调用失败: {e}")

    return (result["choices"][0]["message"]["content"] or "").strip()
