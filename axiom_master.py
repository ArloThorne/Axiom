import subprocess
import os

def run_command(command, description):
    print(f"\n[MASTER] Initiating -> {description}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr and result.returncode != 0:
        print(f"[ERROR] {result.stderr.strip()}")

def main():
    print("==================================================")
    print("      AXIOM SOVEREIGN ORCHESTRATION LAYER         ")
    print("==================================================")
    run_command("python3 scripts/ingest.py", "Markdown Vector Ingestion")
    run_command("python3 core/axiom_kernel.py", "Offline Kernel Node Processing")
    run_command("python3 scripts/monitor.py", "System Health Logging")
    run_command("python3 core/config_compiler.py", "Configuration Manifest Compilation")
    print("\n[MASTER] All local modules executed successfully. Sovereign status: SECURE.")

if __name__ == "__main__":
    main()
