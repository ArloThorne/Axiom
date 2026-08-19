import os
import shutil

def monitor_resources():
    print("[MONITOR] Scanning Termux environment resources...")
    total, used, free = shutil.disk_usage(os.path.expanduser("~"))
    print(f"[STORAGE] Total: {total // (2**20)} MB | Used: {used // (2**20)} MB | Free: {free // (2**20)} MB")
    print("[MONITOR] Resource telemetry check complete.")

if __name__ == "__main__":
    monitor_resources()
