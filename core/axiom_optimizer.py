import os
import json

def optimize_environment():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    print("[OPTIMIZER] Initiating sovereign environmental cleanup...")
    
    cleaned_count = 0
    target_extensions = [".tmp", ".bak"]
    
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if any(file.endswith(ext) for ext in target_extensions):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"[OPTIMIZER] Purged obsolete artifact -> {file}")
                cleaned_count += 1
                
    print(f"[OPTIMIZER] Cleanup complete. {cleaned_count} temporary artifacts removed. System state optimized.")

if __name__ == "__main__":
    optimize_environment()
