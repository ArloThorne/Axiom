import os
import json

def display_status():
    manifest_path = os.path.expanduser("~/storage/shared/Axiom/core/system_manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            data = json.load(f)
        print("==================================================")
        print("          AXIOM SOVEREIGN STATUS NODE             ")
        print("==================================================")
        for key, value in data.items():
            print(f"[{key.upper()}] -> {value}")
        print("==================================================")
    else:
        print("[STATUS] Error: System manifest not found. Run compiler.")

if __name__ == "__main__":
    display_status()
