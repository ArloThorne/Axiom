import os
from pathlib import Path

VAULT_DIR = Path.home() / "Axiom"
SCRIPTS_DIR = VAULT_DIR / "scripts"
PROOFS_DIR = VAULT_DIR / ".axiom" / "proofs"
REPORTS_DIR = VAULT_DIR / ".axiom" / "reports"

def audit_system():
    print("========================================")
    print("     PROJECT AXIOM SYSTEM AUDIT        ")
    print("========================================")
    
    # Check Directories
    dirs = {"Vault": VAULT_DIR, "Scripts": SCRIPTS_DIR, "Proofs": PROOFS_DIR, "Reports": REPORTS_DIR}
    for name, path in dirs.items():
        exists = path.exists() and path.is_dir()
        print(f"[{('OK' if exists else 'MISSING')}] {name} Directory: {path}")

    # Check Core Scripts
    scripts = ["axiom_zk_prover.py", "axiom_background_sync.py", "axiom_init.py"]
    for s in scripts:
        sp = SCRIPTS_DIR / s
        print(f"[{('OK' if sp.exists() else 'MISSING')}] Script: {s}")

    # Count Generated Artifacts
    proof_count = len(list(PROOFS_DIR.glob("*.json"))) if PROOFS_DIR.exists() else 0
    report_count = len(list(REPORTS_DIR.glob("*.html"))) if REPORTS_DIR.exists() else 0
    print(f"[*] Total Stored Proofs: {proof_count}")
    print(f"[*] Total HTML Reports: {report_count}")
    print("========================================")

if __name__ == "__main__":
    audit_system()
