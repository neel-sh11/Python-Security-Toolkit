
import os
import hashlib
import mimetypes
from datetime import datetime

print("===== FILE METADATA INSPECTOR =====")

with open("sample_document.txt", "w") as file:
    file.write("This is a cybersecurity metadata test file.")

filename = "sample_document.txt"

if not os.path.isfile(filename):
    print("\nError: File not found.")
else:
    file_size = os.path.getsize(filename)

    modified_time = os.path.getmtime(filename)
    modified_date = datetime.fromtimestamp(
        modified_time
    ).strftime("%Y-%m-%d %H:%M:%S")

    created_time = os.path.getctime(filename)
    created_date = datetime.fromtimestamp(
        created_time
    ).strftime("%Y-%m-%d %H:%M:%S")

    extension = os.path.splitext(filename)[1]

    file_type, encoding = mimetypes.guess_type(filename)

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    print("\n===== METADATA REPORT =====")
    print("File Name:", os.path.basename(filename))
    print("Extension:", extension if extension else "No extension")
    print("File Size:", file_size, "bytes")
    print("File Type:", file_type or "Unknown")
    print("Created Timestamp:", created_date)
    print("Modified Timestamp:", modified_date)
    print("SHA-256 Hash:", sha256.hexdigest())

    print("\nInspection completed.")

