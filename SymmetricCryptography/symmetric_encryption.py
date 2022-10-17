from secrets import token_bytes
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64

def symmetric_encryption(key, iv, msg):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    output = encryptor.update(msg) + encryptor.finalize()
    return output

def main():
    key = token_bytes(32)
    iv = token_bytes(16)

    if len(sys.argv) < 3:
        print("Usage: symmetric_encryption.py <input_file> <output_file>")
        sys.exit(1)

    encrypted_msg_arr = []
    with open(sys.argv[1], "rb") as input_file:
        while message := input_file.read(16):
            if len(message) < 16:
                padder = padding.PKCS7(128).padder()
                message = padder.update(message) + padder.finalize()
            output = symmetric_encryption(key, iv, message)
            encrypted_msg_arr.append(output)
    encrypted_msg = b''.join(encrypted_msg_arr)

    with open(sys.argv[2], "wb") as output_file:
        output_file.write(encrypted_msg)

    with open("key.txt", "w") as key_file:
        key_file.write(base64.b64encode(key).decode("ASCII") + '\n')
        key_file.write(base64.b64encode(iv).decode("ASCII"))

    print("\nEncrypted message: ", encrypted_msg)

if __name__ == "__main__":
    main()