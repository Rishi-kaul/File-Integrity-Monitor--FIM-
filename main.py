import hashlib
import os
import time

BASELINE_FILE = 'baseline.txt'
TARGET_DIR = './Files'

def calculate_file_hash(filepath):
    """Calculates the SHA512 hash of a given file."""
    sha512 = hashlib.sha512()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha512.update(chunk)
    return sha512.hexdigest()

def erase_baseline_if_already_exists():
    """Deletes the baseline file if it already exists."""
    if os.path.exists(BASELINE_FILE):
        os.remove(BASELINE_FILE)

def collect_new_baseline():
    """Collects a new baseline of file hashes and saves it to the baseline file."""
    erase_baseline_if_already_exists()
    
    with open(BASELINE_FILE, 'a') as baseline:
        for root, dirs, files in os.walk(TARGET_DIR):
            for file in files:
                filepath = os.path.join(root, file)
                filehash = calculate_file_hash(filepath)
                baseline.write(f"{filepath}|{filehash}\n")

def begin_monitoring_files_with_saved_baseline():
    """Monitors files for changes against the saved baseline."""
    file_hash_dict = {}

    with open(BASELINE_FILE, 'r') as baseline:
        for line in baseline:
            filepath, filehash = line.strip().split('|')
            file_hash_dict[filepath] = filehash

    while True:
        time.sleep(1)
        
        for root, dirs, files in os.walk(TARGET_DIR):
            for file in files:
                filepath = os.path.join(root, file)
                filehash = calculate_file_hash(filepath)

                if filepath not in file_hash_dict:
                    print(f"{filepath} has been created!")
                else:
                    if file_hash_dict[filepath] == filehash:
                        # The file has not changed
                        pass
                    else:
                        # The file has been compromised!
                        print(f"{filepath} has changed!!!")
        
        for filepath in list(file_hash_dict.keys()):
            if not os.path.exists(filepath):
                print(f"{filepath} has been deleted!")
                del file_hash_dict[filepath]

if __name__ == "__main__":
    print("What would you like to do?")
    print("    A) Collect new Baseline?")
    print("    B) Begin monitoring files with saved Baseline?")
    print("")
    response = input("Please enter 'A' or 'B': ").strip().upper()
    print("")

    if response == 'A':
        collect_new_baseline()
    elif response == 'B':
        begin_monitoring_files_with_saved_baseline()
    else:
        print("Invalid option. Please enter 'A' or 'B'.")
