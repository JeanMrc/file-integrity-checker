4. Run
```bash
   python integrity_checker.py
```

---

## Security Events Explained

| Event     | Description            | Security Relevance          |
|-----------|------------------------|-----------------------------|
| MODIFIED  | File content changed   | Detect tampering            |
| DELETED   | File removed           | Detect evidence wiping      |
| NEW FILE  | Unknown file added     | Detect malware drops        |
| RENAMED   | File identity changed  | Detect obfuscation          |

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

## Limitations

- Requires the script to keep running for real time monitoring.
  For continuous protection, schedule it as a background service
  using Windows Task Scheduler or a cron job on Linux.
