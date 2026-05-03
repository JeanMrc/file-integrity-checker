# File Integrity Checker

A cybersecurity tool that monitors files using SHA-256 hashing
and instantly detects unauthorized modifications, deletions, 
additions and renames.

---

## Features
- Real time monitoring using Watchdog observer
- Detects four types of security events:
  - [MODIFIED] - file content changed
  - [DELETED]  - file removed
  - [NEW FILE] - unauthorized file added
  - [RENAMED]  - file identity changed (obfuscation detection)
- SHA-256 cryptographic hashing for tamper detection
- Persistent hash database in JSON format
- Full audit trail logged with timestamps
- Instant detection — no polling delay

---

## Built With
- Python 3.13
- Hashlib - SHA-256 hashing
- Watchdog - real time file monitoring
- JSON - hash database storage
- Logging - audit trail

---

## How to Run
1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt
3. Create a monitored folder
4. Add files you want to protect
5. Run:
   python integrity_checker.py

---

## Security Events Explained

| Event | Description | Security Relevance |
|-------|-------------|-------------------|
| MODIFIED | File content changed | Detect tampering |
| DELETED | File removed | Detect evidence wiping |
| NEW FILE | Unknown file added | Detect malware drops |
| RENAMED | File identity changed | Detect obfuscation |

---

## Technical Challenge Solved
Basic file monitors treat a rename as a delete followed by an add,
losing the file history. This tool captures renames specifically
using Watchdog's on_moved event, preserving the file's hash history
and detecting obfuscation tactics where attackers rename malicious
files to appear innocent.

---

## Real World Use Cases
- Detect unauthorized file modifications
- Monitor configuration files for changes
- Audit trail for compliance requirements
- Intrusion detection on critical systems
- SOC analyst tooling

---

## Known Limitations
- Requires manual restart if monitored folder is deleted
- Does not monitor subfolders (recursive=False)
