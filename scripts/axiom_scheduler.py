import subprocess

def execute_pipeline():
    print("[SCHEDULER] Initiating full sovereign execution pipeline...")
    
    tasks = [
        ("python3 scripts/telemetry_daemon.py", "Telemetry Logging Daemon"),
        ("python3 scripts/intel_synthesizer.py", "Vault Intelligence Synthesizer"),
        ("python3 scripts/audit.py", "Structural Integrity Auditor"),
        ("python3 scripts/quick_sync.py", "Automated Quick-Sync Pipeline")
    ]
    
    for cmd, desc in tasks:
        print(f"\n[SCHEDULER] Running -> {desc}")
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            print(f"[SCHEDULER] Error encountered in {desc}. Halting chain.")
            break
            
    print("\n[SCHEDULER] Pipeline execution cycle completed.")

if __name__ == "__main__":
    execute_pipeline()
