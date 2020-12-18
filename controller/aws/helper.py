import uuid
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def generate_id():
    id = uuid.uuid4()
    return id


def generate_aes_key():
    key = get_random_bytes(16)
    return key


def encrypt_password(password):
    aes_key = generate_aes_key()
    aes = AES.new(aes_key, AES.MODE_CBC)
    sixteen_byte_password = bytes(password, 'utf-16')
    encrypted_password = aes.encrypt(sixteen_byte_password)
    return encrypted_password


def decrypt_password(password):
    aes_key = generate_aes_key()
    aes = AES.new(aes_key, AES.MODE_CBC)
    return aes.decrypt(password)


# this line is just to test the encryption
print(encrypt_password("shahirshahir"))
