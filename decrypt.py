from cryptography.fernet import Fernet
import os

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Prompt the user for the key
    key = input("Enter the encryption key: ").encode()

    # Decrypt files in the directory
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)

        # Exclude script files
        if file_name.endswith(".py"):
            continue

        decrypt_file(file_path, key)
        print(f"File decrypted: {file_name}")

if __name__ == "__main__":
    main()
