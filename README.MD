# File Integrity Checker

A cybersecurity tool that monitors files using SHA-256 hashing 
and alerts when files are modified, deleted or added.

---

## Features
- Monitors files using SHA-256 cryptographic hashing
- Detects three types of changes:
  - [MODIFIED] - file content changed
  - [DELETED] - file removed
  - [NEW FILE] - unauthorized file added
- Logs all changes with timestamps
- Checks every 10 seconds
- Works on any folder

---

## Built With
- Python 3.13
- Hashlib - SHA-256 hashing
- JSON - hash database storage
- Logging - audit trail

---

## How to Run
1. Clone the repo
2. Create a monitored folder
3. Add files you want to protect
4. Run:
   python integrity_checker.py

---

## Technical Challenge Solved
File integrity monitoring requires detecting the smallest changes 
in any file type. Solved using SHA-256 hashing — reading files in 
8192 byte chunks to handle large files efficiently without memory 
issues. Any single character change produces a completely different 
hash, making tampering impossible to hide.

---

## Real World Use Cases
- Detect unauthorized file modifications
- Monitor configuration files for changes
- Audit trail for compliance requirements
- Intrusion detection on critical systems