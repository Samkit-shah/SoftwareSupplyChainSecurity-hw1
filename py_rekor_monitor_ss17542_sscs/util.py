import logging
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# extracts and returns public key from a given cert (in pem format)
def extract_public_key(cert):
    # read the certificate
    #    with open("cert.pem", "rb") as cert_file:
    #        cert_data = cert_file.read()

    try:
        # load the certificate
        certificate = x509.load_pem_x509_certificate(cert, default_backend())

        # extract the public key
        public_key = certificate.public_key()

        # save the public key to a PEM file
        #    with open("cert_public.pem", "wb") as pub_key_file:
        #        pub_key_file.write(public_key.public_bytes(
        #            encoding=serialization.Encoding.PEM,
        #            format=serialization.PublicFormat.SubjectPublicKeyInfo
        #        ))
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        return pem_public_key
    except Exception as e:  # pylint: disable=broad-exception-caught
        print("Exception in extracting public key:", e)
        logger.error("Exception in extracting public key: %s", e)
        return None


def verify_artifact_signature(signature, public_key, artifact_filename):
    # load the public key
    # with open("cert_public.pem", "rb") as pub_key_file:
    #    public_key = load_pem_public_key(pub_key_file.read())

    # load the signature
    #    with open("hello.sig", "rb") as sig_file:
    #        signature = sig_file.read()

    public_key = load_pem_public_key(public_key)
    # load the data to be verified
    with open(artifact_filename, "rb") as data_file:
        data = data_file.read()

    # verify the signature
    try:
        public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature as e:
        print("Signature is invalid")
        logger.error("Signature is invalid for artifact: %s : %s", artifact_filename, e)
        return None
    except Exception as e:  # pylint: disable=broad-exception-caught
        print("Exception in verifying artifact signature:", e)
        logger.error("Exception in verifying artifact signature: %s", e)
        return None
