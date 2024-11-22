import subprocess
import time
import os


class InvalidDirectoryException(Exception):
    pass


expected_path = "anavation"
print(os.getcwd())
if expected_path not in os.getcwd():
    raise InvalidDirectoryException(
        f"This script must be run from a directory containing '{expected_path}'")

def run_script():
    python_files = [
        'extract_html.py',
        'extract_links.py',
        'analyze_links.py',
        "similarity_to_resume.py",
    ]

    for file in python_files:
        process = subprocess.Popen(["python", file])
        process.wait()
        time.sleep(5)

run_script()
