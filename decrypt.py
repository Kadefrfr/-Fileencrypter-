from cryptography.fernet import Fernet
import os

def decrypt_file(file_path, key):
    file = open(file_path, "rb")
    data = file.read()
    file.close()

    cipher = Fernet(key)
    decrypted = cipher.decrypt(data)

    file = open(file_path, "wb")
    file.write(decrypted)
    file.close()

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    key = input("Enter the encryption key: ").encode()

    for fname in os.listdir(dir_path):
        path = os.path.join(dir_path, fname)

        if fname.endswith(".py"):
            continue

        decrypt_file(path, key)
        print(f"Decrypted: {fname}")

if __name__ == "__main__":
    main()
