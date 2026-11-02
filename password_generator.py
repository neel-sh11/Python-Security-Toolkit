

import secrets
import string

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = []

    # Ensure character variety
    password.append(secrets.choice(string.ascii_uppercase))
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.digits))
    password.append(secrets.choice(string.punctuation))

    # Fill the remaining length
    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    # Shuffle the password securely
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


print("===== SECURE PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Error: Password length must be at least 8.")
    else:
        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)
        print("\nPassword generated successfully.")

except ValueError:
    print("Error: Please enter a valid number.")