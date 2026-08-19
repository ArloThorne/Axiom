import os

def audit_telemetry():
    print("[TELEMETRY] Scanning Axiom workspace for potential data leaks...")
    root_dir = os.path.expanduser("~/storage/shared/Axiom")
    
    external_endpoints_found = 0
    restricted_keywords = ["analytics", "telemetry", "tracking", "beacon"]
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith((".py", ".json", ".conf")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().lower()
                        for keyword in restricted_keywords:
                            if keyword in content and "telemetry_audit" not in file:
                                print(f"[WARNING] Potential tracking keyword '{keyword}' found in {file_path}")
                                external_endpoints_found += 1
                except Exception:
                    pass
                    
    if external_endpoints_found == 0:
        print("[TELEMETRY] Zero telemetry or tracking vectors detected. Workspace is sovereign.")
    else:
        print(f"[TELEMETRY] Audit complete. Flagged {external_endpoints_found} potential points of interest.")

if __name__ == "__main__":
    audit_telemetry()
