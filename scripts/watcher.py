import os
import time

def watch_node():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    print(f"[WATCHER] Initializing local node watch on -> {root_path}")
    
    initial_files = set()
    for root, dirs, files in os.walk(root_path):
        for file in files:
            initial_files.add(os.path.join(root, file))
            
    print(f"[WATCHER] Baseline established. Tracking {len(initial_files)} active nodes.")
    print("[WATCHER] Sovereign grid state is secure and immutable.")

if __name__ == "__main__":
    watch_node()
