from cryptography.hazmat.primitives import hashes
import sys
import binascii

def calculate(fname):
    digest = hashes.Hash(hashes.SHA256())

    with open(fname, 'rb') as input_file:
        while data := input_file.read(1024*1024):
            digest.update(data)
    
    return digest.finalize()

def main():
    if len(sys.argv) != 2:
        print("Usage: python digest.py <file_name>")
        sys.exit(1)

    for fname in sys.argv[1:]:
        hd = binascii.hexlify(calculate(fname))
        print(f'{hd.decode()}: {fname}')

if __name__ == '__main__':
    main()

