import os

def verify_integrity():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    required_paths = [
        "core/config.json",
        "core/secure_vault.json",
        "core/logs/system.log",
        "core/config_loader.py",
        "core/logger.py",
        "core/vault_keeper.py",
        "scripts/net_check.py",
        "scripts/axiom_runner.py"
    ]
    
    print("[INTEGRITY] Scanning Axiom workspace for required components...")
    missing = []
    
    for path in required_paths:
        full_path = os.path.join(root_path, path)
        if os.path.exists(full_path):
            print(f"[VERIFIED] {path}")
        else:
            print(f"[MISSING] {path}")
            missing.append(path)
            
    if not missing:
        print("[INTEGRITY] All core systems and utility scripts verified successfully.")
    else:
        print(f"[WARNING] Integrity check failed. Missing components: {len(missing)}")

if __name__ == "__main__":
    verify_integrity()
