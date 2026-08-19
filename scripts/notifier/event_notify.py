import os
import time

def dispatch_local_alert(message):
    print(f"[LOCAL_ALERT] {time.strftime('%Y-%m-%d %H:%M:%S')} -> {message}")

if __name__ == "__main__":
    dispatch_local_alert("Axiom sovereign notification engine online. Zero telemetry.")
