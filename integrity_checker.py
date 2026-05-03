import os
import hashlib
import json
import time
import logging
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# -- config -- 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WATCH_DIR = os.path.join(BASE_DIR, "monitored")
HASH_DB = os.path.join(BASE_DIR, "hashes.json")
LOG_FILE = os.path.join(BASE_DIR, "integrity.log")

#-- Logging --
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# -- Hash file -- 
def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

#-- Build Hash Database -- 
def build_database():
    hashes = {}
    for filename in os.listdir(WATCH_DIR):
        filepath = os.path.join(WATCH_DIR, filename)
        if os.path.isfile(filepath):
            hashes[filepath] = hash_file(filepath)
            print(f"Hashed: {filename}")

    with open(HASH_DB, "w") as f:
        json.dump(hashes, f, indent=4)

    print(f"Database built - {len(hashes)}) Files hashed.")
    logging.info(f"Database built - {len(hashes)} Files hashed.")
    return hashes

#-- Load Database --
def load_database():
    if not os.path.exists(HASH_DB):
        print("No Database found - Building new one....")
        return build_database()
    
    with open(HASH_DB, "r") as f:
        hashes = json.load(f)

    print(f"Database loaded - {len(hashes)} Files tracked.")
    return hashes

# -- Check Integrity -- 
def check_integrity(known_hashes):
    changes= []

    for filepath, known_hash in known_hashes.items():
        if not os.path.exists(filepath):
            msg = f"[DELETED] {os.path.basename(filepath)}"
            print(msg)
            logging.warning(msg)
            changes.append(msg)
        else:
            current_hash = hash_file(filepath)
            if current_hash != known_hash:
                msg = f"[MODIFIED] {os.path.basename(filepath)}"
                print(msg)
                logging.warning(msg)
                changes.append(msg)

    for filename in os.listdir(WATCH_DIR):
        filepath = os.path.join(WATCH_DIR, filename)
        if os.path.isfile(filepath) and filepath not in known_hashes:
            msg = f"[NEW FILE] {filename}"
            print(msg)
            logging.warning(msg)
            changes.append(msg)

    if not changes:
        print(f"[OK]All files intact - {datetime.now().strftime('%H"%M:%S')}")
        logging.info("All files intact.")

    return changes


#-- Main -- 
def run_checker():
    print("=" * 50)
    print("File Integrity Checker")
    print(f"Monitoring: {WATCH_DIR}")
    print(f"Started   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    known_hashes = load_database()

    print(f"Watching {len(known_hashes)} files for changes...")
    print("-" * 50)

    while True:
        time.sleep(10)
        check_integrity(known_hashes)


#-- Run -- 
run_checker() 