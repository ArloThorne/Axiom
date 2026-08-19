import os
import shutil
import datetime

def create_backup():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    backup_dir = os.path.expanduser("~/storage/shared/AxiomBackups")
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(backup_dir, f"axiom_backup_{timestamp}")
    
    print("[BACKUP] Packaging Axiom workspace for secure redundancy...")
    shutil.make_archive(backup_filename, 'zip', root_path)
    print(f"[BACKUP] Archive successfully generated at: {backup_filename}.zip")

if __name__ == "__main__":
    create_backup()
