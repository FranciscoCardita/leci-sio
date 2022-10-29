import argparse
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def main(private_key):

    with open("keys/private_key.key", 'r') as input_file:
        ciphertext = input_file.read()

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(plaintext)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-pk", "private_key", required=True, help="<file_name>.key")
    private_key = vars(parser.parse_args())["private_key"]
    main(private_key)