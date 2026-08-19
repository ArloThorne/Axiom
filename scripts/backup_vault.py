import os
import tarfile
import datetime

def backup_vault():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    backup_dir = os.path.expanduser("~/storage/shared/AxiomBackups")
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"axiom_backup_{timestamp}.tar.gz")
    
    print(f"[BACKUP] Packaging sovereign repository into -> {backup_file}")
    
    with tarfile.open(backup_file, "w:gz") as tar:
        tar.add(root_path, arcname=os.path.basename(root_path))
        
    print(f"[BACKUP] Archival complete. Redundancy state secured.")

if __name__ == "__main__":
    backup_vault()
