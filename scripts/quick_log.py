import os
import datetime

def log_entry():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    log_file = os.path.join(root_path, "core/system_operations.log")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] SOVEREIGN_NODE_ACTIVE // GRID_STABLE\n"
    
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    print(f"[LOG] Operational timestamp appended -> {timestamp}")

if __name__ == "__main__":
    log_entry()
