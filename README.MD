# File Integrity Checker

A cybersecurity tool that monitors files using SHA-256 hashing
and instantly detects unauthorized modifications, deletions,
additions and renames.

---

## Features

- Real time monitoring using Watchdog observer
- Recursive subfolder monitoring
- Startup integrity check — catches changes made while offline
- Auto recreates monitored folder if deleted
- Detects four types of security events:
  * [MODIFIED] - file content changed
  * [DELETED] - file removed
  * [NEW FILE] - unauthorized file added
  * [RENAMED] - file identity changed (obfuscation detection)
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
```bash
   git clone https://github.com/JeanMrc/file-integrity-checker
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Create a monitored folder and add files to protect
