# Caesar Cipher Program
# Cybersecurity Internship Task 1

def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')

            position = ord(char) - ascii_offset
            new_position = (position + shift) % 26
            new_char = chr(new_position + ascii_offset)

            encrypted_message += new_char
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(message, shift):
    decrypted_message = ""

    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')

            position = ord(char) - ascii_offset
            new_position = (position - shift) % 26
            new_char = chr(new_position + ascii_offset)

            decrypted_message += new_char
        else:
            decrypted_message += char

    return decrypted_message


# 🔥 THIS PART RUNS ONLY WHEN YOU RUN THIS FILE DIRECTLY
if __name__ == "__main__":

    print("===== Caesar Cipher Tool =====")

    while True:

        print("\n1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))

            result = encrypt(message, shift)
            print("Encrypted message:", result)

        elif choice == "2":
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))

            result = decrypt(message, shift)
            print("Decrypted message:", result)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")