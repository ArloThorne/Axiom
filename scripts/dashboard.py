import os
import json
import shutil
import datetime

def render_dashboard():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    manifest_path = os.path.join(root_path, "core/system_manifest.json")
    log_path = os.path.join(root_path, "core/system_operations.log")
    
    print("==================================================")
    print("         AXIOM SOVEREIGN MASTER DASHBOARD         ")
    print("==================================================")
    print(f"Timestamp   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Node ID     : pixel_6a_axiom_01")
    print(f"Operator    : Arlo Thorne")
    print("--------------------------------------------------")
    
    # Count markdown files
    md_count = sum(len(files) for _, _, files in os.walk(root_path) if any(f.endswith('.md') for f in files))
    print(f"Vault Nodes : {md_count} Markdown documents indexed")
    
    # Storage check
    total, used, free = shutil.disk_usage(root_path)
    print(f"Storage Free: {free // (1024 * 1024)} MB available")
    
    # Recent logs
    print("--------------------------------------------------")
    print("Recent Operations:")
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-3:]:
                print(f"  {line.strip()}")
    else:
        print("  No operational logs recorded.")
    print("==================================================")

if __name__ == "__main__":
    render_dashboard()
