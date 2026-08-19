import os
import subprocess
import sys

def run_health_checks():
    print("[DAEMON] Initiating Axiom universal health diagnostics...")
    scripts_to_test = [
        "scripts/net_check.py",
        "scripts/integrity_check.py",
        "scripts/sys_monitor.py"
    ]
    
    for script in scripts_to_test:
        if os.path.exists(script):
            print(f"[DAEMON] Executing diagnostic target: {script}")
            result = subprocess.run([sys.executable, script], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"[SUCCESS] {script} passed verification.")
            else:
                print(f"[WARNING] {script} reported a non-zero exit code.")
        else:
            print(f"[MISSING] Target script not found: {script}")
            
    print("[DAEMON] Health diagnostic cycle complete.")

if __name__ == "__main__":
    run_health_checks()
