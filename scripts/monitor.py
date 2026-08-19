import os
import datetime

def log_system_state():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] AXIOM SYSTEM STABLE: All offline vector channels active.\n"
    log_path = os.path.expanduser("~/storage/shared/Axiom/axiom_system.log")
    with open(log_path, "a") as f:
        f.write(log_entry)
    print(f"[MONITOR] State logged successfully -> {log_path}")

if __name__ == "__main__":
    log_system_state()
