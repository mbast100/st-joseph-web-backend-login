import uuid
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def generate_id():
    id = uuid.uuid4()
    return id
