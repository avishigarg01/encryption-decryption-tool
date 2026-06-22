# main.py
# This is the main file that runs the whole program.
# It shows a simple menu and lets the user encrypt or decrypt
# text or files, using either the Caesar Cipher or the Fernet method.

import os

# bring in the two methods we made in the other files
import caesar_cipher
import fernet_cipher


# This asks the user which method they want to use.
# It keeps asking until they type 1 or 2.
def ask_method():
    print("Choose a method:")
    print("  1. Caesar Cipher (simple, just for learning)")
    print("  2. Fernet (strong, secure encryption)")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return "caesar"
        elif choice == "2":
            return "fernet"
        else:
            print("Please type 1 or 2.")


# This asks the user for the Caesar key (a number).
# It keeps asking until they type a proper number.
def ask_caesar_key():
    while True:
        value = input("Enter the shift key (a number, e.g. 3): ")
        if value.lstrip("-").isdigit():   # allow negative numbers too
            return int(value)
        else:
            print("That is not a number, please try again.")


# ---------- the four main actions ----------

def do_encrypt_text():
    text = input("Enter the text you want to encrypt: ")
    method = ask_method()

    if method == "caesar":
        key = ask_caesar_key()
        result = caesar_cipher.encrypt_text(text, key)
        print("\nEncrypted text:", result)

    else:  # fernet
        # make a fresh key and save it so it can be used to decrypt later
        key = fernet_cipher.generate_key()
        result = fernet_cipher.encrypt_text(text, key)
        print("\nEncrypted text:", result)
        print("Keep your 'secret.key' file safe - you need it to decrypt!")


def do_decrypt_text():
    method = ask_method()

    if method == "caesar":
        text = input("Enter the text you want to decrypt: ")
        key = ask_caesar_key()
        result = caesar_cipher.decrypt_text(text, key)
        print("\nDecrypted text:", result)

    else:  # fernet
        # fernet text is bytes, so the user pastes it and we turn it into bytes
        text = input("Enter the encrypted text you want to decrypt: ")
        try:
            key = fernet_cipher.load_key()  # read the saved secret.key
            result = fernet_cipher.decrypt_text(text.encode(), key)
            print("\nDecrypted text:", result)
        except FileNotFoundError:
            print("No 'secret.key' file found. You need the key to decrypt.")
        except Exception:
            print("Could not decrypt. The key or the text may be wrong.")


def do_encrypt_file():
    input_file = input("Enter the name of the file to encrypt: ")
    output_file = input("Enter a name for the encrypted file: ")
    method = ask_method()

    if method == "caesar":
        key = ask_caesar_key()
        caesar_cipher.encrypt_file(input_file, output_file, key)
    else:  # fernet
        key = fernet_cipher.generate_key()
        fernet_cipher.encrypt_file(input_file, output_file, key)
        print("Keep your 'secret.key' file safe - you need it to decrypt!")


def do_decrypt_file():
    input_file = input("Enter the name of the file to decrypt: ")
    output_file = input("Enter a name for the decrypted file: ")
    method = ask_method()

    if method == "caesar":
        key = ask_caesar_key()
        caesar_cipher.decrypt_file(input_file, output_file, key)
    else:  # fernet
        try:
            key = fernet_cipher.load_key()
            fernet_cipher.decrypt_file(input_file, output_file, key)
        except FileNotFoundError:
            print("No 'secret.key' file found. You need the key to decrypt.")


# ---------- the main menu ----------

def main():
    print("====================================")
    print("  File Encryption / Decryption Tool")
    print("====================================")

    while True:
        print("\nWhat would you like to do?")
        print("  1. Encrypt text")
        print("  2. Decrypt text")
        print("  3. Encrypt a file")
        print("  4. Decrypt a file")
        print("  5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            do_encrypt_text()
        elif choice == "2":
            do_decrypt_text()
        elif choice == "3":
            do_encrypt_file()
        elif choice == "4":
            do_decrypt_file()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 5.")


# this runs the program when we start this file
if __name__ == "__main__":
    main()
