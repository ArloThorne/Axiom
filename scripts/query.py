import os
import sys

def query_vault():
    if len(sys.argv) < 2:
        print("[QUERY] Usage: python3 scripts/query.py <keyword>")
        return
        
    term = sys.argv[1].lower()
    vault_path = os.path.expanduser("~/storage/shared/Axiom")
    print(f"[QUERY] Searching vault nodes for term: '{term}'...")
    
    matches = 0
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if term in content.lower():
                            print(f"[MATCH] Found in -> {os.path.relpath(full_path, vault_path)}")
                            matches += 1
                except Exception:
                    pass
                    
    print(f"[QUERY] Search complete. Total matching nodes: {matches}")

if __name__ == "__main__":
    query_vault()
