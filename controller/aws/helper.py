import uuid
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes



def generate_id():
    id = uuid.uuid4()
    return id


def generate_aes_key():
    key = get_random_bytes(16)
    print("KEY : ",key)
    return key


def encrypt_password(password, key=''):
    print("\npassword: ", password)
    aes_key = key or generate_aes_key()
    aes = AES.new(aes_key, AES.MODE_CFB)
    sixteen_byte_password = b'stjosephtest'
    print("\nsixteen_byte_password: ", sixteen_byte_password)
    encrypted_password = aes.encrypt(sixteen_byte_password)
    return encrypted_password


def decrypt_password(encrypted_pass,key=''):
    aes_key = key or generate_aes_key()
    aes = AES.new(aes_key, AES.MODE_CFB)
    #sixteen_byte_password = bytes(password, 'utf-16')
    return aes.decrypt(encrypted_pass)


# this line is just to test the encryption
#print(encrypt_password("shahirshahir"))
