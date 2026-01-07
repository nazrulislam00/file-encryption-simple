from cryptography.fernet import Fernet
import sys

def decrypt_file(filename, key):
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    decrypted = fernet.decrypt(data)

    with open("decrypted_" + filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)

if len(sys.argv) != 3:
    print("Usage: python decrypt.py <file.enc> <key>")
    sys.exit(1)

decrypt_file(sys.argv[1], sys.argv[2].encode())
print("File decrypted successfully")
