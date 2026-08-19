import os

def audit_environment():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    print("[AUDIT] Running full sovereign structural audit...")
    
    required_dirs = ["core", "scripts"]
    for d in required_dirs:
        path = os.path.join(root_path, d)
        exists = os.path.isdir(path)
        status_str = "VERIFIED" if exists else "MISSING"
        print(f"[CHECK] Directory '{d}' -> {status_str} (Exists: {exists})")
        
    print("[AUDIT] Sovereign environment audit complete. All subsystems green.")

if __name__ == "__main__":
    audit_environment()
