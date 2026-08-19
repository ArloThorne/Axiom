import os
import datetime

def log_event(action):
    log_dir = os.path.expanduser("~/Axiom/logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "axiom_activity.log")
    
    timestamp = datetime.datetime.now().isoformat()
    entry = f"[{timestamp}] EXECUTED: {action}\n"
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[LOGGER] Recorded action '{action}' to secure local vault.")

if __name__ == "__main__":
    log_event("manual_audit_check")
