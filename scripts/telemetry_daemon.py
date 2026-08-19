import os
import datetime
import shutil
import json

def log_telemetry():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check storage statistics of shared storage
    total, used, free = shutil.disk_usage(root_path)
    free_mb = free // (2^20)
    
    # Count active core and script nodes
    core_files = len(os.listdir(os.path.join(root_path, "core"))) if os.path.exists(os.path.join(root_path, "core")) else 0
    script_files = len(os.listdir(os.path.join(root_path, "scripts"))) if os.path.exists(os.path.join(root_path, "scripts")) else 0
    
    telemetry_entry = {
        "timestamp": timestamp,
        "free_space_bytes": free,
        "core_node_count": core_files,
        "script_node_count": script_files,
        "status": "NOMINAL"
    }
    
    log_path = os.path.join(root_path, "core/telemetry_log.json")
    
    # Append or initialize log list
    history = []
    if os.path.exists(log_path):
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            pass
            
    history.append(telemetry_entry)
    
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)
        
    print(f"[TELEMETRY] System state logged successfully at {timestamp}.")

if __name__ == "__main__":
    log_telemetry()
