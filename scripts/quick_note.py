import os
import sys
import datetime

def create_note():
    if len(sys.argv) < 3:
        print("[NOTE] Usage: python3 scripts/quick_note.py <filename> <content>")
        return
        
    filename = sys.argv[1]
    if not filename.endswith(".md"):
        filename += ".md"
        
    content = sys.argv[2]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    vault_path = os.path.expanduser("~/storage/shared/Axiom")
    target_path = os.path.join(vault_path, filename)
    
    note_data = f"# Note: {filename}\nCreated: {timestamp}\n\n{content}\n"
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(note_data)
        
    print(f"[NOTE] Successfully created and stored -> {filename}")

if __name__ == "__main__":
    create_note()
