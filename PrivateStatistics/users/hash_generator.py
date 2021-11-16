import hashlib


class HashGenerator:

    @staticmethod
    def generate_sha256_hash(plaintext):
        try:
            encoded = plaintext.encode()
            result = hashlib.sha256(encoded)
            return result.hexdigest()
        except AttributeError:
            return ""
