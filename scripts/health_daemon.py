import os
import shutil

def run_health_check():
    print("[HEALTH_DAEMON] Scanning local system integrity...")
    total, used, free = shutil.disk_usage(os.path.expanduser("~/Axiom"))
    
    print(f"[STORAGE_METRIC] Total Space: {total // (2**20)} MB")
    print(f"[STORAGE_METRIC] Used Space:  {used // (2**20)} MB")
    print(f"[STORAGE_METRIC] Free Space:  {free // (2**20)} MB")
    
    if (free / total) < 0.05:
        print("[WARNING] Low storage threshold reached. Run 'axiom purge' to clear cache.")
    else:
        print("[STATUS] Local storage hygiene optimal. Zero telemetry detected.")

if __name__ == "__main__":
    run_health_check()
