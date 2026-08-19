import os
import datetime
import json

def log_event(level, message):
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    log_dir = os.path.join(root_path, "core/logs")
    log_path = os.path.join(log_dir, "system.log")
    
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] [{level.upper()}] {message}\n"
    
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    print(log_entry.strip())

if __name__ == "__main__":
    log_event("INFO", "Axiom system logger initialized successfully.")
