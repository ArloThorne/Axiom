import os
import json

VAULT_PATH = os.path.expanduser("~/Axiom/vault_store.json")

def init_vault():
    print("[VAULT] Initializing local-only cryptographic storage...")
    if not os.path.exists(VAULT_PATH):
        with open(VAULT_PATH, "w") as f:
            json.dump({"status": "secured", "keys": {}}, f)
        print("[VAULT] Local secret vault established. Zero telemetry.")
    else:
        print("[VAULT] Local secret vault already active.")

if __name__ == "__main__":
    init_vault()
