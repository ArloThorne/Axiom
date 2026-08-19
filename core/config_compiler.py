import json
import os
import datetime

def compile_config():
    config_data = {
        "node_id": "pixel_6a_axiom_01",
        "operator": "Arlo Thorne",
        "environment": "Termux-Android",
        "compiled_at": datetime.datetime.now().isoformat(),
        "storage_mount": "~/storage/shared/Axiom",
        "status": "SOVEREIGN_SECURE"
    }
    output_path = os.path.expanduser("~/storage/shared/Axiom/core/system_manifest.json")
    with open(output_path, "w") as f:
        json.dump(config_data, f, indent=4)
    print(f"[COMPILER] System manifest compiled -> {output_path}")

if __name__ == "__main__":
    compile_config()
