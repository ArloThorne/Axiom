import os
import shutil

def purge_workspace():
    print("[PURGE] Initiating Axiom workspace sanitation...")
    root_dir = os.path.expanduser("~/storage/shared/Axiom")
    removed_files = 0
    
    for root, dirs, files in os.walk(root_dir):
        for d in dirs:
            if d == "__pycache__":
                cache_path = os.path.join(root, d)
                shutil.rmtree(cache_path)
                print(f"[REMOVED] Cache directory: {cache_path}")
                removed_files += 1
                
        for f in files:
            if f.endswith((".log", ".tmp", ".bak")):
                file_path = os.path.join(root, f)
                os.remove(file_path)
                print(f"[REMOVED] Temporary artifact: {file_path}")
                removed_files += 1
                
    print(f"[PURGE] Sanitation complete. Cleared {removed_files} target objects.")

if __name__ == "__main__":
    purge_workspace()
