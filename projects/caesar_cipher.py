

def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isupper():
            position = ord(char) - ord("A")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("A"))

        elif char.islower():
            position = ord(char) - ord("a")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("a"))

        else:
            result += char

    return result


print("===== CAESAR CIPHER TOOL =====")

message = input("Enter your message: ")

try:
    shift = int(input("Enter shift value (1-25): "))

    if not 1 <= shift <= 25:
        print("Error: Shift must be between 1 and 25.")

    else:
        print("\n1. Encrypt")
        print("2. Decrypt")

        choice = input("Choose an option: ")

        if choice == "1":
            result = caesar_cipher(message, shift, "encrypt")
            print("\nEncrypted Message:", result)

        elif choice == "2":
            result = caesar_cipher(message, shift, "decrypt")
            print("\nDecrypted Message:", result)

        else:
            print("Invalid choice.")

except ValueError:
    print("Error: Enter a valid number.")

print("\nOperation completed.")
