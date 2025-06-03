import subprocess
import time

PHONE_IP = '192.168.30.85'  
SCAN_INTERVAL = 60
restreamer_path = "/Users/admin/.Trash/backend 11-44-47-965/intern-training/restreamer/restreamer.py"

restreamer_process = None

def is_phone_connected():
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", PHONE_IP],  
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Ping failed: {e}")
        return False

while True:
    print("hello", flush=True)
    if is_phone_connected():
        if restreamer_process is None or restreamer_process.poll() is not None:
            print("Phone is online! Launching restreamer.py", flush=True)
            restreamer_process = subprocess.Popen(["python3", restreamer_path])
        else:
            print("Restreamer already running.", flush=True)
    else:
        print("Phone not detected.", flush=True)
    time.sleep(SCAN_INTERVAL)
