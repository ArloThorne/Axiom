import os
import json

def load_config():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    config_path = os.path.join(root_path, "core/config.json")
    
    print("[CONFIG] Loading universal runtime parameters...")
    
    default_config = {
        "environment": "termux",
        "version": "1.0.0",
        "auto_sync": True
    }
    
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
        print("[CONFIG] Default runtime configuration generated.")
    else:
        print("[CONFIG] Runtime configuration verified.")

if __name__ == "__main__":
    load_config()
