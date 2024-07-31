from cryptography.fernet import Fernet
import os

def decrypt_file(file_path, key):
    # Open the file to read encrypted data
    file = open(file_path, "rb")
    data = file.read()
    file.close()

    # Create a cipher object and decrypt the data
    cipher = Fernet(key)
    decrypted = cipher.decrypt(data)

    # Open the file to write the decrypted data
    file = open(file_path, "wb")
    file.write(decrypted)
    file.close()

def main():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Prompt user for encryption key
    key = input("Enter the encryption key: ").encode()

    # Iterate over files in the directory
    for fname in os.listdir(dir_path):
        path = os.path.join(dir_path, fname)

        # Skip Python script files
        if fname.endswith(".py"):
            continue

        # Decrypt the file and print status
        decrypt_file(path, key)
        print(f"Decrypted: {fname}")

if __name__ == "__main__":
    main()
