import os
import json
from collections import Counter

def synthesize_vault():
    vault_path = os.path.expanduser("~/storage/shared/Axiom")
    print("[INTEL] Scanning vault nodes for semantic extraction...")
    
    word_counter = Counter()
    markdown_files = 0
    
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                markdown_files += 1
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        words = f.read().lower().split()
                        word_counter.update(words)
                except Exception:
                    pass
                    
    top_keywords = word_counter.most_common(10)
    report = {
        "markdown_files_scanned": markdown_files,
        "top_keywords": top_keywords
    }
    
    report_path = os.path.expanduser("~/storage/shared/Axiom/core/vault_intel.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
        
    print(f"[INTEL] Synthesized {markdown_files} markdown files. Report compiled to core/vault_intel.json")

if __name__ == "__main__":
    synthesize_vault()
