# -*- coding: utf-8 -*-
"""手机学习服务管理：start / stop / restart / status / autostart / autostop。

服务以隐藏窗口后台运行（日志写 logs/mobile.log），关窗口不会带走服务；
要停就 svc.py stop。开机自启 = 在 Windows 启动文件夹放一个快捷方式，
登录时静默拉起（若已在运行则跳过）。

端口固定 8577（不常用端口，便于以后做映射/隧道）。
"""
from __future__ import annotations

import os
import socket
import subprocess
import sys
import time
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from config import PUBLIC_URL, SERVER_PORT
PORT = SERVER_PORT
PID_FILE = os.path.join(BASE, "data", "mobile.pid")
LOG_FILE = os.path.join(BASE, "logs", "mobile.log")
PY = sys.executable.replace("pythonw.exe", "python.exe")
PYW = os.path.join(os.path.dirname(PY), "pythonw.exe")
APP = os.path.join(BASE, "mobile.py")

DETACHED = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP


# ------------------------------------------------------------------
def _pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    out = subprocess.run(["tasklist", "/FI", "PID eq %d" % pid, "/NH"],
                         capture_output=True, text=True).stdout
    return str(pid) in out


def _read_pid() -> int | None:
    try:
        pid = int(open(PID_FILE).read().strip())
    except (OSError, ValueError):
        return None
    return pid if _pid_alive(pid) else None


def _health() -> bool:
    try:
        r = urllib.request.urlopen("http://localhost:%d/_stcore/health" % PORT,
                                   timeout=2)
        return r.status == 200
    except Exception:
        return False


def _lan_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


# ------------------------------------------------------------------
def cmd_start() -> int:
    if _read_pid() and _health():
        print("已在运行（PID %d），无需重复启动。" % _read_pid())
        return 0
    if _health():
        print("端口 %d 已被占用且服务健康——可能是旧窗口启动的，未记录 PID。" % PORT)
        print("局域网：http://%s:%d" % (_lan_ip(), PORT))
        print("外网：%s" % PUBLIC_URL)
        return 0
    os.makedirs(os.path.dirname(PID_FILE), exist_ok=True)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    log = open(LOG_FILE, "ab")
    proc = subprocess.Popen(
        [PY, "-m", "streamlit", "run", APP,
         "--server.address", "0.0.0.0", "--server.port", str(PORT),
         "--server.headless", "true", "--browser.gatherUsageStats", "false"],
        stdout=log, stderr=log, cwd=BASE, creationflags=DETACHED,
        close_fds=True)
    open(PID_FILE, "w").write(str(proc.pid))
    for _ in range(30):
        if _health():
            print("已启动（PID %d）" % proc.pid)
            print("局域网：http://%s:%d" % (_lan_ip(), PORT))
            print("外网：%s" % PUBLIC_URL)
            return 0
        time.sleep(0.6)
    print("启动超时，请查看日志：%s" % LOG_FILE)
    return 1


def cmd_stop() -> int:
    pid = _read_pid()
    if not pid:
        if _health():
            print("服务在跑但没有 PID 记录（可能是窗口方式启动的）。")
            print("请关闭那个黑色窗口，或手动结束占用 %d 端口的进程。" % PORT)
            return 1
        print("服务未运行。")
        return 0
    subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"],
                   capture_output=True)
    try:
        os.remove(PID_FILE)
    except OSError:
        pass
    print("已停止（PID %d）。" % pid)
    return 0


def cmd_restart() -> int:
    cmd_stop()
    time.sleep(1)
    return cmd_start()


def cmd_status() -> int:
    pid = _read_pid()
    alive = bool(pid) and _health()
    if pid and not _health():
        print("进程在（PID %d）但端口无响应——可能还在启动中，稍后再看。" % pid)
        return 0
    if alive:
        print("● 运行中   PID %d   端口 %d" % (pid, PORT))
        print("  局域网： http://%s:%d" % (_lan_ip(), PORT))
        print("  外网：   %s" % PUBLIC_URL)
        print("  日志：   %s" % LOG_FILE)
    else:
        print("○ 未运行。启动：svc_start.bat 或 python svc.py start")
    return 0 if alive else 3


# ------------------------------------------------------------------
def _startup_dir() -> str:
    import ctypes
    from ctypes import wintypes
    CSIX_STARTUP = 0x7
    buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(0, CSIX_STARTUP, 0, 0, buf)
    return buf.value


def cmd_autostart() -> int:
    """在启动文件夹放快捷方式：登录时 pythonw 静默执行 svc.py _autorun。"""
    sd = _startup_dir()
    lnk = os.path.join(sd, "gk2027-mobile.lnk")
    ps = r'''
$ws = New-Object -ComObject WScript.Shell
$l = $ws.CreateShortcut('%s')
$l.TargetPath = '%s'
$l.Arguments = 'svc.py _autorun'
$l.WorkingDirectory = '%s'
$l.Save()
''' % (lnk.replace("'", "''"), PYW.replace("'", "''"), BASE.replace("'", "''"))
    tmp = os.path.join(BASE, "data", "_autostart.ps1")
    os.makedirs(os.path.dirname(tmp), exist_ok=True)
    open(tmp, "w", encoding="utf-8").write(ps)
    subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
                    "-File", tmp], check=True)
    os.remove(tmp)
    print("已设置开机自启：%s" % lnk)
    print("取消：python svc.py autostop")
    return 0


def cmd_autostop() -> int:
    lnk = os.path.join(_startup_dir(), "gk2027-mobile.lnk")
    if os.path.exists(lnk):
        os.remove(lnk)
        print("已取消开机自启。")
    else:
        print("未设置过开机自启。")
    return 0


def cmd_autorun() -> int:
    """开机静默拉起：已在运行则什么都不做。"""
    if _health():
        return 0
    return cmd_start()


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "status"
    fn = {"start": cmd_start, "stop": cmd_stop, "restart": cmd_restart,
          "status": cmd_status, "autostart": cmd_autostart,
          "autostop": cmd_autostop, "_autorun": cmd_autorun}.get(cmd)
    if fn is None:
        print(__doc__)
        return 2
    return fn()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
