import os
import subprocess
import sys

def bootstrap_environment():
    print("[BOOTSTRAP] Verifying universal runtime dependencies...")
    required_packages = ["requests", "colorama"]
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"[PACKAGE] {package} is already installed.")
        except ImportError:
            print(f"[PACKAGE] Installing missing dependency: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            
    print("[BOOTSTRAP] Environment dependency verification complete.")

if __name__ == "__main__":
    bootstrap_environment()
