import hashlib
import os


def store_password(pw):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, 100000)
    return salt.hex() + ':' + digest.hex()
