import os
import binascii
import hashlib


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


def sha1(str_data):
    return hashlib.sha1(str_data.encode()).hexdigest()


def is_type_dict(x):
    return isinstance(x, dict)
