# -*- coding: utf-8 -*-
"""AI出题模块：调用 DeepSeek API 根据知识点内容自动生成测试题。"""
from __future__ import annotations

import json
import re
import urllib.request
import urllib.error

API_KEY = "sk-b975b7c022ca4815b3c8d75c1d89c3c7"
API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-chat"

SYSTEM_PROMPT = """你是一位高中辅导老师。根据用户提供的知识点内容，生成基础巩固测试题。

要求：
1. 生成5道题，题型混合：3道选择题（ABCD四个选项）+ 2道填空题
2. 题目要基础、直接，考的就是知识点本身，不要出难题、偏题、综合题
3. 选择题考概念辨析和基本公式套用，4个选项中1个正确，错误选项要是常见易错点
4. 填空题考核心概念、公式、定义的直接记忆
5. 每道题都要有解析说明，解析要讲清楚为什么对
6. 难度：学完这个知识点就能做对，相当于课后作业基础题

输出格式（严格JSON，不要有其他文字）：
{
  "questions": [
    {
      "type": "choice",
      "stem": "题目题干",
      "options": ["A选项", "B选项", "C选项", "D选项"],
      "answer": "A",
      "analysis": "解析说明"
    },
    {
      "type": "fill",
      "stem": "填空题题干（空处用____表示）",
      "answer": "答案",
      "analysis": "解析说明"
    }
  ]
}"""


def _chat(payload: dict) -> dict:
    """通用 DeepSeek 对话请求，返回完整响应体。"""
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
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"DeepSeek API错误 {e.code}: {err_body[:200]}")
    except Exception as e:
        raise RuntimeError(f"API调用失败: {e}")


def generate_quiz(subject: str, kp_name: str, points: list[str], count: int = 5) -> list[dict]:
    """根据知识点要点生成AI题目。

    Args:
        subject: 科目（语文/数学/英语/物理/化学/生物）
        kp_name: 知识点名称
        points: 知识点要点列表
        count: 题目数量

    Returns:
        题目列表，每项含 type/stem/options/answer/analysis
    """
    # 拼接知识点内容（限制长度，避免token超限）
    content = "\n".join("- " + p for p in points[:30])  # 最多取30条要点
    if len(content) > 6000:
        content = content[:6000] + "..."

    user_prompt = f"""科目：{subject}
知识点：{kp_name}
知识点内容：
{content}

请生成{count}道基础巩固测试题（课后作业难度），严格按JSON格式输出。"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 2000,
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
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"DeepSeek API错误 {e.code}: {err_body[:200]}")
    except Exception as e:
        raise RuntimeError(f"API调用失败: {e}")

    content_text = result["choices"][0]["message"]["content"]

    # 提取JSON（模型可能输出多余文字）
    json_match = re.search(r'\{[\s\S]*\}', content_text)
    if not json_match:
        raise RuntimeError("AI返回格式异常，未找到JSON")

    data = json.loads(json_match.group())
    questions = data.get("questions", [])

    # 标准化题目格式
    normalized = []
    for i, q in enumerate(questions[:count]):
        qtype = q.get("type", "choice")
        item = {
            "qid": f"ai_{kp_name}_{i}",
            "qtype": "选择题" if qtype == "choice" else "填空题",
            "stem": q.get("stem", ""),
            "options": q.get("options", []),
            "answer": q.get("answer", ""),
            "analysis": q.get("analysis", ""),
            "source": "AI生成",
        }
        normalized.append(item)

    return normalized
