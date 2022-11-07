import certificate as c
import sys
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python read_cert.py <cert1>.pem <cert2>.pem ...")
        sys.exit(1)

    certs = {}
    for cert_file in sys.argv[1:]:
        cert = c.load_cert(cert_file)
        certs[cert.subject] = cert

    print(certs)

if __name__ == '__main__':
    main()