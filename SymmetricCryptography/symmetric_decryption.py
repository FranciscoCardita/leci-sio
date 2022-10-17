from secrets import token_bytes
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64

def symmetric_decryption(key, iv, encrypted_msg_arr):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    output = decryptor.update(encrypted_msg_arr) + decryptor.finalize()
    return output

def main():
    if len(sys.argv) < 3:
        print("Usage: symmetric_decryption.py <input_file> <output_file>")
        sys.exit(1)

    with open("key.txt", "rb") as key_file:
        key = base64.b64decode(key_file.readline())
        iv = base64.b64decode(key_file.readline())

    decrypted_msg_arr = []
    with open(sys.argv[1], 'rb') as input_file:
        while message := input_file.read(16):
            output = symmetric_decryption(key,iv,message)
            decrypted_msg_arr.append(output)
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_msg_arr[-1] = unpadder.update(decrypted_msg_arr[-1]) + unpadder.finalize()
    decrypted_msg = b''.join(decrypted_msg_arr).decode("utf-8")

    with open(sys.argv[2], "w") as output_file:
        output_file.write(decrypted_msg)

    print("\nDecrypted message: ", decrypted_msg)

if __name__ == "__main__":
    main()