from secrets import token_bytes
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def symmetric_encryption(key, iv, msg):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    output = encryptor.update(msg) + encryptor.finalize()
    return output

def symmetric_decryption(key, iv, encrypted_msg):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    output = decryptor.update(encrypted_msg) + decryptor.finalize()
    return output

def main():
    key = token_bytes(32)
    iv = token_bytes(16)

    if len(sys.argv) < 3:
        print("Usage: symmetric_encryption.py <input_file> <output_file>")
        sys.exit(1)

    encrypted_msg = []
    with open(sys.argv[1], "rb") as input_file:
        while message := input_file.read(16):
            if len(message) < 16:
                padder = padding.PKCS7(128).padder()
                padded_data = padder.update(message)
                padded_data += padder.finalize()
        output = symmetric_encryption(key, iv, message)