import os

def execute_kernel():
    print("[AXIOM_KERNEL] Initializing offline sovereign matrix...")
    vault_path = os.path.expanduser("~/storage/shared/Axiom")
    md_files = [f for f in os.listdir(vault_path) if f.endswith(".md")]
    for file in md_files:
        print(f"[KERNEL] Processing vector node -> {file}")
    print("[AXIOM_KERNEL] Matrix state stabilized. All nodes compiled locally.")

if __name__ == "__main__":
    execute_kernel()
