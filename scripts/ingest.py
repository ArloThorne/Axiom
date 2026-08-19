import os

def scan_vault():
    print("[AXIOM] Scanning local vault for unindexed nodes...")
    vault_path = os.path.expanduser("~/storage/shared/Axiom")
    files = [f for f in os.listdir(vault_path) if f.endswith(".md")]
    print(f"[AXIOM] Found {len(files)} localized markdown vectors.")

if __name__ == "__main__":
    scan_vault()
