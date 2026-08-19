import os
import json

def synthesize_intel():
    vault_path = os.path.expanduser("~/storage/shared/Axiom")
    print("[INTEL] Synthesizing markdown index and structural headers...")
    
    vault_index = {}
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), vault_path)
                vault_index[rel_path] = {"status": "indexed"}
                
    intel_file = os.path.join(vault_path, "core/vault_intel.json")
    os.makedirs(os.path.dirname(intel_file), exist_ok=True)
    
    with open(intel_file, "w", encoding="utf-8") as f:
        json.dump(vault_index, f, indent=4)
        
    print(f"[INTEL] Synthesis complete. {len(vault_index)} notes cataloged.")

if __name__ == "__main__":
    synthesizer_intel()
