from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key(key_file):
    return open(key_file, "rb").read()

def save_key(key_file, key):
    with open(key_file, "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    key_file = os.path.join(current_directory, "encryption_key.key")

    # Generate or load the key
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key_file, key)
        print("Encryption key generated and saved:", key)
    else:
        key = load_key(key_file)
        print("Encryption key loaded from file:", key)

    # Encrypt files in the directory
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)

        # Exclude script files and the key file
        if file_name.endswith(".py") or file_name == "encryption_key.key":
            continue

        encrypt_file(file_path, key)
        print(f"File encrypted: {file_name}")

if __name__ == "__main__":
    main()
