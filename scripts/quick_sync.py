import subprocess
import datetime

def quick_sync():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[SYNC] Staging local alterations at {timestamp}...")
    subprocess.run("git add .", shell=True)
    
    commit_msg = f"chore(sync): automated sovereign checkpoint -> {timestamp}"
    print(f"[SYNC] Committing with message: '{commit_msg}'")
    subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
    
    print("[SYNC] Pushing to sovereign remote repository...")
    subprocess.run("git push", shell=True)
    print("[SYNC] Pipeline synchronized successfully.")

if __name__ == "__main__":
    quick_sync()
