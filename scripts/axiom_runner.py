import os
import sys

def run_task():
    print("[AXIOM] Initializing universal task execution engine...")
    if len(sys.argv) > 1:
        task_name = sys.argv[1]
        print(f"[AXIOM] Executing registered target vector: {task_name}")
    else:
        print("[AXIOM] Core operational state: READY. Pass target module as argument.")

if __name__ == "__main__":
    run_task()
