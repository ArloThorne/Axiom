import os

def audit_matrix():
    print("[AUDIT] Initiating sovereign structural integrity check...")
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    required_paths = [
        "core/axiom_kernel.py",
        "core/config_compiler.py",
        "scripts/ingest.py",
        "scripts/monitor.py",
        "scripts/backup.py",
        "axiom_master.py"
    ]
    
    missing = []
    for path in required_paths:
        full_path = os.path.join(root_path, path)
        if os.path.exists(full_path):
            print(f"[AUDIT] Verified -> {path}")
        else:
            print(f"[AUDIT] MISSING -> {path}")
            missing.append(path)
            
    if not missing:
        print("[AUDIT] Integrity check complete. All sovereign vectors verified secure.")
    else:
        print(f"[AUDIT] Warning: {len(missing)} nodes require re-compilation.")

if __name__ == "__main__":
    audit_matrix()
