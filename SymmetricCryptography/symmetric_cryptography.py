from secrets import token_bytes
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def symmetric_encryption(key, iv, msg):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    output = encryptor.update(msg) + encryptor.finalize()
    return output

def symmetric_decryption(key, iv, encrypted_msg_arr):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    output = decryptor.update(encrypted_msg_arr) + decryptor.finalize()
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

    decrypted_msg_arr = []
    with open(sys.argv[2], 'rb') as input_file:
        while message := input_file.read(16):
            output = symmetric_decryption(key,iv,message)
            decrypted_msg_arr.append(output)
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_msg_arr[-1] = unpadder.update(decrypted_msg_arr[-1]) + unpadder.finalize()
    decrypted_msg = b''.join(decrypted_msg_arr).decode("utf-8")

    print("Encrypted message: ", encrypted_msg)
    print("\nDecrypted message: ", decrypted_msg)

if __name__ == "__main__":
    main()
