import os, hashlib, json, time
from pathlib import Path

VAULT_DIR = Path.home() / "Axiom"
PROOFS_DIR = VAULT_DIR / ".axiom" / "proofs"
REPORTS_DIR = VAULT_DIR / ".axiom" / "reports"
PROOFS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

manifest = {}
hasher = hashlib.sha256()
for root, dirs, files in os.walk(VAULT_DIR):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for file in files:
        p = Path(root) / file
        if "scripts" in p.parts: continue
        with open(p, "rb") as f:
            b = f.read()
            h = hashlib.sha256(b).hexdigest()
            manifest[str(p.relative_to(VAULT_DIR))] = h
            hasher.update(h.encode())

timestamp = time.time()
state_root = hasher.hexdigest()
proof = {"timestamp": timestamp, "state_root": state_root, "manifest": manifest}

# Save JSON Proof
json_path = PROOFS_DIR / f"proof_{int(timestamp)}.json"
with open(json_path, "w") as f:
    json.dump(proof, f, indent=4)

# Generate Standalone HTML Report for General Users
html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Axiom Integrity Report</title>
    <style>
        body {{ font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }}
        .card {{ background: #1e293b; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
        h1 {{ color: #38bdf8; }}
        .hash {{ font-family: monospace; background: #0f172a; padding: 10px; border-radius: 4px; display: inline-block; }}
        table {{ width: 100%; margin-top: 20px; border-collapse: collapse; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #334155; }}
        th {{ color: #38bdf8; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Axiom System Security & Integrity Audit</h1>
        <p><strong>Timestamp:</strong> {time.ctime(timestamp)}</p>
        <p><strong>State Root Hash:</strong></p>
        <div class="hash">{state_root}</div>
        <h2>Tracked Files Manifest</h2>
        <table>
            <tr><th>File Path</th><th>SHA-256 Checksum</th></tr>
"""

for fpath, fhash in manifest.items():
    html_content += f"<tr><td>{fpath}</td><td style='font-family:monospace;'>{fhash}</td></tr>"

html_content += """
        </table>
    </div>
</body>
</html>
"""

html_path = REPORTS_DIR / f"report_{int(timestamp)}.html"
with open(html_path, "w") as f:
    f.write(html_content)

print(f"[+] Proof Generated. State Root: {state_root}")
print(f"[+] HTML Report Compiled: file://{html_path}")
