from cryptography.fernet import Fernet
import sys

def generate_key(password):
    return Fernet.generate_key()

def encrypt_file(filename, key):
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

if len(sys.argv) != 2:
    print("Usage: python encrypt.py <file>")
    sys.exit(1)

key = Fernet.generate_key()
print("Save this key:", key.decode())

encrypt_file(sys.argv[1], key)
print("File encrypted successfully")
