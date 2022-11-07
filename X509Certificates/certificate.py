from cryptography import x509
from datetime import datetime

def load_cert(pem_file):
    with open(pem_file, 'rb') as f:
        cert = x509.load_pem_x509_certificate(f.read())
    return cert

def cert_validity(cert):
    current_date = datetime.today()
    if (cert.not_valid_before < current_date < cert.not_valid_after):
        return True
    return False