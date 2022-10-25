import argparse
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def main(public_key):
        
    with open(public_key, 'rb') as input_file:
        pub_key = serialization.load_pem_public_key(
            input_file.read(),
        )

    message = b"encrypted data"
    ciphertext = pub_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    with open("rsa_encrypted.txt", 'wb') as output:
        output.write(ciphertext)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-pk", "--public_key", required=True, help="<file_name>.pem")
    public_key = vars(parser.parse_args())["public_key"]
    main(public_key)