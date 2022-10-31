from getpass import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import sys

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1e5,
    )

    data = kdf.derive(password)
    iv = data[:16]
    key = data[16:]

    print(password, data, iv, key)

def main():
    if len(sys.argv) != 2:
        print("Usage: python keygen.py <input_file>")
        sys.exit(1)

    salt = os.urandom(16)
    password = getpass("Password: ")
    generate_key(password, salt)

if __name__ == '__main__':
    main()