import os
import json

def track_media():
    root_path = os.path.expanduser("~/storage/shared/Axiom")
    media_file = os.path.join(root_path, "core/media_manifest.json")
    
    print("[MEDIA] Initializing sovereign media and narrative tracker...")
    
    catalog = {
        "graphic_novels": ["Bunny vs Monkey"],
        "cinematic_projects": ["Predator: Badlands", "Tenet"],
        "status": "synchronized"
    }
    
    os.makedirs(os.path.dirname(media_file), exist_ok=True)
    with open(media_file, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=4)
        
    print(f"[MEDIA] Manifest secured. Tracking active narrative vectors.")

if __name__ == "__main__":
    track_media()
