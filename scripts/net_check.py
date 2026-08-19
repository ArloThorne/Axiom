import urllib.request
import sys

def check_connectivity():
    print("[NET] Probing external connectivity to GitHub...")
    try:
        urllib.request.urlopen("https://github.com", timeout=5)
        print("[NET] Connection established. Remote telemetry link is ONLINE.")
    except Exception as e:
        print(f"[NET] Connection failed: {e}. Operating in OFFLINE mode.")

if __name__ == "__main__":
    check_connectivity()
