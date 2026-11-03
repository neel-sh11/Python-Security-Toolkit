


import hashlib

def calculate_hash(text):

    sha256 = hashlib.sha256()

    sha256.update(text.encode("utf-8"))

    return sha256.hexdigest()


print("===== SHA-256 HASH GENERATOR =====")

data = input("Enter text to generate hash: ")

if data.strip() == "":
    print("Error: Input cannot be empty.")

else:
    result = calculate_hash(data)

    print("\nOriginal Text:", data)
    print("SHA-256 Hash:")
    print(result)

    print("\nHash generated successfully!")
