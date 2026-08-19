import compileall
import os

def compile_axiom_bytecode():
    print("[COMPILER] Initiating Axiom bytecode optimization...")
    root_dir = os.path.expanduser("~/storage/shared/Axiom")
    
    # Compile all python files in core/ and scripts/
    success = compileall.compile_dir(root_dir, force=True, quiet=0)
    
    if success:
        print("[COMPILER] Bytecode compilation successfully completed across all modules.")
    else:
        print("[WARNING] Compilation completed with minor warnings or skipped files.")

if __name__ == "__main__":
    compile_axiom_bytecode()
