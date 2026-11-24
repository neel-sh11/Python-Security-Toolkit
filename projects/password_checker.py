

import string

def check_password(password):

    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1

    print("\n===== PASSWORD SECURITY REPORT =====")

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("Password Length:", len(password))
    print("Security Score:", score, "/ 5")
    print("Password Strength:", strength)

    if score <= 2:
        print("Suggestion: Improve your password complexity.")
    elif score == 3:
        print("Suggestion: Add more character variety.")
    else:
        print("Suggestion: Good character diversity!")

    print("====================================")


password = input("Enter a password to check: ")

if password.strip() == "":
    print("Error: Password cannot be empty.")
else:
    check_password(password)

