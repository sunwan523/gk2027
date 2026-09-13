# -*- coding: utf-8 -*-
"""知识点讲解内容加载器。

各科详解存放在 core/content_<科目>.py（CONTENT = {kp_id: [要点, ...]}），
由内容生成流程产出。本模块聚合成统一查询入口，容错：
某科目文件缺失/损坏时跳过，不影响其余科目与整体运行。

设计为"从文件路径加载"而非 import_module，规避中文模块名的导入机制差异。
"""
from __future__ import annotations

import importlib.util
import os
from typing import Any

from config import BASE_DIR, SUBJECTS

_CORE = os.path.join(BASE_DIR, "core")
_MERGED: dict[str, list[str]] | None = None
_LOADED_FROM: dict[str, str] = {}


def _load_subject(subject: str) -> dict[str, list[str]]:
    path = os.path.join(_CORE, "content_%s.py" % subject)
    if not os.path.exists(path):
        return {}
    try:
        spec = importlib.util.spec_from_file_location("content_%s" % subject, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
        data = getattr(mod, "CONTENT", {}) or {}
        _LOADED_FROM[subject] = path
        return {str(k): [str(x) for x in v] for k, v in data.items()}
    except Exception as e:  # 语法错误等——跳过该科，不拖垮整体
        import warnings
        warnings.warn("内容文件 %s 加载失败：%s" % (path, e))
        return {}


def _all() -> dict[str, list[str]]:
    global _MERGED
    if _MERGED is None:
        _MERGED = {}
        for s in SUBJECTS:
            _MERGED.update(_load_subject(s))
    return _MERGED


def reload_content() -> None:
    global _MERGED
    _MERGED = None
    _LOADED_FROM.clear()
    _all()


def get_content(kp_id: str) -> list[str]:
    """某知识点的学习要点列表；无内容返回 []。"""
    return _all().get(kp_id, [])


def has_content(kp_id: str) -> bool:
    return bool(_all().get(kp_id))


def coverage() -> dict[str, Any]:
    """内容覆盖统计：各科目已写知识点数 / 该科总节点数。

    滚动任务（词汇/默写）无固定章节，不计入分母。
    """
    from core import db
    ROLLING = ("eng_vocab", "chn_dictation")
    conn = db.connect()
    total = {s: conn.execute(
        "SELECT COUNT(*) FROM knowledge_points WHERE subject=? AND id NOT IN (%s)"
        % ",".join("?" * len(ROLLING)), (s,) + ROLLING).fetchone()[0]
        for s in SUBJECTS}
    got = {s: 0 for s in SUBJECTS}
    ids = _all().keys()
    for kp in ids:
        r = conn.execute(
            "SELECT subject FROM knowledge_points WHERE id=?", (kp,)).fetchone()
        if r and r["subject"] in got:
            got[r["subject"]] += 1
    conn.close()
    return {"by_subject": {s: (got[s], total[s]) for s in SUBJECTS},
            "loaded_files": dict(_LOADED_FROM)}
