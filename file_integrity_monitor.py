





import hashlib

def calculate_file_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


print("===== FILE INTEGRITY MONITOR =====")

filename = "important_file.txt"

# Create a sample file
with open(filename, "w") as file:
    file.write("Original confidential information.")

# Calculate original hash
original_hash = calculate_file_hash(filename)

print("\nOriginal file hash:")
print(original_hash)

# Check the file before modification
current_hash = calculate_file_hash(filename)

if original_hash == current_hash:
    print("\nStatus: File is unchanged.")

# Simulate an unauthorised modification
with open(filename, "a") as file:
    file.write(" Modified content.")

# Calculate new hash
new_hash = calculate_file_hash(filename)

print("\nNew file hash:")
print(new_hash)

# Compare hashes
print("\n===== SECURITY REPORT =====")

if original_hash == new_hash:
    print("Status: File integrity maintained.")
else:
    print("ALERT: File modification detected!")

print("\nMonitoring completed.")


