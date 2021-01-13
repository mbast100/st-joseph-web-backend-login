from controller.password_encryption import PasswordEncryption


class TestPasswordEncryption():

    def test_decrypt(self, test_user_input, aes_key):
        temp = PasswordEncryption(aes_key)
        encrypted_pass = temp.encrypt(test_user_input["password"])
        print(encrypted_pass)
        passwrod = temp.decrypt(encrypted_pass)

        assert passwrod == test_user_input["password"]

    def test_failed_decryption(self, aes_key):
        temp = PasswordEncryption(aes_key)
        random_encryption = 'zPFy93LMikTD2vCUepbqJsDuA6SzZfqaBM71UED9oyo='
        passwrod = temp.decrypt(random_encryption)
        assert not passwrod

    def test_encrypt_password(self, aes_key):
        temp = PasswordEncryption(aes_key)
        print("\nENC PASSWORD: ", temp.encrypt("stjosephtest"),"\n")
