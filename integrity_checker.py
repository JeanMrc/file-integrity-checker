import os
import hashlib
import json
import time
import logging
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ─────────────────────────────────────────
# Config
# ─────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
WATCH_DIR = os.path.join(BASE_DIR, "monitored")
HASH_DB   = os.path.join(BASE_DIR, "hashes.json")
LOG_FILE  = os.path.join(BASE_DIR, "integrity.log")

# ─────────────────────────────────────────
# Logging
# ─────────────────────────────────────────
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ─────────────────────────────────────────
# Hash File
# ─────────────────────────────────────────
def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# ─────────────────────────────────────────
# Build Hash Database
# ─────────────────────────────────────────
def build_database():
    hashes = {}
    for root, dirs, files in os.walk(WATCH_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            hashes[filepath] = hash_file(filepath)
            print(f"Hashed: {filename}")

    with open(HASH_DB, "w") as f:
        json.dump(hashes, f, indent=4)

    print(f"Database built - {len(hashes)} files hashed.")
    logging.info(f"Database built - {len(hashes)} files hashed.")
    return hashes

# ─────────────────────────────────────────
# Load Database
# ─────────────────────────────────────────
def load_database():
    if not os.path.exists(HASH_DB):
        print("No database found - building new one...")
        return build_database()

    with open(HASH_DB, "r") as f:
        hashes = json.load(f)

    print(f"Database loaded - {len(hashes)} files tracked.")
    return hashes

# ─────────────────────────────────────────
# Integrity Event Handler
# ─────────────────────────────────────────
class IntegrityHandler(FileSystemEventHandler):
    def __init__(self, known_hashes):
        self.known_hashes = known_hashes

    def on_modified(self, event):
        if not event.is_directory:
            filepath     = event.src_path
            filename     = os.path.basename(filepath)
            current_hash = hash_file(filepath)
            known_hash   = self.known_hashes.get(filepath)

            if known_hash and current_hash != known_hash:
                msg = f"[MODIFIED] {filename}"
                print(msg)
                logging.warning(msg)
                self.known_hashes[filepath] = current_hash

    def on_deleted(self, event):
        if not event.is_directory:
            filename = os.path.basename(eve
