import argparse
from email import message
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def main(args):

    msg = args["file_name"]
    public_key = args["public_key"]
    output = args["output"]
        
    with open(public_key, 'rb') as input_file:
        pub_key = serialization.load_pem_public_key(
            input_file.read(),
        )
    
    key_size = (pub_key.key_size + 7) // 8
    ciphertext = []
    with open(msg, 'rb') as input_file:
        while message := input_file.read(key_size - 66):
            ciphertext.append(pub_key.encrypt(
                message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                ))
            )

    with open(output, 'wb') as output_file:
        for c in ciphertext:
            output_file.write(c)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_name", required=True, help="<file_name>.txt")
    parser.add_argument("-pk", "--public_key", required=True, help="<file_name>.pem")
    parser.add_argument("-o", "--output", default="rsa_encrypted.txt", help="<output_name>.txt")
    args = vars(parser.parse_args())
    main(args)