import os
import tarfile
import datetime

def create_archive():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"axiom_backup_{timestamp}.tar.gz"
    target_dir = os.path.expanduser("~/storage/shared/Axiom")
    backup_path = os.path.expanduser(f"~/storage/shared/{backup_name}")
    
    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(target_dir, arcname=os.path.basename(target_dir))
    
    print(f"[BACKUP] Sovereign archive secured -> {backup_path}")

if __name__ == "__main__":
    create_archive()
