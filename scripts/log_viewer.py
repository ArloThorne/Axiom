import os
import json

def view_telemetry_logs():
    log_path = os.path.expanduser("~/storage/shared/Axiom/core/telemetry_log.json")
    print("==================================================")
    print("         AXIOM TELEMETRY HISTORY LOG              ")
    print("==================================================")
    
    if not os.path.exists(log_path):
        print("[LOGS] No telemetry history found. Run scheduler.")
        return
        
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            history = json.load(f)
            
        for entry in history[-5:]:  # Display last 5 entries
            print(f"Timestamp : {entry.get('timestamp')}")
            print(f"Status    : {entry.get('status')}")
            print(f"Core Nodes: {entry.get('core_node_count')}")
            print(f"Scripts   : {entry.get('script_node_count')}")
            print("-" * 50)
    except Exception as e:
        print(f"[LOGS] Error reading telemetry log: {e}")

if __name__ == "__main__":
    view_telemetry_logs()
