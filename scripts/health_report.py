import os
import json
import shutil
import datetime

def generate_health_report():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    manifest_path = os.path.join(root_path, "core/system_manifest.json")
    intel_path = os.path.join(root_path, "core/vault_intel.json")
    
    print("==================================================")
    print("         AXIOM SYSTEM HEALTH TELEMETRY            ")
    print("==================================================")
    print(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
        print(f"Node ID: {manifest.get('node_id', 'N/A')}")
        print(f"Environment: {manifest.get('environment', 'N/A')}")
    
    if os.path.exists(intel_path):
        with open(intel_path, "r") as f:
            intel = json.load(f)
        print(f"Indexed Markdown Files: {intel.get('markdown_files_scanned', 0)}")
    
    total, used, free = shutil.disk_usage(root_path)
    free_mb = free // (1024 * 1024)
    print(f"Available Storage: {free_mb} MB")
    print("==================================================")

if __name__ == "__main__":
    generate_health_report()
