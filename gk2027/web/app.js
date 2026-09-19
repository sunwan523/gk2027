/* 高考复习 · 单页前端逻辑（原生 JS，无框架） */
"use strict";

// ---------- 工具 ----------
const $ = (s) => document.querySelector(s);
const $$ = (s) => Array.from(document.querySelectorAll(s));
function esc(s) {
  return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
function toast(msg) {
  const t = $("#toast");
  t.textContent = msg; t.classList.remove("hidden");
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.add("hidden"), 1600);
}
async function api(path, opts) {
  const r = await fetch(path, Object.assign({
    headers: { "Content-Type": "application/json" },
  }, opts));
  if (!r.ok) {
    let msg = "请求失败";
    try { msg = (await r.json()).error || msg; } catch (e) {}
    throw new Error(msg);
  }
  return r.json();
}
const post = (path, body) => api(path, { method: "POST", body: JSON.stringify(body || {}) });

// ---------- 朗读（Web Speech API，中文） ----------
let tts = { voices: [], voice: null, rate: 1, pitch: 1, playing: false, utter: null, queue: [], idx: 0, onDone: null };
function ttsLoadVoices() {
  tts.voices = (window.speechSynthesis.getVoices() || []).filter(v => v.lang && v.lang.toLowerCase().indexOf("zh") >= 0);
  const saved = localStorage.getItem("tts_voice");
  tts.voice = tts.voices.find(v => v.name === saved) || tts.voices[0] || null;
  tts.rate = parseFloat(localStorage.getItem("tts_rate") || "1");
  tts.pitch = parseFloat(localStorage.getItem("tts_pitch") || "1");
  const sel = $("#ttsVoice");
  if (sel) {
    sel.innerHTML = "";
    if (!tts.voices.length) { sel.innerHTML = '<option value="">无中文语音</option>'; return; }
    tts.voices.forEach((v, i) => {
      const o = document.createElement("option");
      o.value = i; o.text = v.name + (v.default ? " (默认)" : "");
      sel.appendChild(o);
      if (tts.voice && v.name === tts.voice.name) sel.value = i;
    });
  }
}
if (window.speechSynthesis && speechSynthesis.onvoiceschanged !== undefined) {
  speechSynthesis.onvoiceschanged = ttsLoadVoices;
}

function ttsSpeak(texts, onDone) {
  tts.queue = texts; tts.idx = 0; tts.onDone = onDone || null;
  if (!texts.length) return;
  window.speechSynthesis.cancel();
  ttsSay(0);
}
function ttsSay(i) {
  if (i < 0 || i >= tts.queue.length) return;
  tts.idx = i; tts.playing = true;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(tts.queue[i]);
  u.lang = "zh-CN"; u.rate = tts.rate; u.pitch = tts.pitch;
  if (tts.voice) u.voice = tts.voice;
  u.onend = () => {
    if (tts.idx < tts.queue.length - 1) { ttsSay(tts.idx + 1); }
    else { tts.playing = false; syncPlayBtn(); if (tts.onDone) { const f = tts.onDone; tts.onDone = null; f(); } }
  };
  u.onerror = () => { tts.playing = false; syncPlayBtn(); };
  window.speechSynthesis.speak(u);
}
function ttsToggle() {
  if (tts.playing) { window.speechSynthesis.pause(); tts.playing = false; syncPlayBtn(); }
  else if (window.speechSynthesis.paused) { window.speechSynthesis.resume(); tts.playing = true; syncPlayBtn(); }
  else ttsSay(tts.idx);
}
function ttsStop() { window.speechSynthesis.cancel(); tts.playing = false; syncPlayBtn(); }
function syncPlayBtn() {
  const b = $("#ttsPlay");
  if (b) b.textContent = tts.playing ? "⏸ 暂停" : (window.speechSynthesis.paused ? "▶️ 继续" : "▶️ 朗读");
}

// ---------- 埋点：切页/离开时上报停留时长（上限5分钟） ----------
let act = { page: "浏览", subject: "", kp_id: "", ts: Date.now() };
function reportAct(page, subject, kp_id) {
  const now = Date.now();
  const secs = Math.round((now - act.ts) / 1000);
  if (secs >= 1 && secs <= 300) {
    const body = JSON.stringify({ page: act.page, subject: act.subject, kp_id: act.kp_id, seconds: secs });
    try { navigator.sendBeacon("/api/activity", body); } catch (e) {}
  }
  act = { page: page || "浏览", subject: subject || "", kp_id: kp_id || "", ts: now };
}
window.addEventListener("beforeunload", () => {
  saveProgress();
  const secs = Math.round((Date.now() - act.ts) / 1000);
  if (secs >= 1 && secs <= 300) {
    const body = JSON.stringify({ page: act.page, subject: act.subject, kp_id: act.kp_id, seconds: secs });
    try { navigator.sendBeacon("/api/activity", body); } catch (e) {}
  }
});

// ---------- 全局状态 ----------
let me = null;
let lesson = null;      // 学习中：{kp_id,name,subject,points,questions,idx,phase,results}
let aiQuiz = null;      // AI 出题会话
let review = { cards: [], idx: 0, peek: false };
const SUBJECTS = ["语文", "数学", "英语", "物理", "化学", "生物"];

// ---------- 页面切换 ----------
const PAGE_ACT = {
  tabLearn: "浏览", tabReview: "复习", tabStats: "统计", tabRecite: "背诵", tabExport: "导出", tabSpace: "空间",
};
function switchTab(tabId) {
  $$(".tab-page").forEach(p => p.classList.add("hidden"));
  $$(".nav-btn").forEach(b => b.classList.remove("active"));
  $("#" + tabId).classList.remove("hidden");
  $$(".nav-btn").find(b => b.dataset.tab === tabId).classList.add("active");
  reportAct(PAGE_ACT[tabId]);
  if (tabId === "tabLearn") renderLearn();
  if (tabId === "tabReview") renderReview();
  if (tabId === "tabStats") renderStats();
  if (tabId === "tabRecite") renderRecite();
  if (tabId === "tabExport") renderExport();
  if (tabId === "tabSpace") renderSpace();
  window.scrollTo(0, 0);
}

// ---------- 顶栏 ----------
async function refreshHeader() {
  try {
    const d = await api("/api/header");
    const nm = (me && me.nickname) || d.uname;
    const av = me && me.avatar
      ? `<img class="h-av" src="/${esc(me.avatar)}" alt="">`
      : `<span class="h-av h-av-t">${esc(String(nm).slice(0, 1))}</span>`;
    $("#headerBar").innerHTML =
      `<button class="h-user" onclick="switchTab('tabSpace')">${av}<span>${esc(nm)}</span></button>` +
      `<span class="h-stat">🔥 ${d.streak} 天</span>` +
      `<span class="h-stat">🏆 ${d.mastered}/${d.total}</span>` +
      `<span class="h-xp">今日 XP ${d.xp_today}/${d.xp_goal} ${d.goal_done ? "✅" : ""}` +
      `<div class="xp-bar"><div style="width:${d.ratio}%"></div></div></span>`;
  } catch (e) { /* 忽略 */ }
}

// ---------- 登录 ----------
async function renderLogin() {
  const d = await api("/api/users");
  const box = $("#loginUsers");
  box.innerHTML = d.users.map(u =>
    `<button class="user-btn" data-id="${esc(u.id)}" data-name="${esc(u.name)}">🧑 ${esc(u.name)}</button>`).join("");
  box.querySelectorAll(".user-btn").forEach(b => b.onclick = () => login(b.dataset.name));
}
async function login(name) {
  const d = await post("/api/login", { name });
  if (!d.ok) { toast(d.error || "登录失败"); return; }
  await enterApp();
}
$("#loginBtn").onclick = () => login($("#newName").value.trim());
$("#newName").oninput = (e) => { $("#loginBtn").disabled = !e.target.value.trim(); };

async function enterApp() {
  me = (await api("/api/me")).user;
  if (!me) { showLogin(); return; }
  $("#loginPage").classList.add("hidden");
  $("#mainPage").classList.remove("hidden");
  await refreshHeader();
  switchTab("tabLearn");
}

function showLogin() {
  $("#mainPage").classList.add("hidden");
  $("#loginPage").classList.remove("hidden");
  renderLogin();
}

// ---------- 学页：课程列表 ----------
let learnSubj = "全部";
async function renderLearn() {
  if (lesson) { renderLesson(); return; }
  if (aiQuiz) { renderAiQuiz(); return; }
  const el = $("#tabLearn");
  el.innerHTML = `<div class="subj-filter">${["全部", ...SUBJECTS].map(s =>
    `<button class="${s === learnSubj ? "active" : ""}" data-s="${s}">${s}</button>`).join("")}</div>` +
    `<div id="lessonList"><div class="spinner">加载中…</div></div>`;
  el.querySelectorAll(".subj-filter button").forEach(b => b.onclick = () => { learnSubj = b.dataset.s; renderLearn(); });
  try {
    const saved = loadProgress();
    const d = await api("/api/lessons?subject=" + encodeURIComponent(learnSubj));
    const list = $("#lessonList");
    if (!list) return;
    if (d.empty) {
      const t = d.empty.kind === "locked" ? `该科目高中课程尚未解锁（${d.empty.n} 节），先完成初中诊断课程即可解锁。`
        : d.empty.kind === "no_quiz" ? `该科目有 ${d.empty.n} 节课程暂无自检题，内容可在「导出」页生成 PDF 学习。`
        : "所有已解锁课程全部通关 🎉 去复习页巩固吧。";
      list.innerHTML = `<div class="chart-card" style="text-align:center;color:#888;padding:26px;">${t}</div>`;
      return;
    }
    if (!d.lessons.length) { list.innerHTML = `<div class="chart-card" style="text-align:center;color:#888;">暂无课程</div>`; return; }
    list.innerHTML = d.lessons.map(l => {
      const cont = saved && saved.kp_id === l.kp_id &&
        (saved.card_idx > 0 || saved.phase !== "learn" || saved.q_idx > 0 ||
         (saved.results || []).length > 0);
      return `<div class="lesson-card">
        <div class="lc-main">
          <div class="lc-name">${iconOf(l.status)} ${esc(l.subject)}·${esc(l.name)}</div>
          <div class="lc-sub">掌握度 ${l.mastery}%｜自检题 ${l.q_done}/${l.q_total}｜约 ${l.minutes} 分钟</div>
        </div>
        <div class="lc-actions">
          ${cont ? `<button class="lc-go" data-kp="${esc(l.kp_id)}">继续 ▶</button>
          <button class="lc-restart" data-kp="${esc(l.kp_id)}">↺ 重学</button>`
          : `<button class="lc-go" data-kp="${esc(l.kp_id)}">开始</button>`}
        </div>
      </div>`;
    }).join("");
    list.querySelectorAll(".lc-go").forEach(b => b.onclick = () => startLesson(b.dataset.kp));
    list.querySelectorAll(".lc-restart").forEach(b => b.onclick = () => restartLesson(b.dataset.kp));
    reportAct("学习", learnSubj === "全部" ? "" : learnSubj, "");
  } catch (e) {
    $("#lessonList").innerHTML = `<div class="chart-card" style="color:#d9534f;">${esc(e.message)}</div>`;
  }
}
function iconOf(status) {
  return { "可学": "▶️", "学习中": "🔶", "需复习": "🔁", "已掌握": "✅", "未解锁": "🔒" }[status] || "▶️";
}

// ---------- 开课 ----------
function restartLesson(kpId) {
  // 重新开始：只清本课的进度记录（其他课的快照不动）
  const saved = loadProgress();
  if (saved && saved.kp_id === kpId) clearProgress();
  deck.idx = 0;
  startLesson(kpId);
}

async function startLesson(kpId) {
  try {
    const d = await post("/api/lesson/start", { kp_id: kpId });
    const saved = loadProgress();
    const has = saved && saved.kp_id === kpId && saved.phase !== "done";
    let phase = has ? (saved.phase === "fb" ? "q" : saved.phase) : "learn";
    let idx = has ? (saved.q_idx || 0) : 0;
    if (has && saved.phase === "fb") idx += 1;   // 反馈页退出 → 从下一题继续
    if (phase === "q" && idx >= d.questions.length) {
      // 练习已答完但没点通关就退了：直接进完成页，不重复领 XP
      lesson = { kp_id: d.kp_id, name: d.name, subject: d.subject, points: d.points,
                 questions: d.questions, idx: 0, phase: "done", results: saved.results || [],
                 rewarded: true, reward: null };
      clearProgress();
      renderLesson();
      return;
    }
    lesson = { kp_id: d.kp_id, name: d.name, subject: d.subject, points: d.points,
               questions: d.questions, idx: idx, phase: phase,
               results: has ? (saved.results || []) : [], rewarded: false };
    deck.idx = has ? (saved.card_idx || 0) : 0;
    renderLesson();
  } catch (e) { toast(e.message); }
}

function progKey() { return "lesson_progress_" + (me ? me.id : "anon"); }
function saveProgress() {
  // 学习中才保存；无课程/已完成/未登录一律不动已有快照（防止列表页关页面误清）
  if (!lesson || lesson.phase === "done" || !me) return;
  try {
    localStorage.setItem(progKey(), JSON.stringify({
      kp_id: lesson.kp_id, phase: lesson.phase,
      card_idx: deck.idx, q_idx: lesson.idx,
      results: lesson.results || [], ts: Date.now(),
    }));
  } catch (e) {}
}
function loadProgress() {
  try { return JSON.parse(localStorage.getItem(progKey()) || "null"); } catch (e) { return null; }
}
function clearProgress() { try { localStorage.removeItem(progKey()); } catch (e) {} }

function exitToLearn() {
  saveProgress();
  lesson = null; aiQuiz = null; deck.idx = 0;
  ttsStop();
  renderLearn();
}

function renderLesson() {
  saveProgress();
  const L = lesson;
  const el = $("#tabLearn");
  if (L.phase === "done") { renderLessonDone(L); return; }
  if (L.phase === "learn") {
    reportAct("学习", L.subject, L.kp_id);
    el.innerHTML = `<div class="page-top"><button class="back-btn" id="exitLearn">← 返回</button></div>
      <h3>📖 ${esc(L.name)}</h3>
      <div class="cap">${L.points.length} 张知识点卡片 · 朗读可自动翻页</div>
      <div id="deckWrap"></div>
      <div class="btn-row">
        <button class="btn primary" id="toQuiz">我学完了，开始练习 ✏️</button>
        <button class="btn ghost" id="skipQuiz">跳过</button>
      </div>`;
    renderDeck(L.points);
    $("#exitLearn").onclick = exitToLearn;
    $("#toQuiz").onclick = () => { L.phase = "q"; L.idx = 0; renderLesson(); };
    $("#skipQuiz").onclick = () => { L.phase = "q"; L.idx = 0; renderLesson(); };
    return;
  }
  // 练习 / 反馈
  reportAct("练习", L.subject, L.kp_id);
  if (L.idx >= L.questions.length) {
    finishLesson(L);
    return;
  }
  const q = L.questions[L.idx];
  el.innerHTML = `<div class="page-top"><button class="back-btn" id="exitQuiz">← 返回列表</button></div>
    <div class="q-progress">
      <div class="bar"><div style="width:${Math.round(L.idx / L.questions.length * 100)}%"></div></div>
      <span>${esc(L.name)} · 第 ${L.idx + 1}/${L.questions.length} 题 · ${q.qtype}</span>
    </div>
    <div class="q-stem">${esc(q.stem)}</div>
    <div id="qBody"></div>`;
  const qb = $("#qBody");
  const eb = $("#exitQuiz"); if (eb) eb.onclick = exitToLearn;
  if (L.phase === "q") {
    if (q.qtype === "选择题") {
      qb.innerHTML = q.options.map((o, i) =>
        `<button class="q-opt" data-i="${i}">${esc(o)}</button>`).join("") +
        `<button class="btn primary mt12" id="submitQ">提交答案</button>`;
      let picked = null;
      qb.querySelectorAll(".q-opt").forEach(b => b.onclick = () => {
        qb.querySelectorAll(".q-opt").forEach(x => x.classList.remove("selected"));
        b.classList.add("selected"); picked = b.dataset.i;
      });
      $("#submitQ").onclick = async () => {
        if (picked == null) { toast("请先选择一个答案"); return; }
        const letter = q.option_letters[parseInt(picked)] || q.options[parseInt(picked)].slice(0, 1);
        await submitAnswer(q, { letter });
      };
    } else if (q.qtype === "填空题") {
      qb.innerHTML = `<input class="q-input" id="fillText" placeholder="多空用 ; 分隔">` +
        `<button class="btn primary mt12" id="submitQ">提交答案</button>`;
      $("#submitQ").onclick = async () => {
        await submitAnswer(q, { text: $("#fillText").value });
      };
    } else {
      qb.innerHTML = `<div class="cap">先在纸上/脑中作答，再看答案诚实自评</div>` +
        `<button class="btn ghost" id="peekQ">看答案</button>`;
      $("#peekQ").onclick = () => { L.phase = "peek"; renderLesson(); };
    }
  } else if (L.phase === "peek") {
    qb.innerHTML = `<div class="fb-answer"><b>答案：</b>${esc(q.answer)}</div>` +
      (q.analysis ? `<div class="fb-answer">解析：${esc(q.analysis)}</div>` : "") +
      `<div class="btn-row">
        <button class="btn success" id="selfRight">✅ 我答对了</button>
        <button class="btn danger" id="selfWrong">❌ 答错了</button>
      </div>`;
    $("#selfRight").onclick = async () => { await selfAnswer(q, true); };
    $("#selfWrong").onclick = async () => { await selfAnswer(q, false); };
  } else if (L.phase === "fb") {
    qb.innerHTML = (L.lastOk
      ? `<div class="fb-correct">✅ 答对了 +5 XP</div>`
      : `<div class="fb-wrong">❌ 答错了，已进错题本（稍后自动复习）</div>`) +
      `<div class="fb-answer"><b>答案：</b>${esc(q.answer)}</div>` +
      (q.analysis ? `<div class="fb-answer">解析：${esc(q.analysis)}</div>` : "") +
      (L.lastOk ? "" : `<select class="attr-select" id="attrSel">
        <option value="">（默认：概念不清）</option>
        ${["概念不清", "方法未掌握", "计算失误", "审题偏差", "时间不够", "表述不规范"].map(a => `<option>${a}</option>`).join("")}
      </select>`) +
      `<button class="btn primary" id="nextQ">${L.idx + 1 >= L.questions.length ? "完成本节 🎉" : "下一题 →"}</button>`;
    const attr = $("#attrSel");
    if (attr) attr.onchange = async () => { if (attr.value) await post("/api/wrong_attr", { qid: q.qid, attribution: attr.value }); };
    $("#nextQ").onclick = () => { L.idx += 1; L.phase = "q"; renderLesson(); };
  }
}

async function submitAnswer(q, payload) {
  const L = lesson;
  const body = Object.assign({ qid: q.qid, kp_id: L.kp_id, qtype: q.qtype, answer: q.answer }, payload);
  try {
    const d = await post("/api/answer", body);
    L.lastOk = d.correct;
    L.results.push(d.correct);
    L.phase = "fb";
    await refreshHeader();
    renderLesson();
  } catch (e) { toast(e.message); }
}
async function selfAnswer(q, ok) {
  const L = lesson;
  try {
    await post("/api/answer_self", { qid: q.qid, correct: ok, kp_id: L.kp_id });
    L.lastOk = ok;
    L.results.push(ok);
    L.phase = "fb";
    await refreshHeader();
    renderLesson();
  } catch (e) { toast(e.message); }
}

async function finishLesson(L) {
  if (L.rewarded) { renderLessonDone(L); return; }
  const allOk = L.results.length > 0 && L.results.every(Boolean);
  const d = await post("/api/lesson/finish", { kp_id: L.kp_id, all_correct: allOk });
  L.rewarded = true; L.reward = d;
  clearProgress();
  await refreshHeader();
  renderLesson();
}
function renderLessonDone(L) {
  const el = $("#tabLearn");
  const r = L.reward || { bonus: 0, newly_unlocked: 0, mastery: 0, status: "学习中" };
  el.innerHTML = `<div style="text-align:center;padding:20px 0 8px;">🎉</div>
    <h3 style="text-align:center;">通关：${esc(L.name)}</h3>
    <div class="chart-card mt12">${r.bonus ? "+" + r.bonus + " XP（全对奖励 " + (L.results.length > 0 && L.results.every(Boolean) ? "已含" : "未含") + "）" : "本课已学完 🎉"}
      <div class="cap mt8">掌握度 ${r.mastery}%（${esc(r.status)}）${r.newly_unlocked ? "｜🔓 解锁了 " + r.newly_unlocked + " 节新课" : ""}</div>
    </div>
    <div class="btn-row">
      <button class="btn primary" id="aiQuizBtn">🤖 AI出题测试（再练5题）</button>
      <button class="btn ghost" id="backList">返回课程列表</button>
    </div>`;
  $("#aiQuizBtn").onclick = () => { aiQuiz = { kp_id: L.kp_id, name: L.name, idx: 0, results: [], phase: "q" }; renderAiQuiz(); };
  $("#backList").onclick = () => { lesson = null; renderLearn(); };
}

// ---------- 知识点卡片（朗读 + 自动翻页） ----------
let deck = { idx: 0, auto: true };
function renderDeck(points) {
  if (!points || !points.length) return;
  deck.idx = Math.min(deck.idx, points.length - 1);
  const wrap = $("#deckWrap");
  if (!wrap) return;
  const i = deck.idx;
  wrap.innerHTML = `
    <div class="deck-progress">
      <div class="bar"><div style="width:${Math.round((i + 1) / points.length * 100)}%"></div></div>
      <span>${i + 1}/${points.length}</span>
    </div>
    <div class="deck-body">${esc(points[i])}</div>
    <div class="deck-help">
      <button class="help-btn ai" id="helpAi">🤖 这句没懂？AI 讲懂</button>
    </div>
    <div id="aiExplainBox"></div>
    <div class="tts-bar">
      <div class="tts-row">
        <button class="tts-mini" id="deckPrev">⏮ 上一条</button>
        <button class="tts-play" id="ttsPlay">▶️ 朗读</button>
        <button class="tts-mini" id="deckNext">⏭ 下一条</button>
        <button class="tts-mini" id="deckAuto">${deck.auto ? "🔁 自动翻页开" : "⏹ 自动翻页关"}</button>
      </div>
      <div class="tts-opt">
        <span>语速</span>
        <input type="range" id="ttsRate" min="0.6" max="1.6" step="0.1" value="${tts.rate}">
        <select id="ttsVoice"></select>
      </div>
    </div>`;
  ttsLoadVoices();
  bindDeck(points);
  saveProgress();
}
function bindDeck(points) {
  $("#deckPrev").onclick = () => { ttsStop(); deck.idx = Math.max(0, deck.idx - 1); renderDeck(points); };
  $("#deckNext").onclick = () => { ttsStop(); deck.idx = Math.min(points.length - 1, deck.idx + 1); renderDeck(points); };
  $("#deckAuto").onclick = () => { deck.auto = !deck.auto; $("#deckAuto").textContent = deck.auto ? "🔁 自动翻页开" : "⏹ 自动翻页关"; };
  $("#ttsRate").oninput = (e) => { tts.rate = parseFloat(e.target.value); localStorage.setItem("tts_rate", String(tts.rate)); };
  $("#ttsVoice").onchange = (e) => {
    const v = tts.voices[parseInt(e.target.value)];
    if (v) { tts.voice = v; localStorage.setItem("tts_voice", v.name); }
  };
  $("#ttsPlay").onclick = () => {
    if (tts.playing || window.speechSynthesis.paused) { ttsToggle(); return; }
    ttsSpeak(points.slice(deck.idx), () => {
      if (deck.auto && deck.idx < points.length - 1) { deck.idx += 1; renderDeck(points); }
    });
  };
  // 遇到不懂的：AI 讲懂
  const curText = () => points[deck.idx] || "";
  $("#helpAi").onclick = async () => {
    const box = $("#aiExplainBox");
    box.innerHTML = `<div class="spinner" style="padding:14px;">🤖 老师正在讲…</div>`;
    try {
      const d = await post("/api/ai_explain", { kp_id: lesson ? lesson.kp_id : "", text: curText() });
      const plain = (d.explain || "").trim();
      box.innerHTML = `<div class="ai-explain">
        <div class="ae-head">🤖 AI 讲懂 · ${esc(lesson ? lesson.name : "")}
          <button class="ae-speak" id="aeSpeak">🔊 朗读讲解</button>
          <button class="ae-close" id="aeClose">✕</button></div>
        <div class="ae-body">${markdownish(plain)}</div></div>`;
      $("#aeClose").onclick = () => { box.innerHTML = ""; ttsStop(); };
      $("#aeSpeak").onclick = () => {
        const paras = plain.split(/\n+/).map(x => x.replace(/^[-*•#\s]+/, "").trim()).filter(Boolean);
        if (paras.length) ttsSpeak(paras);
      };
    } catch (e) {
      box.innerHTML = `<div class="fb-wrong">${esc(e.message)}</div>`;
    }
  };
}
// ---------- AI 出题 ----------
async function renderAiQuiz() {
  const el = $("#tabLearn");
  const A = aiQuiz;
  reportAct("练习", lesson ? lesson.subject : "", lesson ? lesson.kp_id : "");
  if (A.phase === "loading") {
    el.innerHTML = `<div class="page-top"><button class="back-btn" id="exitAi">← 返回列表</button></div>
    <div class="spinner">🤖 DeepSeek 出题中…<br><span style="font-size:12px;">根据「${esc(A.name)}」生成基础测试题</span></div>`;
    try {
      const d = await post("/api/ai_quiz", { kp_id: A.kp_id });
      if (A.cancelled) return;
      A.questions = d.questions || [];
      A.phase = "q";
      renderAiQuiz();
    } catch (e) { toast(e.message); A.phase = "q"; renderAiQuiz(); }
    return;
  }
  if (A.idx >= (A.questions || []).length) {
    const ok = A.results.filter(Boolean).length;
    const total = A.results.length;
    el.innerHTML = `<h3 style="text-align:center;">🤖 AI测试完成</h3>
      <div class="chart-card mt12" style="text-align:center;">答对 <b>${ok} / ${total}</b> 题
        ${ok === total ? "<div class='cap'>全对！掌握得很扎实 🔥</div>"
          : ok >= total * 0.6 ? "<div class='cap'>不错，再复习一下错题就更好了</div>"
          : "<div class='cap'>建议回到知识点卡片再复习一遍</div>"}
      </div>
      <button class="btn primary" id="backFromAi">返回课程列表</button>`;
    $("#backFromAi").onclick = () => { aiQuiz = null; lesson = null; renderLearn(); };
    return;
  }
  const q = A.questions[A.idx];
  el.innerHTML = `<div class="page-top"><button class="back-btn" id="exitAi">← 返回列表</button></div>
    <div class="q-progress">
      <div class="bar"><div style="width:${Math.round(A.idx / A.questions.length * 100)}%"></div></div>
      <span>🤖 AI出题 · 第 ${A.idx + 1}/${A.questions.length} 题 · ${q.qtype}</span>
    </div>
    <div class="q-stem">${esc(q.stem)}</div><div id="qBody"></div>`;
  const qb = $("#qBody");
  const ae = $("#exitAi"); if (ae) ae.onclick = () => { A.cancelled = true; exitToLearn(); };
  if (A.phase === "q") {
    if (q.qtype === "选择题") {
      qb.innerHTML = q.options.map((o, i) => `<button class="q-opt" data-i="${i}">${esc(o)}</button>`).join("") +
        `<button class="btn primary mt12" id="submitAI">提交答案</button>`;
      let picked = null;
      qb.querySelectorAll(".q-opt").forEach(b => b.onclick = () => {
        qb.querySelectorAll(".q-opt").forEach(x => x.classList.remove("selected"));
        b.classList.add("selected"); picked = b.dataset.i;
      });
      $("#submitAI").onclick = () => {
        if (picked == null) { toast("请先选择答案"); return; }
        const letter = (q.options[parseInt(picked)] || "").slice(0, 1);
        A.lastOk = letter.toUpperCase() === (q.answer || "").trim().slice(0, 1).toUpperCase();
        A.results.push(A.lastOk); A.phase = "fb"; renderAiQuiz();
      };
    } else {
      qb.innerHTML = `<input class="q-input" id="aiFill" placeholder="输入答案">` +
        `<button class="btn primary mt12" id="submitAI">提交答案</button>`;
      $("#submitAI").onclick = () => {
        const u = ($("#aiFill").value || "").replace(/\s+/g, "").toLowerCase();
        const ans = String(q.answer || "").split(";").map(x => x.replace(/\s+/g, "").toLowerCase());
        A.lastOk = !!u && ans.includes(u);
        A.results.push(A.lastOk); A.phase = "fb"; renderAiQuiz();
      };
    }
  } else {
    qb.innerHTML = (A.lastOk
      ? `<div class="fb-correct">✅ 答对了</div>`
      : `<div class="fb-wrong">❌ 答错了</div>`) +
      `<div class="fb-answer"><b>答案：</b>${esc(q.answer)}</div>` +
      (q.analysis ? `<div class="fb-answer">解析：${esc(q.analysis)}</div>` : "") +
      `<button class="btn primary mt12" id="nextAI">下一题 →</button>`;
    $("#nextAI").onclick = () => { A.idx += 1; A.phase = "q"; renderAiQuiz(); };
  }
}

// ---------- 复习 ----------
async function renderReview() {
  const el = $("#tabReview");
  el.innerHTML = `<h3>🔁 复习</h3><div id="revBody"><div class="spinner">加载中…</div></div>`;
  try {
    const d = await api("/api/reviews");
    review = { cards: d.cards, idx: 0, peek: false };
    const body = $("#revBody");
    if (!d.cards.length) {
      body.innerHTML = `<div class="chart-card" style="text-align:center;color:#888;padding:26px;">🎉 今日没有到期的复习卡片。</div>`;
      return;
    }
    drawReviewCard();
  } catch (e) { $("#revBody").innerHTML = `<div class="chart-card" style="color:#d9534f;">${esc(e.message)}</div>`; }
}
function drawReviewCard() {
  const el = $("#tabReview");
  if (review.idx >= review.cards.length) {
    el.innerHTML = `<h3>🔁 复习</h3>
      <div class="chart-card" style="text-align:center;padding:30px 0;">🎉 本轮复习完成！共复习 ${review.idx} 张卡。</div>
      <button class="btn primary" id="revAgain">再来一轮检查</button>`;
    $("#revAgain").onclick = () => { review.idx = 0; drawReviewCard(); };
    return;
  }
  const card = review.cards[review.idx];
  el.innerHTML = `<h3>🔁 复习</h3>
    <div class="q-progress"><div class="bar"><div style="width:${Math.round(review.idx / review.cards.length * 100)}%"></div></div>
      <span>${review.idx + 1}/${review.cards.length} · ${esc(card.subject)} · ${esc(card.kind)}</span></div>
    <div class="review-card">
      <div class="review-front">${esc(card.front)}</div>
      <div id="revBack"></div>
    </div>
    <div class="btn-row mt12"><button class="btn ghost" id="peekRev">显示答案</button></div>`;
  $("#peekRev").onclick = () => {
    review.peek = true;
    $("#revBack").innerHTML = `<div class="review-back">${esc(card.back || "（无背面内容）")}</div>`;
    $("#peekRev").parentElement.innerHTML = `<div class="btn-row mt12">
      <button class="btn danger" id="forgotCard">😅 忘了</button>
      <button class="btn success" id="rememberCard">🙂 记得</button></div>`;
    $("#forgotCard").onclick = async () => { await post("/api/review", { card_id: card.card_id, remembered: false }); review.idx += 1; review.peek = false; await refreshHeader(); drawReviewCard(); };
    $("#rememberCard").onclick = async () => { await post("/api/review", { card_id: card.card_id, remembered: true }); review.idx += 1; review.peek = false; await refreshHeader(); drawReviewCard(); };
  };
}

// ---------- 统计 ----------
async function renderStats() {
  const el = $("#tabStats");
  el.innerHTML = `<h3>📊 学习统计</h3><div class="spinner">加载中…</div>`;
  try {
    const d = await api("/api/stats");
    const t = d.time;
    el.innerHTML = `<h3>📊 学习统计</h3>
      <div class="metric-row">
        <div class="metric"><div class="m-val">${t.today_min}</div><div class="m-label">今日（分）</div></div>
        <div class="metric"><div class="m-val">${t.week_min}</div><div class="m-label">本周（分）</div></div>
        <div class="metric"><div class="m-val">${t.total_min}</div><div class="m-label">累计（分）</div></div>
      </div>
      ${barsHtml("每日学习分钟（近14天）", t.per_day, "min")}
      ${barsHtml("各科学习分钟（近14天）", t.per_subject, "min")}
      ${barsHtml("各科掌握率（%）", Object.fromEntries(d.mastery.by_subject.map(m => [m.subject, m.pct])), "%")}
      <div class="chart-card"><div class="cc-title">未掌握知识点（${d.mastery.weak.length} 个）</div>
        ${d.mastery.weak.slice(0, 12).map(w => `<div class="weak-item">${esc(w.subject)} · ${esc(w.name)} · ${esc(w.status)} · ${w.mastery}%</div>`).join("")}
        ${d.mastery.weak.length > 12 ? `<div class="cap">…共 ${d.mastery.weak.length} 个</div>` : ""}
      </div>
      ${Object.keys(d.wrong.attributions).length ? barsHtml("未解决错题归因", d.wrong.attributions, "题") : ""}
      ${barsHtml("每日做题正确率（近14天，%）", d.accuracy.per_day, "%")}
      <div class="chart-card"><div class="cc-title">累计作答 ${d.accuracy.total_n} 题 · 总正确率 ${d.accuracy.total_pct}%</div></div>
      <div class="chart-card"><div class="cc-title">一轮总进度 ${d.progress.mastered} / ${d.progress.total} 知识点已掌握</div>
        <div class="bars" style="height:40px;">${d.progress.tree.map(t =>
          `<div class="bar-item"><div class="b" style="height:${Math.max(3, Math.round(t.mastered / Math.max(1, t.total) * 36))}px;background:#1fd16f;"></div>
           <div class="b-l">${esc(t.subject)} ${t.mastered}/${t.total}</div></div>`).join("")}
        </div></div>
      <div class="chart-card" style="margin-top:10px;">
        <div class="cc-title">🤖 AI 学习建议</div>
        <div class="cap">只发送你的学习统计汇总（不含姓名/账号等身份信息），由 DeepSeek 分析。AI 建议仅供参考。</div>
        <button class="btn primary mt12" id="genAdvice">生成 AI 学习建议</button>
        <div id="adviceBox"></div>
      </div>
      <button class="btn ghost mt16" id="logoutBtn">🔄 切换用户 / 退出</button>`;
    $("#genAdvice").onclick = async () => {
      const box = $("#adviceBox");
      box.innerHTML = `<div class="spinner">DeepSeek 正在分析你的学习数据…</div>`;
      try {
        const d = await post("/api/ai_advice", {});
        box.innerHTML = `<div class="advice-box">${markdownish(d.advice)}</div>
          <div class="cap mt8">—— AI 建议仅供参考，请结合自身情况判断 ——</div>`;
      } catch (e) {
        box.innerHTML = `<div class="fb-wrong">${esc(e.message)}</div>`;
      }
    };
    $("#logoutBtn").onclick = async () => { await post("/api/logout", {}); me = null; lesson = null; aiQuiz = null; showLogin(); };
  } catch (e) {
    el.innerHTML = `<h3>📊 学习统计</h3><div class="chart-card" style="color:#d9534f;">${esc(e.message)}</div>`;
  }
}
function barsHtml(title, data, unit) {
  const items = Object.entries(data || {});
  if (!items.length) return "";
  const max = Math.max(1, ...items.map(i => i[1]));
  return `<div class="chart-card"><div class="cc-title">${esc(title)}</div>
    <div class="bars">${items.map(([k, v]) =>
      `<div class="bar-item"><div class="b" style="height:${Math.max(3, Math.round(v / max * 96))}px;"></div>
       <div class="b-v">${v}</div><div class="b-l">${esc(k)}</div></div>`).join("")}
    </div></div>`;
}
function markdownish(txt) {
  let s = esc(txt);
  s = s.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>");
  s = s.replace(/^###?\s+(.+)$/gm, "<h3>$1</h3>");
  s = s.replace(/^- (.+)$/gm, "• $1");
  s = s.replace(/\n/g, "<br>");
  return s;
}

// ---------- 背诵 ----------
let recite = { subject: "语文", catIdx: 0, items: [], kpId: "", kw: "" };
let reciteCatalog = null;
async function renderRecite() {
  const el = $("#tabRecite");
  if (!reciteCatalog) {
    el.innerHTML = `<h3>📖 背诵听读</h3><div class="spinner">加载中…</div>`;
    try { reciteCatalog = await api("/api/recite_catalog"); } catch (e) { el.innerHTML = `<div class="chart-card" style="color:#d9534f;">${esc(e.message)}</div>`; return; }
  }
  const cats = reciteCatalog[recite.subject] || [];
  if (recite.catIdx >= cats.length) recite.catIdx = 0;
  const [kpId, catName] = cats[recite.catIdx] || ["", ""];
  recite.kpId = kpId;
  el.innerHTML = `<h3>📖 背诵听读</h3>
    <div class="cap">出门随身背：选分类→逐条听读，已背打勾自动保存</div>
    <div class="subj-filter">${Object.keys(reciteCatalog).map(s =>
      `<button class="${s === recite.subject ? "active" : ""}" data-s="${s}">${s}</button>`).join("")}</div>
    <div class="recite-cat">${cats.map((c, i) =>
      `<button class="${i === recite.catIdx ? "active" : ""}" data-i="${i}">${esc(c[1])}</button>`).join("")}</div>
    <input class="recite-search" id="reciteKw" placeholder="🔍 搜索关键词（留空显示全部）" value="${esc(recite.kw)}">
    <div class="recite-count" id="reciteCount">…</div>
    <div id="reciteBody"><div class="spinner">加载中…</div></div>`;
  el.querySelectorAll(".subj-filter button").forEach(b => b.onclick = () => { recite.subject = b.dataset.s; recite.catIdx = 0; renderRecite(); });
  el.querySelectorAll(".recite-cat button").forEach(b => b.onclick = () => { recite.catIdx = parseInt(b.dataset.i); renderRecite(); });
  $("#reciteKw").oninput = (e) => { recite.kw = e.target.value; filterRecite(); };
  try {
    const d = await api("/api/recite/" + encodeURIComponent(kpId));
    recite.items = d.items || [];
    reportAct("背诵", recite.subject, kpId);
    filterRecite();
  } catch (e) { $("#reciteBody").innerHTML = `<div class="chart-card" style="color:#d9534f;">${esc(e.message)}</div>`; }
}
function filterRecite() {
  const items = recite.kw ? recite.items.filter(p => p.toLowerCase().includes(recite.kw.toLowerCase())) : recite.items;
  const done = reciteDoneSet(recite.kpId);
  $("#reciteCount").textContent = `共 ${items.length} 条`;
  const box = $("#reciteBody");
  box.innerHTML = `<div class="tts-bar"><div class="tts-row">
      <button class="tts-btn" onclick="ttsSpeak(${JSON.stringify(items).replace(/"/g, "&quot;")})">▶️ 全部连播</button>
      <button class="tts-btn" onclick="ttsStop()">⏹ 停止</button>
      <span style="font-size:10px;color:#888;margin-left:auto;">已背 ${done.size}/${items.length}</span>
    </div></div>` +
    items.map((p, i) => {
      const isDone = done.has(i);
      return `<div class="recite-item ${isDone ? "done" : ""}">
        <input type="checkbox" ${isDone ? "checked" : ""} data-i="${i}">
        <div class="r-text">${esc(p)}</div>
        <button class="tts-mini" data-i="${i}">🔊</button></div>`;
    }).join("") || `<div class="chart-card" style="text-align:center;color:#888;">没有匹配内容</div>`;
  box.querySelectorAll(".recite-item input[type=checkbox]").forEach(cb => cb.onchange = () => toggleReciteDone(recite.kpId, parseInt(cb.dataset.i), cb.checked));
  box.querySelectorAll(".tts-mini").forEach(b => b.onclick = () => ttsSpeak([items[parseInt(b.dataset.i)]]));
}
function reciteDoneKey(kpId) { return "recite_done_" + kpId; }
function reciteDoneSet(kpId) {
  try { return new Set(JSON.parse(localStorage.getItem(reciteDoneKey(kpId)) || "[]")); } catch (e) { return new Set(); }
}
function toggleReciteDone(kpId, i, checked) {
  const s = reciteDoneSet(kpId);
  checked ? s.add(i) : s.delete(i);
  localStorage.setItem(reciteDoneKey(kpId), JSON.stringify(Array.from(s).sort((a, b) => a - b)));
  filterRecite();
}

// ---------- 导出 ----------
function renderExport() {
  const el = $("#tabExport");
  el.innerHTML = `<h3>📄 导出 PDF</h3>
    <div class="cap">生成的 PDF 可发送到电脑打印，或手机连打印机直接打。</div>
    <div class="export-card"><p>每日学习单＝按你当前进度排（已掌握的自动跳过）。排多少天？</p>
      <input type="range" id="expDays" min="7" max="90" step="1" value="30" style="width:100%;">
      <div class="cap" id="expDaysLabel">30 天</div>
      <a id="dailyLink" href="/api/export/daily?days=30" download><button class="mt8">📄 生成《每日学习单》PDF</button></a>
    </div>
    <div class="export-card"><p>总复习文档＝全部知识点讲解+练习，按科目分章（生成较慢，请耐心）。</p>
      <a href="/api/export/review" download><button>📚 生成《高考总复习·知识点详解》PDF</button></a>
    </div>
    <div class="export-card"><p>背诵手册＝语文名句 + 英语词汇 + 作文模板。</p>
      <a href="/api/export/dictation" download><button>📖 生成《背诵手册》PDF</button></a>
    </div>`;
  $("#expDays").oninput = (e) => { $("#expDaysLabel").textContent = e.target.value + " 天"; $("#dailyLink").href = "/api/export/daily?days=" + e.target.value; };
}

// ---------- 启动 ----------
(async function init() {
  $$(".nav-btn").forEach(b => b.onclick = () => switchTab(b.dataset.tab));
  try { me = (await api("/api/me")).user; } catch (e) { me = null; }
  if (me) { await enterApp(); } else { showLogin(); }
})();


// ================== 📖 空间（成长记录） ==================
const space = {
  month: "", selDate: "", camStream: null, camShot: null,
  notePics: [], notePriv: false,
  priv: { enabled: false, unlocked: false },
  profile: null, monthData: null, weights: [],
  _aiing: false,
};
const SPACE_MOODS = ["😀 开心", "😐 平淡", "😔 低落", "💪 加油", "🤯 疲惫"];

function todayStr() { const d = new Date(); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }

function compressImg(dataURL, maxW) {
  maxW = maxW || 1280;
  return new Promise((res) => {
    const img = new Image();
    img.onload = () => {
      try {
        const scale = Math.min(1, maxW / img.width);
        const c = document.createElement("canvas");
        c.width = Math.max(1, Math.round(img.width * scale));
        c.height = Math.max(1, Math.round(img.height * scale));
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
        res(c.toDataURL("image/jpeg", 0.82));
      } catch (e) { res(dataURL); }
    };
    img.onerror = () => res(dataURL);
    img.src = dataURL;
  });
}
function fileToDataURL(f) {
  return new Promise((res) => {
    const r = new FileReader();
    r.onload = () => res(r.result);
    r.readAsDataURL(f);
  });
}

async function renderSpace() {
  const el = $("#tabSpace");
  try {
    me = (await api("/api/me")).user;
    refreshHeader();
  } catch (e) {}
  const [profile, status, month, weights, list, today] = await Promise.all([
    api("/api/profile").catch(() => ({})),
    api("/api/diary/private/status").catch(() => ({ enabled: false, unlocked: false })),
    api("/api/diary/month?ym=" + space.month).catch(() => ({ days: {}, streak: 0, total_sign: 0 })),
    api("/api/weight/list").catch(() => ({ items: [] })),
    api("/api/diary/list").catch(() => ({ items: [] })),
    api("/api/diary/day?date=" + todayStr()).catch(() => ({ date: todayStr(), sign: null, note: null, weight: null })),
  ]);
  space.profile = profile; space.monthData = month; space.weights = weights.items || [];
  space.priv = { enabled: !!status.enabled, unlocked: !!status.unlocked };
  space.selDate = space.selDate || todayStr();

  const nm = (me && me.nickname) || (me && me.name) || "";
  const av = (profile && profile.avatar) || (me && me.avatar) || "";
  const bd = (profile && profile.birthday) || "";
  el.innerHTML = `
  <div class="qq-cover">
    <div class="cover-deco d1"></div><div class="cover-deco d2"></div><div class="cover-deco d3"></div>
    <div class="cover-ava">${av ? `<img src="/${esc(av)}" alt="">` : esc(String(nm).slice(0, 1) || "我")}</div>
    <div class="cover-name">${esc(nm || "同学")}</div>
    <div class="cover-sig">${bd ? "🎂 " + esc(bd) + " · " : ""}坚持复习，每天进步一点点</div>
    <button class="cover-edit" onclick="openSettings()">✏️ 编辑资料</button>
    <div class="cover-badge">🔥 连签 ${month.streak} 天</div>
  </div>

  ${space.priv.unlocked ? `<div class="priv-tip"><span>🔓</span> 隐秘空间已解锁（30分钟内有效）</div>` : ""}
  ${renderWeightCard()}
  ${renderSignCard(today)}
  ${renderNoteCard()}
  <div class="space-card"><h4>📅 时间轴</h4>${renderCal(month, today)}</div>
  <div class="space-card">${renderPrivCard()}</div>
  <div class="space-card"><h4>🕰 全部记录</h4>${renderTimeline(list.items || [])}</div>
  <div style="height:20px"></div>`;
  bindSpaceEvents();
}

function renderSignCard(today) {
  const t = todayStr();
  if (today && today.sign) {
    const s = today.sign;
    return `<div class="space-card sign-card">
      <div class="sign-row">
        <div class="sign-cam done">
          ${s.photos && s.photos[0] ? `<img src="/${esc(s.photos[0])}" alt="签到照">` : `<span class="cam-ico">📷</span>`}
          <div class="cam-hint">今日已签</div>
        </div>
        <div class="sign-main">
          <div class="sign-title">📷 今日签到 <span class="sd-badge">✓ ${s.is_late ? "补签" : "完成"}</span></div>
          <div class="sign-mood-txt">${esc(s.mood || "今天也坚持下来了 💪")}</div>
          <div class="dv-meta">${esc((s.created_at || "").slice(5, 16))}</div>
        </div>
      </div>
    </div>`;
  }
  return `<div class="space-card sign-card">
    <div class="sign-row">
      <div class="sign-cam" id="signCam" title="点击拍照">
        ${space.camShot ? `<img src="${space.camShot}" alt="预览">` : `<span class="cam-ico">📷</span>`}
        <div class="cam-hint">${space.camShot ? "点击重拍" : "点击自拍"}</div>
      </div>
      <div class="sign-main">
        <div class="sign-title">今日自拍签到</div>
        <div class="tip" style="margin:2px 0 8px;">每天一张照片 + 一句话，见证 90 天的坚持</div>
        <input id="signMood" class="input" placeholder="今天的一句话…" maxlength="50">
      </div>
    </div>
    <div class="cam-wrap hidden" id="camWrap"></div>
    <div class="mood-row" id="moodRow"></div>
    <div class="btn-row">
      <button class="btn ghost" id="signPick">🖼 从相册选择</button>
      <button class="btn primary" id="submitSign">✅ 完成签到</button>
    </div>
    <input type="file" id="signFile" accept="image/*" style="display:none">
  </div>`;
}

function renderNoteCard() {
  return `<div class="space-card note-card">
    <div class="card-head"><span class="card-ico">💬</span>随手记</div>
    <textarea id="noteText" class="input" placeholder="今天学了什么？有什么想法、心情、反思？"></textarea>
    <div class="photo-pre" id="notePics"></div>
    <div class="photo-add" id="noteAddPic">＋</div>
    <input type="file" id="noteFile" accept="image/*" multiple style="display:none">
    <label class="priv-switch"><input type="checkbox" id="notePriv"> 🔒 存入隐秘空间（需高级密码才可见）</label>
    <div id="noteAiOut"></div>
    <div class="btn-row">
      <button class="btn ghost" id="noteAi">✨ AI 整理</button>
      <button class="btn primary" id="noteSave">💾 保存</button>
    </div>
  </div>`;
}

function renderWeightCard() {
  const last = space.weights[space.weights.length - 1];
  return `<div class="space-card weight-card">
    <div class="card-head"><span class="card-ico">⚖️</span>体重记录
      ${last ? `<span class="card-sub">上次 ${last.value} kg · ${esc(last.date.slice(5))}</span>` : ""}
    </div>
    <div class="weight-row">
      <input id="wValue" class="input" type="number" step="0.1" min="20" max="300" placeholder="${last ? last.value + " kg" : "kg"}">
      <button class="btn primary" id="wSave" style="width:auto;padding:10px 18px;">记录</button>
    </div>
    <div class="weight-chart">${weightSvg(space.weights)}</div>
  </div>`;
}

function weightSvg(items) {
  if (!items || items.length < 1) return `<div class="w-note">还没有体重记录，记录第一条开始吧</div>`;
  const last = items.slice(-14);
  const W = 320, H = 120, pad = 26;
  const vals = last.map(i => i.value);
  const min = Math.min.apply(null, vals), max = Math.max.apply(null, vals);
  const span = Math.max(0.5, max - min);
  const px = (i) => pad + i * (W - pad * 2) / Math.max(1, last.length - 1);
  const py = (v) => H - pad - (v - min) / span * (H - pad * 2);
  const pts = last.map((i, idx) => px(idx).toFixed(1) + "," + py(i.value).toFixed(1)).join(" ");
  const lastP = last[last.length - 1];
  const diff = items.length > 1 ? (items[items.length - 1].value - items[items.length - 2].value) : 0;
  return `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">
    <polyline points="${pts}" fill="none" stroke="#4a90d9" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${px(last.length - 1)}" cy="${py(lastP.value)}" r="4" fill="#4a90d9"/>
  </svg>
  <div class="w-note">最近：${lastP.value} kg${diff !== 0 ? "（" + (diff > 0 ? "+" : "") + diff.toFixed(1) + "）" : ""} · 共 ${items.length} 条</div>`;
}

function renderCal(month, today) {
  const ym = space.month || todayStr().slice(0, 7);
  const [y, m] = ym.split("-").map(Number);
  const days = month.days || {};
  const first = new Date(y, m - 1, 1).getDay();
  const ndays = new Date(y, m, 0).getDate();
  const t = todayStr();
  let cells = `<div class="cw">日</div><div class="cw">一</div><div class="cw">二</div><div class="cw">三</div><div class="cw">四</div><div class="cw">五</div><div class="cw">六</div>`;
  for (let i = 0; i < first; i++) cells += `<div class="cd blank"></div>`;
  for (let d = 1; d <= ndays; d++) {
    const ds = ym + "-" + String(d).padStart(2, "0");
    const info = days[ds] || {};
    const dots = (info.sign ? '<i class="s"></i>' : "") + (info.note ? '<i class="n"></i>' : "") + (info.weight != null ? '<i class="w"></i>' : "");
    const cls = ["cd", ds === space.selDate ? "sel" : "", ds === t ? "today" : ""].join(" ");
    cells += `<div class="${cls}" onclick="pickDate('${ds}')">${d}<span class="dot">${dots}</span></div>`;
  }
  return `<div class="cal-head">
    <button onclick="setMonth(-1)">‹</button>
    <span class="cal-m">${y} 年 ${m} 月</span>
    <button onclick="setMonth(1)">›</button>
  </div>
  <div class="cal-grid">${cells}</div>
  <div class="cal-stats">
    <span>📷 签到 <b>${month.total_sign}</b></span>
    <span>🔥 连续 <b>${month.streak}</b> 天</span>
    <span class="tip">●绿=签到 ●蓝=随手记 ●橙=体重</span>
  </div>
  <div id="dayView"></div>`;
}

function renderTimeline(items) {
  if (!items.length) return `<div class="tip">还没有记录，从今天的签到开始吧</div>`;
  return items.map(it => `
    <div class="tl-item">
      <div class="tl-date">${esc(it.date)}<br><span style="font-size:11px;">${esc((it.created_at || "").slice(11, 16))}</span></div>
      <div class="tl-body">
        <span class="tl-tag">${it.label}</span>
        ${it.is_private && it.locked ? `<div class="locked-note">🔒 隐秘内容（需高级密码）</div>`
          : `<div class="tl-txt">${esc(it.mood ? "【" + it.mood + "】" : "")}${esc(it.text || it.summary || "")}</div>`}
        ${it.category ? `<div class="dv-meta">分类：${esc(it.category)}${it.summary ? " · " + esc(it.summary) : ""}</div>` : ""}
        ${(it.photos || []).slice(0, 3).map(ph => `<img src="${(it.is_private ? "/api/diary/private/photo?p=" : "/") + esc(ph)}" alt="">`).join("")}
      </div>
    </div>`).join("");
}

function renderPrivCard() {
  const p = space.priv;
  const body = !p.enabled ? `
    <div class="tip">设置高级密码后，可把不想被别人看到的记录存进隐秘空间（后台加密存储）</div>
    <div class="priv-row"><input id="privNew" class="input" type="password" placeholder="设置高级密码（至少4位）"></div>
    <button class="btn primary" id="privSet" style="margin-top:8px">🔒 开启隐秘空间</button>`
    : (!p.unlocked ? `
    <div class="tip">输入高级密码解锁，30 分钟内可查看和写入隐秘内容</div>
    <div class="priv-row"><input id="privPwd" class="input" type="password" placeholder="高级密码"></div>
    <button class="btn primary" id="privUnlock" style="margin-top:8px">🔓 解锁</button>
    <div style="margin-top:8px"><button class="btn ghost" id="privChange">修改密码</button></div>`
    : `
    <div class="tip">已解锁，随手记勾选"🔒 存入隐秘空间"即可写入；内容在服务器后台以密文存储</div>
    <div class="btn-row">
      <button class="btn ghost" id="privLock">🔐 立即锁定</button>
      <button class="btn ghost" id="privChange2">修改密码</button>
    </div>`);
  return `<h4>🔒 隐秘空间</h4>${body}`;
}

function bindSpaceEvents() {
  // 签到（自拍 + 心情合一）
  const sc = $("#signCam");
  if (sc) sc.onclick = () => {
    if (space.camShot) { space.camShot = null; renderSpace(); return; }
    startCam();
  };
  const sf = $("#signFile");
  const sp = $("#signPick");
  if (sp) sp.onclick = () => { if (sf) sf.click(); };
  if (sf) sf.onchange = async (e) => {
    const f = e.target.files && e.target.files[0];
    if (!f) return;
    const d = await fileToDataURL(f);
    if (!d.startsWith("data:image/")) { toast("请选择图片"); return; }
    space.camShot = d;
    renderSpace();
  };
  const moodRow = $("#moodRow");
  if (moodRow) {
    moodRow.innerHTML = SPACE_MOODS.map(m => `<button class="mood-btn" data-m="${esc(m)}">${esc(m)}</button>`).join("");
    moodRow.querySelectorAll(".mood-btn").forEach(b => b.onclick = () => {
      const inp = $("#signMood"); if (!inp) return;
      const em = b.dataset.m.split(" ")[0];
      inp.value = (inp.value ? inp.value + " " : "") + em;
      moodRow.querySelectorAll(".mood-btn").forEach(x => x.classList.remove("sel"));
      b.classList.add("sel");
    });
  }
  const ss = $("#submitSign");
  if (ss) ss.onclick = submitSign;
  // 随手记
  const nf = $("#noteFile"), addPic = $("#noteAddPic");
  if (nf) nf.onchange = async (e) => {
    for (const f of e.target.files || []) {
      if (space.notePics.length >= 6) break;
      const d = await fileToDataURL(f);
      if (d.startsWith("data:image/")) space.notePics.push(d);
    }
    renderNotePics(); nf.value = "";
  };
  if (addPic) addPic.onclick = () => { const f = $("#noteFile"); if (f) f.click(); };
  const np = $("#notePriv");
  if (np) np.onchange = (e) => {
    space.notePriv = e.target.checked;
    if (space.notePriv && !space.priv.unlocked) {
      toast("先在下方解锁隐秘空间");
      e.target.checked = false; space.notePriv = false;
    }
  };
  const ai = $("#noteAi");
  if (ai) ai.onclick = aiOrganize;
  const sv = $("#noteSave");
  if (sv) sv.onclick = saveNote;
  // 体重
  const ws = $("#wSave");
  if (ws) ws.onclick = saveWeight;
  // 隐秘
  const ps = $("#privSet");
  if (ps) ps.onclick = async () => {
    const v = ($("#privNew").value || "").trim();
    if (v.length < 4) { toast("密码至少4位"); return; }
    try { await post("/api/diary/private/config", { new_pwd: v }); toast("隐秘空间已开启 🔒"); renderSpace(); }
    catch (e) { toast(e.message); }
  };
  const pu = $("#privUnlock");
  if (pu) pu.onclick = async () => {
    const v = ($("#privPwd").value || "").trim();
    if (!v) { toast("输入密码"); return; }
    try { await post("/api/diary/private/unlock", { pwd: v }); toast("已解锁 🔓"); renderSpace(); }
    catch (e) { toast(e.message); }
  };
  const pl = $("#privLock");
  if (pl) pl.onclick = async () => { await post("/api/diary/private/lock", {}); toast("已锁定"); renderSpace(); };
  const pc = $("#privChange") || $("#privChange2");
  if (pc) pc.onclick = () => openPrivChange();
}

function renderNotePics() {
  const box = $("#notePics"); if (!box) return;
  box.innerHTML = space.notePics.map((d, i) =>
    `<div class="pp"><img src="${d}" alt=""><span class="pp-x" data-i="${i}">×</span></div>`).join("");
  box.querySelectorAll(".pp-x").forEach(x => x.onclick = () => {
    space.notePics.splice(Number(x.dataset.i), 1); renderNotePics();
  });
  const add = $(".photo-add");
  if (add) add.style.display = space.notePics.length >= 6 ? "none" : "flex";
}

async function startCam() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    toast("此浏览器不支持摄像头，可改用手机浏览器");
    return;
  }
  try {
    space.camStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" }, audio: false });
    const w = $("#camWrap");
    if (!w) return;
    w.classList.remove("hidden");
    w.innerHTML = `<video id="camVideo" autoplay playsinline></video>
      <button class="cam-snap" id="camSnap">📸 拍照</button>`;
    w.querySelector("video").srcObject = space.camStream;
    $("#camSnap").onclick = snapShot;
  } catch (e) {
    toast("摄像头无法打开：" + (e.name === "NotAllowedError" ? "请允许摄像头权限" : "设备不可用"));
  }
}
function snapShot() {
  const v = $("#camVideo"); if (!v) return;
  const c = document.createElement("canvas");
  c.width = v.videoWidth || 640; c.height = v.videoHeight || 480;
  c.getContext("2d").drawImage(v, 0, 0, c.width, c.height);
  space.camShot = c.toDataURL("image/jpeg", 0.85);
  stopCam();
  renderSpace();
}
function stopCam() {
  if (space.camStream) {
    space.camStream.getTracks().forEach(t => t.stop());
    space.camStream = null;
  }
  const w = $("#camWrap");
  if (w) w.classList.add("hidden");
}
async function submitSign() {
  if (!space.camShot) { toast("先拍一张自拍"); return; }
  try {
    const img = await compressImg(space.camShot);
    await post("/api/diary/save", {
      date: todayStr(), kind: "sign",
      mood: ($("#signMood").value || "").trim(),
      photos: [img],
    });
    space.camShot = null;
    toast("签到成功 🎉");
    renderSpace();
  } catch (e) { toast(e.message); }
}

async function aiOrganize() {
  const t = ($("#noteText").value || "").trim();
  if (!t) { toast("先写点内容"); return; }
  if (space.notePriv) { toast("隐秘内容不能发给 AI 整理"); return; }
  if (space._aiing) return;
  space._aiing = true;
  $("#noteAiOut").innerHTML = `<div class="spinner">✨ AI 整理中…</div>`;
  try {
    const r = await post("/api/diary/ai_organize", { text: t });
    $("#noteAiOut").innerHTML =
      `<div class="ai-result"><span class="ai-cat">${esc(r.category)}</span>${esc(r.summary)}` +
      (r.advice ? `<br><span style="color:#888">💡 ${esc(r.advice)}</span>` : "") + `</div>`;
  } catch (e) {
    $("#noteAiOut").innerHTML = `<div class="ai-result" style="color:#d9534f">${esc(e.message)}</div>`;
  }
  space._aiing = false;
}

async function saveNote() {
  const t = ($("#noteText").value || "").trim();
  if (!t && !space.notePics.length) { toast("写点什么或传张图吧"); return; }
  // 直接读勾选状态（兼容程序化勾选未触发 onchange 的情况）
  const privBox = $("#notePriv");
  if (privBox && privBox.checked) space.notePriv = true;
  if (space.notePriv && !space.priv.unlocked) { toast("请先解锁隐秘空间"); return; }
  const aiOut = $("#noteAiOut").querySelector(".ai-cat");
  try {
    const imgs = [];
    for (const d of space.notePics) imgs.push(await compressImg(d));
    await post("/api/diary/save", {
      date: todayStr(), kind: "note", text: t, photos: imgs,
      is_private: space.notePriv ? 1 : 0,
      category: aiOut ? aiOut.textContent : "",
      summary: aiOut ? ($("#noteAiOut").textContent.split("💡")[0] || "").replace(aiOut.textContent, "").trim().slice(0, 100) : "",
      advice: aiOut ? (($("#noteAiOut").textContent.match(/💡(.*)/) || [])[1] || "").trim() : "",
    });
    space.notePics = [];
    $("#noteText").value = "";
    $("#noteAiOut").innerHTML = "";
    toast(space.notePriv ? "已存入隐秘空间 🔒" : "已保存 📝");
    renderSpace();
  } catch (e) { toast(e.message); }
}

async function saveWeight() {
  const v = parseFloat(($("#wValue").value || "").trim());
  if (!(v >= 20 && v <= 300)) { toast("体重需在 20-300 kg 之间"); return; }
  try {
    await post("/api/weight/save", { date: todayStr(), value: v });
    toast("已记录 ⚖️");
    renderSpace();
  } catch (e) { toast(e.message); }
}

async function pickDate(ds) {
  space.selDate = ds;
  const dv = $("#dayView"); if (!dv) return;
  try {
    const d = await api("/api/diary/day?date=" + ds);
    let html = `<div class="day-view" style="margin-top:10px"><div style="font-size:12px;color:#888;margin-bottom:6px">${esc(ds)}</div>`;
    if (d.sign) html += dvItem(d.sign, "📷 签到", ds);
    if (d.note) html += dvItem(d.note, "📝 随手记", ds);
    if (d.weight) html += `<div class="dv-item"><span class="tl-tag">⚖️ 体重</span><div class="dv-txt">${d.weight.value} kg${d.weight.note ? " · " + esc(d.weight.note) : ""}</div>
      <button class="dv-del" onclick="delWeight('${ds}')">删除</button></div>`;
    if (!d.sign && !d.note && !d.weight) html += `<div class="tip">这一天还没有记录</div>`;
    dv.innerHTML = html + `</div>`;
  } catch (e) { toast(e.message); }
}

function dvItem(it, tag, ds) {
  return `<div class="dv-item">
    ${it.photos && it.photos[0] ? `<img src="${(it.is_private ? "/api/diary/private/photo?p=" : "/") + esc(it.photos[0])}" alt="">` : ""}
    <div class="dv-txt">
      <span class="tl-tag">${tag}${it.is_private ? " 🔒" : ""}</span>
      ${it.locked ? `<div class="locked-note">🔒 隐秘内容，需高级密码</div>` : `<div>${esc(it.mood ? "【" + it.mood + "】" : "")}${esc(it.text || "")}</div>`}
      ${it.category ? `<div class="dv-meta">分类：${esc(it.category)}${it.summary ? " · " + esc(it.summary) : ""}</div>` : ""}
      <div class="dv-meta">${esc(it.created_at || "")}</div>
    </div>
    <button class="dv-del" onclick="delDiary(${it.id})">删除</button>
  </div>`;
}

async function delDiary(id) {
  if (!confirm("删除这条记录？")) return;
  try { await post("/api/diary/delete", { id }); toast("已删除"); renderSpace(); } catch (e) { toast(e.message); }
}
async function delWeight(ds) {
  if (!confirm("删除这天的体重记录？")) return;
  try { await post("/api/weight/delete", { date: ds }); toast("已删除"); renderSpace(); } catch (e) { toast(e.message); }
}

async function setMonth(delta) {
  const [y, m] = (space.month || todayStr().slice(0, 7)).split("-").map(Number);
  const d = new Date(y, m - 1 + delta, 1);
  space.month = d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0");
  renderSpace();
}

// ---------- 用户设置 ----------
function openSettings() {
  const p = space.profile || {};
  const av = p.avatar || "";
  const mask = document.createElement("div");
  mask.className = "modal-mask";
  mask.innerHTML = `<div class="modal" onclick="event.stopPropagation()">
    <h3>👤 个人设置</h3>
    <div class="row"><label>头像</label>
      <div class="av-up">
        ${av ? `<img id="setAv" src="/${esc(av)}" alt="">` : `<div class="space-avatar" id="setAv">${esc(String(me && (me.nickname || me.name) || "我").slice(0, 1))}</div>`}
        <button class="btn ghost" style="width:auto;padding:8px 14px;" id="avUp">上传头像</button>
        <input type="file" id="avFile" accept="image/*" style="display:none">
      </div>
    </div>
    <div class="row"><label>昵称</label><input id="setName" class="input" maxlength="12" value="${esc(p.nickname || (me && me.name) || "")}"></div>
    <div class="row"><label>生日</label><input id="setBirth" class="input" type="date" value="${esc(p.birthday || "")}"></div>
    <div class="btn-row">
      <button class="btn ghost" id="setCancel">取消</button>
      <button class="btn primary" id="setSave">保存</button>
    </div>
  </div>`;
  document.body.appendChild(mask);
  $("#setCancel").onclick = () => mask.remove();
  mask.onclick = () => mask.remove();
  const af = $("#avFile");
  $("#avUp").onclick = () => af.click();
  af.onchange = async (e) => {
    const f = e.target.files && e.target.files[0];
    if (!f) return;
    const d = await fileToDataURL(f);
    if (!d.startsWith("data:image/")) { toast("请选择图片"); return; }
    try {
      const img = await compressImg(d, 512);
      const r = await post("/api/profile/avatar", { data: img });
      toast("头像已更新");
      mask.remove();
      renderSpace();
    } catch (err) { toast(err.message); }
  };
  $("#setSave").onclick = async () => {
    try {
      await post("/api/profile/save", {
        nickname: ($("#setName").value || "").trim(),
        birthday: ($("#setBirth").value || "").trim(),
      });
      toast("已保存");
      mask.remove();
      renderSpace();
    } catch (err) { toast(err.message); }
  };
}

function openPrivChange() {
  const mask = document.createElement("div");
  mask.className = "modal-mask";
  mask.innerHTML = `<div class="modal" onclick="event.stopPropagation()">
    <h3>🔒 修改高级密码</h3>
    <div class="row"><label>旧密码</label><input id="pcOld" class="input" type="password"></div>
    <div class="row"><label>新密码（至少4位）</label><input id="pcNew" class="input" type="password"></div>
    <div class="btn-row">
      <button class="btn ghost" id="pcCancel">取消</button>
      <button class="btn primary" id="pcSave">修改</button>
    </div>
  </div>`;
  document.body.appendChild(mask);
  $("#pcCancel").onclick = () => mask.remove();
  mask.onclick = () => mask.remove();
  $("#pcSave").onclick = async () => {
    try {
      await post("/api/diary/private/config", {
        old_pwd: $("#pcOld").value,
        new_pwd: $("#pcNew").value,
      });
      toast("密码已修改");
      mask.remove();
      renderSpace();
    } catch (e) { toast(e.message); }
  };
}
