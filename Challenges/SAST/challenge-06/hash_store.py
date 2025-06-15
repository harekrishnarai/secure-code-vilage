import hashlib


def store_password(pw):
    digest = hashlib.sha1(pw.encode()).hexdigest()
    return digest
