# -*- coding: utf-8 -*-
"""多用户支持：用户注册表 + 每用户独立数据库。

设计（2026-09-12）：
  - 用户注册表 data/users.json：{users:[{id,name,created}], current:"<id>"}
  - 每用户一个完整 SQLite 库：data/users/<id>.db
    （知识点掌握度、答题记录、错题本、SRS 卡片全部隔离；
      题库/图谱靠 seed 灌入，讲解内容 content_*.py 本来就全局共享）
  - 隔离粒度选"分库"而非"表加 user_id 列"：现有全部 SQL 零改动，
    单人本地场景下最简单可靠；备份=拷一个文件。
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import date

from config import DATA_DIR

USERS_DIR = os.path.join(DATA_DIR, "users")
REGISTRY = os.path.join(DATA_DIR, "users.json")
os.makedirs(USERS_DIR, exist_ok=True)


# ---------------------------------------------------------------- registry
def _load() -> dict:
    try:
        with open(REGISTRY, encoding="utf-8") as f:
            reg = json.load(f)
        if isinstance(reg.get("users"), list):
            return reg
    except (OSError, ValueError):
        pass
    return {"users": [], "current": None}


def _save(reg: dict) -> None:
    tmp = REGISTRY + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)
    os.replace(tmp, REGISTRY)


def _uid(name: str) -> str:
    """用户 id：名字哈希短码，避免中文名进文件名带来的编码/路径问题。"""
    return "u" + hashlib.md5(name.encode("utf-8")).hexdigest()[:8]


# ---------------------------------------------------------------- CRUD
def list_users() -> list[dict]:
    return _load()["users"]


def add_user(name: str) -> dict:
    name = name.strip()
    if not name:
        raise ValueError("名字不能为空")
    if not re.fullmatch(r"[\w\u4e00-\u9fff·\s-]{1,20}", name):
        raise ValueError("名字只能是 1—20 个中文/字母/数字")
    reg = _load()
    if any(u["name"] == name for u in reg["users"]):
        raise ValueError("已存在同名用户：%s" % name)
    u = {"id": _uid(name), "name": name, "created": date.today().isoformat()}
    reg["users"].append(u)
    reg["current"] = u["id"]
    _save(reg)
    return u


def remove_user(uid: str) -> None:
    reg = _load()
    reg["users"] = [u for u in reg["users"] if u["id"] != uid]
    if reg["current"] == uid:
        reg["current"] = reg["users"][0]["id"] if reg["users"] else None
    _save(reg)
    p = db_path(uid)
    try:
        if os.path.exists(p):
            os.rename(p, p + ".deleted")   # 不物理删，留一手
    except OSError:
        pass   # 服务占用中：注册表已移除，文件留待下次清理


def get_current() -> dict | None:
    reg = _load()
    cid = reg.get("current")
    return next((u for u in reg["users"] if u["id"] == cid), None)


def set_current(uid: str) -> None:
    reg = _load()
    if not any(u["id"] == uid for u in reg["users"]):
        raise ValueError("用户不存在：%s" % uid)
    reg["current"] = uid
    _save(reg)


def find_by_name(name: str) -> dict | None:
    return next((u for u in list_users() if u["name"] == name.strip()), None)


# ---------------------------------------------------------------- paths
def db_path(uid: str) -> str:
    return os.path.join(USERS_DIR, "%s.db" % uid)


def ensure_user(name: str) -> dict:
    """取已有用户或创建新用户（幂等，手机端登录页用）。"""
    u = find_by_name(name)
    return u or add_user(name)
