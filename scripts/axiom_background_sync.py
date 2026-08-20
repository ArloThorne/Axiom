import subprocess
from pathlib import Path

SCRIPTS_DIR = Path.home() / "Axiom" / "scripts"

def run_background_cycle():
    print("[*] Running background ZK Prover cycle...")
    subprocess.run(["python3", str(SCRIPTS_DIR / "axiom_zk_prover.py")])
    print("[*] Running background ZK Verifier cycle...")
    subprocess.run(["python3", str(SCRIPTS_DIR / "axiom_zk_verifier.py")])

if __name__ == "__main__":
    run_background_cycle()
