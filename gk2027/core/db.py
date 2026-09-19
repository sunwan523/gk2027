# -*- coding: utf-8 -*-
"""SQLite 数据层。

对应重构方案 5.3 节。两条硬约束用于杜绝旧项目的两个致命缺陷：

1. ``UNIQUE(stem)`` —— 旧项目 3003 条生物"真题"里只有 11 道不重复。
   有此约束，第 12 条重复题干插入即失败，"批量注水"在技术上不可能。
2. 触发器校验 ``source_type`` 与 ``year``/``paper`` 的绑定 ——
   AI 生成题永远不能带年份卷别，旧项目让模型编的题顶着"2009 年天津卷"
   的名义出现，这是最严重的错误，必须在数据结构层面禁止。
"""
from __future__ import annotations

import json
import os
import sqlite3
from datetime import date, datetime
from typing import Any, Iterable, Sequence

from config import DB_PATH, SOURCE_TYPES, SOURCES_ALLOWING_YEAR, ATTRIBUTIONS

SCHEMA = """
PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------- 知识点
CREATE TABLE IF NOT EXISTS knowledge_points (
    id          TEXT PRIMARY KEY,
    subject     TEXT NOT NULL,
    tier        TEXT NOT NULL CHECK(tier IN ('初中','高中必修','高中选择性')),
    name        TEXT NOT NULL,
    weight      TEXT NOT NULL DEFAULT '常规'
                CHECK(weight IN ('高频考点','常规','低频')),
    est_hours   REAL NOT NULL DEFAULT 2.0,
    status      TEXT NOT NULL DEFAULT '未解锁'
                CHECK(status IN ('未解锁','可学','学习中','已掌握','需复习')),
    mastery     REAL NOT NULL DEFAULT 0.0 CHECK(mastery >= 0 AND mastery <= 1),
    diagnosis   TEXT DEFAULT NULL
                CHECK(diagnosis IS NULL OR diagnosis IN ('记得','忘了','从没学过')),
    notes       TEXT DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_kp_subject ON knowledge_points(subject, tier);

-- 依赖边。跨学科依赖是这张图最重要的部分（方案 5.4）。
CREATE TABLE IF NOT EXISTS kp_requires (
    kp_id       TEXT NOT NULL REFERENCES knowledge_points(id) ON DELETE CASCADE,
    requires_id TEXT NOT NULL REFERENCES knowledge_points(id) ON DELETE CASCADE,
    PRIMARY KEY (kp_id, requires_id),
    CHECK (kp_id <> requires_id)
);

-- ---------------------------------------------------------------- 题目
CREATE TABLE IF NOT EXISTS questions (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    source_type  TEXT NOT NULL CHECK(source_type IN ({sources})),
    year         INTEGER,
    paper        TEXT,
    question_no  TEXT,
    source_ref   TEXT,
    verified     INTEGER NOT NULL DEFAULT 0 CHECK(verified IN (0,1)),
    subject      TEXT NOT NULL,
    kp_id        TEXT REFERENCES knowledge_points(id) ON DELETE SET NULL,
    difficulty   INTEGER NOT NULL DEFAULT 3 CHECK(difficulty BETWEEN 1 AND 5),
    qtype        TEXT NOT NULL DEFAULT '选择题'
                 CHECK(qtype IN ('选择题','填空题','解答题','实验题','作文','默写')),
    stem         TEXT NOT NULL UNIQUE,
    options      TEXT DEFAULT '[]',
    answer       TEXT NOT NULL,
    analysis     TEXT DEFAULT '',
    image_path   TEXT,
    created_at   TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);
CREATE INDEX IF NOT EXISTS idx_q_kp ON questions(kp_id);
CREATE INDEX IF NOT EXISTS idx_q_subject ON questions(subject, difficulty);

-- ---------------------------------------------------------------- 训练包
CREATE TABLE IF NOT EXISTS packs (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    kind         TEXT NOT NULL CHECK(kind IN
                 ('A','B','C','D','E','F','CALC','READ','TIME')),
    subject      TEXT,
    title        TEXT NOT NULL,
    created_at   TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    path         TEXT,
    printed      INTEGER NOT NULL DEFAULT 0 CHECK(printed IN (0,1)),
    finished     INTEGER NOT NULL DEFAULT 0 CHECK(finished IN (0,1))
);

-- ---------------------------------------------------------------- 作答记录
CREATE TABLE IF NOT EXISTS attempts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id  INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    pack_id      INTEGER REFERENCES packs(id) ON DELETE SET NULL,
    done_at      TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    correct      INTEGER NOT NULL CHECK(correct IN (0,1)),
    seconds      INTEGER,
    attribution  TEXT CHECK(attribution IS NULL OR attribution IN ({attrs})),
    note         TEXT DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_att_q ON attempts(question_id, done_at);

-- ---------------------------------------------------------------- 错题本
CREATE TABLE IF NOT EXISTS wrong_questions (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id   INTEGER NOT NULL UNIQUE REFERENCES questions(id) ON DELETE CASCADE,
    attribution   TEXT NOT NULL CHECK(attribution IN ({attrs})),
    first_wrong   TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    last_wrong    TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    wrong_count   INTEGER NOT NULL DEFAULT 1,
    streak        INTEGER NOT NULL DEFAULT 0,
    resolved      INTEGER NOT NULL DEFAULT 0 CHECK(resolved IN (0,1)),
    resolved_at   TEXT
);

-- ---------------------------------------------------------------- 间隔重复卡片
CREATE TABLE IF NOT EXISTS cards (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    kind          TEXT NOT NULL CHECK(kind IN ('错题','知识卡','默写','词汇','公式','概念')),
    subject       TEXT NOT NULL,
    kp_id         TEXT REFERENCES knowledge_points(id) ON DELETE SET NULL,
    question_id   INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    front         TEXT NOT NULL,
    back          TEXT NOT NULL DEFAULT '',
    image_path    TEXT,
    due_at        TEXT NOT NULL,
    interval_days REAL NOT NULL DEFAULT 1.0,
    ease          REAL NOT NULL DEFAULT 2.5,
    reps          INTEGER NOT NULL DEFAULT 0,
    lapses        INTEGER NOT NULL DEFAULT 0,
    streak        INTEGER NOT NULL DEFAULT 0,
    retired       INTEGER NOT NULL DEFAULT 0 CHECK(retired IN (0,1)),
    UNIQUE(kind, front)
);
CREATE INDEX IF NOT EXISTS idx_card_due ON cards(due_at, retired);

CREATE TABLE IF NOT EXISTS pack_items (
    pack_id     INTEGER NOT NULL REFERENCES packs(id) ON DELETE CASCADE,
    question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    seq         INTEGER NOT NULL,
    PRIMARY KEY (pack_id, question_id)
);
CREATE TABLE IF NOT EXISTS pack_cards (
    pack_id INTEGER NOT NULL REFERENCES packs(id) ON DELETE CASCADE,
    card_id INTEGER NOT NULL REFERENCES cards(id) ON DELETE CASCADE,
    seq     INTEGER NOT NULL,
    PRIMARY KEY (pack_id, card_id)
);

-- ---------------------------------------------------------------- 模考与实测
CREATE TABLE IF NOT EXISTS exam_records (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    taken_at     TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    kind         TEXT NOT NULL CHECK(kind IN ('诊断','章节测试','单科实测','全真模考')),
    subject      TEXT,
    score        REAL,
    full_mark    REAL NOT NULL,
    duration_min INTEGER,
    raw_score    REAL,
    detail       TEXT DEFAULT ''
);

-- ---------------------------------------------------------------- 学习时长
CREATE TABLE IF NOT EXISTS activity_log (
    day       TEXT NOT NULL,
    hour      INTEGER NOT NULL DEFAULT 0,
    page      TEXT NOT NULL,
    subject   TEXT NOT NULL DEFAULT '',
    kp_id     TEXT NOT NULL DEFAULT '',
    seconds   INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (day, hour, page, subject, kp_id)
);

-- ---------------------------------------------------------------- 设置
CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- ---------------------------------------------------------------- 触发器
-- AI 生成 / 教辅录入 / 自主命题练习 一律不得带年份与卷别。
CREATE TRIGGER IF NOT EXISTS trg_no_fake_provenance_insert
BEFORE INSERT ON questions
FOR EACH ROW WHEN NEW.source_type NOT IN ({with_year})
             AND (NEW.year IS NOT NULL OR NEW.paper IS NOT NULL)
BEGIN
    SELECT RAISE(ABORT,
      '禁止：非真题来源不得填写 year/paper。这是旧项目最严重的错误，让编造的题顶着真实年份卷别出现。如需标注出处请用 source_ref。');
END;

CREATE TRIGGER IF NOT EXISTS trg_no_fake_provenance_update
BEFORE UPDATE OF source_type, year, paper ON questions
FOR EACH ROW WHEN NEW.source_type NOT IN ({with_year})
             AND (NEW.year IS NOT NULL OR NEW.paper IS NOT NULL)
BEGIN
    SELECT RAISE(ABORT,
      '禁止：非真题来源不得填写 year/paper。');
END;

-- 真题必须给出可核查出处，否则无法溯源。
CREATE TRIGGER IF NOT EXISTS trg_real_exam_needs_ref_insert
BEFORE INSERT ON questions
FOR EACH ROW WHEN NEW.source_type = '真题'
             AND (NEW.source_ref IS NULL OR TRIM(NEW.source_ref) = '')
BEGIN
    SELECT RAISE(ABORT, '真题必须填写 source_ref（出处链接或书名页码），否则不得入库。');
END;
"""


def connect(path: str | None = None) -> sqlite3.Connection:
    target = path or DB_PATH
    os.makedirs(os.path.dirname(target), exist_ok=True)
    # check_same_thread=False：Streamlit 在不同线程执行脚本，
    # 缓存连接跨线程使用；单人本地应用，无并发写风险。
    conn = sqlite3.connect(target, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    if path is None:
        # 主库：任何部署点首次使用都必须有 schema（新环境主库没有其他建表入口）
        conn.executescript(_render_schema())
        conn.commit()
    return conn


def _render_schema() -> str:
    src = ", ".join("'%s'" % s for s in SOURCE_TYPES)
    wy = ", ".join("'%s'" % s for s in SOURCES_ALLOWING_YEAR)
    at = ", ".join("'%s'" % a for a in ATTRIBUTIONS)
    return SCHEMA.format(sources=src, with_year=wy, attrs=at)


def init_db(path: str | None = None, *, seed: bool = False) -> sqlite3.Connection:
    """建表并返回连接。seed=True 时首次自动灌入知识图谱与自检题库
    （多用户模式下每个新库都需要种子数据）。"""
    conn = connect(path)
    conn.executescript(_render_schema())
    conn.commit()
    from core import diary
    diary.create_tables(conn)   # 📖 空间：签到/随手记/体重/用户设置/隐秘空间
    if seed:
        from core import graph, seed_quiz
        graph.seed_graph(conn)
        seed_quiz.seed_self_quiz(conn)
        conn.commit()
    return conn


# ----------------------------------------------------------------------
# 设置读写
# ----------------------------------------------------------------------
def get_setting(conn: sqlite3.Connection, key: str, default: Any = None) -> Any:
    row = conn.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
    if row is None:
        return default
    try:
        return json.loads(row["value"])
    except (ValueError, TypeError):
        return row["value"]


def set_setting(conn: sqlite3.Connection, key: str, value: Any) -> None:
    conn.execute(
        "INSERT INTO settings(key, value) VALUES(?,?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (key, json.dumps(value, ensure_ascii=False)),
    )
    conn.commit()


# ----------------------------------------------------------------------
# 题目
# ----------------------------------------------------------------------
class DuplicateStem(Exception):
    """题干重复。旧项目 3003 条生物题只有 11 道不重复，此异常用于拦截注水。"""


def add_question(conn: sqlite3.Connection, **kw: Any) -> int:
    cols = [
        "source_type", "year", "paper", "question_no", "source_ref", "verified",
        "subject", "kp_id", "difficulty", "qtype", "stem", "options",
        "answer", "analysis", "image_path",
    ]
    stem = (kw.get("stem") or "").strip()
    if not stem:
        raise ValueError("stem 不能为空")
    kw["stem"] = stem
    if isinstance(kw.get("options"), (list, tuple)):
        kw["options"] = json.dumps(list(kw["options"]), ensure_ascii=False)
    kw.setdefault("options", "[]")
    kw.setdefault("verified", 0)
    kw.setdefault("difficulty", 3)
    kw.setdefault("qtype", "选择题")

    existing = conn.execute("SELECT id FROM questions WHERE stem=?", (stem,)).fetchone()
    if existing:
        raise DuplicateStem("题干已存在（id=%d），拒绝重复录入。" % existing["id"])

    fields = [c for c in cols if c in kw]
    sql = "INSERT INTO questions(%s) VALUES(%s)" % (
        ",".join(fields), ",".join("?" * len(fields)))
    cur = conn.execute(sql, [kw[c] for c in fields])
    conn.commit()
    return int(cur.lastrowid)


def add_questions(conn: sqlite3.Connection, rows: Iterable[dict]) -> dict[str, int]:
    """批量录入，返回统计。重复题干跳过而不中断，便于教辅批量导入。"""
    ok = dup = err = 0
    for r in rows:
        try:
            add_question(conn, **r)
            ok += 1
        except DuplicateStem:
            dup += 1
        except sqlite3.IntegrityError:
            dup += 1
        except Exception:
            err += 1
    return {"inserted": ok, "duplicate": dup, "error": err}


def list_questions(
    conn: sqlite3.Connection,
    subject: str | None = None,
    kp_id: str | None = None,
    source_type: str | None = None,
    difficulty: tuple[int, int] | None = None,
    limit: int | None = None,
) -> list[sqlite3.Row]:
    sql = "SELECT * FROM questions WHERE 1=1"
    args: list[Any] = []
    if subject:
        sql += " AND subject=?"; args.append(subject)
    if kp_id:
        sql += " AND kp_id=?"; args.append(kp_id)
    if source_type:
        sql += " AND source_type=?"; args.append(source_type)
    if difficulty:
        sql += " AND difficulty BETWEEN ? AND ?"; args += list(difficulty)
    sql += " ORDER BY subject, kp_id, difficulty"
    if limit:
        sql += " LIMIT %d" % int(limit)
    return conn.execute(sql, args).fetchall()


def decode_options(row: sqlite3.Row) -> list[str]:
    try:
        val = json.loads(row["options"] or "[]")
        return val if isinstance(val, list) else []
    except (ValueError, TypeError):
        return []


# ----------------------------------------------------------------------
# 作答与错题
# ----------------------------------------------------------------------
def record_attempt(
    conn: sqlite3.Connection,
    question_id: int,
    correct: bool,
    attribution: str | None = None,
    seconds: int | None = None,
    pack_id: int | None = None,
    note: str = "",
) -> None:
    """记录一次作答；答错自动进错题本，答对累加连续正确次数。"""
    if attribution and attribution not in ATTRIBUTIONS:
        raise ValueError("归因必须是六类之一：%s" % "/".join(ATTRIBUTIONS))
    conn.execute(
        "INSERT INTO attempts(question_id, pack_id, correct, seconds, attribution, note)"
        " VALUES(?,?,?,?,?,?)",
        (question_id, pack_id, 1 if correct else 0, seconds, attribution, note),
    )
    row = conn.execute(
        "SELECT id, streak, wrong_count FROM wrong_questions WHERE question_id=?",
        (question_id,)).fetchone()
    if correct:
        if row:
            new_streak = row["streak"] + 1
            # 连续 3 次做对才出库（方案 5.2 D 类包规则）
            if new_streak >= 3:
                conn.execute(
                    "UPDATE wrong_questions SET streak=?, resolved=1, "
                    "resolved_at=datetime('now','localtime') WHERE id=?",
                    (new_streak, row["id"]))
            else:
                conn.execute(
                    "UPDATE wrong_questions SET streak=? WHERE id=?",
                    (new_streak, row["id"]))
    else:
        if not attribution:
            raise ValueError(
                "错题必须选择归因类型，不能跳过（方案 4.3）。"
                "六类：%s" % "/".join(ATTRIBUTIONS))
        if row:
            conn.execute(
                "UPDATE wrong_questions SET attribution=?, streak=0, wrong_count=wrong_count+1,"
                " last_wrong=datetime('now','localtime'), resolved=0, resolved_at=NULL WHERE id=?",
                (attribution, row["id"]))
        else:
            conn.execute(
                "INSERT INTO wrong_questions(question_id, attribution) VALUES(?,?)",
                (question_id, attribution))
    conn.commit()


def attribution_distribution(conn: sqlite3.Connection, subject: str | None = None) -> list[sqlite3.Row]:
    """归因分布——决定下一步练什么（方案 5.5）。"""
    sql = ("SELECT w.attribution AS attribution, COUNT(*) AS n "
           "FROM wrong_questions w JOIN questions q ON q.id=w.question_id "
           "WHERE w.resolved=0")
    args: list[Any] = []
    if subject:
        sql += " AND q.subject=?"
        args.append(subject)
    sql += " GROUP BY w.attribution ORDER BY n DESC"
    return conn.execute(sql, args).fetchall()


def open_wrongs(conn: sqlite3.Connection, subject: str | None = None) -> list[sqlite3.Row]:
    sql = ("SELECT w.*, q.stem, q.answer, q.analysis, q.subject, q.kp_id, q.qtype "
           "FROM wrong_questions w JOIN questions q ON q.id=w.question_id "
           "WHERE w.resolved=0")
    args: list[Any] = []
    if subject:
        sql += " AND q.subject=?"; args.append(subject)
    sql += " ORDER BY w.wrong_count DESC, w.last_wrong DESC"
    return conn.execute(sql, args).fetchall()


# ----------------------------------------------------------------------
# 统计
# ----------------------------------------------------------------------
def stats(conn: sqlite3.Connection) -> dict[str, Any]:
    def one(sql: str) -> int:
        r = conn.execute(sql).fetchone()
        return int(r[0]) if r and r[0] is not None else 0

    return {
        "知识点总数": one("SELECT COUNT(*) FROM knowledge_points"),
        "已掌握知识点": one("SELECT COUNT(*) FROM knowledge_points WHERE status='已掌握'"),
        "题目总数": one("SELECT COUNT(*) FROM questions"),
        "真题数": one("SELECT COUNT(*) FROM questions WHERE source_type='真题'"),
        "未解决错题": one("SELECT COUNT(*) FROM wrong_questions WHERE resolved=0"),
        "待复习卡片": one("SELECT COUNT(*) FROM cards WHERE retired=0"),
        "作答次数": one("SELECT COUNT(*) FROM attempts"),
        "训练包数": one("SELECT COUNT(*) FROM packs"),
    }


def question_stats_by_subject(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    out = []
    for r in conn.execute(
            "SELECT subject, COUNT(*) AS n, "
            "SUM(CASE WHEN source_type='真题' THEN 1 ELSE 0 END) AS real_n, "
            "SUM(CASE WHEN source_type='AI生成' THEN 1 ELSE 0 END) AS ai_n "
            "FROM questions GROUP BY subject ORDER BY subject"):
        out.append(dict(r))
    return out


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------------------------------------
# 学习时长统计
# ----------------------------------------------------------------------
MAX_ACTIVITY_SECONDS = 300   # 单条时长上限5分钟，防挂机虚增


def add_activity(conn: sqlite3.Connection, day: str, page: str,
                 subject: str = "", kp_id: str = "", seconds: int = 1,
                 hour: int = 0) -> None:
    """累计一次学习时长（按 天×小时×页面×科目×知识点 聚合，可重复调用累加）。

    page 取值：学习 / 练习 / 背诵 / 复习 / 进度 / 导出 / 统计 / 浏览
    seconds 单条上限 5 分钟，避免页面挂着不动虚增时长。
    """
    seconds = max(0, min(int(seconds), MAX_ACTIVITY_SECONDS))
    if seconds <= 0:
        return
    conn.execute(
        "INSERT INTO activity_log(day, hour, page, subject, kp_id, seconds)"
        " VALUES(?,?,?,?,?,?)"
        " ON CONFLICT(day, hour, page, subject, kp_id)"
        " DO UPDATE SET seconds = seconds + excluded.seconds",
        (day, hour % 24, page, subject or "", kp_id or "", seconds),
    )
    conn.commit()


def activity_totals(conn: sqlite3.Connection, since: str | None = None,
                    page: str | None = None) -> list[sqlite3.Row]:
    """聚合时长。since 为 YYYY-MM-DD 起始日期（含）；page 过滤页面类型。"""
    sql = "SELECT day, page, subject, kp_id, seconds FROM activity_log WHERE 1=1"
    args: list[Any] = []
    if since:
        sql += " AND day >= ?"; args.append(since)
    if page:
        sql += " AND page = ?"; args.append(page)
    sql += " ORDER BY day, page, subject, kp_id"
    return conn.execute(sql, args).fetchall()
