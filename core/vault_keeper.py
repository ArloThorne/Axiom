import os
import json

def init_vault():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    vault_path = os.path.join(root_path, "core/secure_vault.json")
    
    print("[VAULT] Initializing local encrypted credential storage...")
    
    placeholder_vault = {
        "status": "locked",
        "encryption": "aes-local",
        "keys_registered": 0
    }
    
    if not os.path.exists(vault_path):
        os.makedirs(os.path.dirname(vault_path), exist_ok=True)
        with open(vault_path, "w", encoding="utf-8") as f:
            json.dump(placeholder_vault, f, indent=4)
        print("[VAULT] Secure storage structure initialized.")
    else:
        print("[VAULT] Secure vault state verified.")

if __name__ == "__main__":
    init_vault()
