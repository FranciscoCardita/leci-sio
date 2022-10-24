import argparse
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def main(args):
    key_size = int(args["key_size"])

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )
    with open("keys/private_key.key", 'wb') as output_file:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        output_file.write(pem)
      
    public_key = private_key.public_key()
    with open("keys/public_key.pem", 'wb') as output_file:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        output_file.write(pem)

if __name__ == "__main__":
    key_values = [1024, 2048, 3072, 4096]
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key_size", required=True, help=f"Supported key values: {key_values}")
    args = vars(parser.parse_args())
    main(args)