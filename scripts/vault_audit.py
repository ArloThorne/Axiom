import os

def audit_vault_permissions():
    print("[VAULT] Initiating security and permission audit...")
    root_dir = os.path.expanduser("~/storage/shared/Axiom")
    target_dirs = ["core", "scripts"]
    
    issues_found = 0
    for target in target_dirs:
        dir_path = os.path.join(root_dir, target)
        if os.path.exists(dir_path):
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_stat = os.stat(file_path)
                    file_mode = oct(file_stat.st_mode)[-3:]
                    
                    # Check if file has overly permissive access (e.g., world-readable)
                    if file_mode[2] != '0':
                        print(f"[WARNING] Permissive access detected on {file_path} ({file_mode})")
                        os.chmod(file_path, 0o600)
                        print(f"[RESOLVED] Restrictive permissions (600) enforced on {file_path}")
                        issues_found += 1
                        
    if issues_found == 0:
        print("[VAULT] All core and script components adhere to strict security standards.")
    else:
        print(f"[VAULT] Audit complete. Corrected {issues_found} permission anomalies.")

if __name__ == "__main__":
    audit_vault_permissions()
