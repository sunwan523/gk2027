import subprocess
import time
import os

os.chdir("d:\\codex\\gaokao")

while True:
    try:
        process = subprocess.Popen([
            "streamlit", "run", "app.py",
            "--server.port", "9999",
            "--server.address", "0.0.0.0",
            "--server.headless", "true"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        process.wait()
        time.sleep(5)
    except Exception as e:
        time.sleep(5)
