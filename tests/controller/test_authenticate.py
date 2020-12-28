from controller.password_encryption import PasswordEncryption

class TestAuthenticate():


    # def test_encryption(self,test_user, aes_key):
    #     res = encrypt_password(test_user["password"], aes_key)
    #     temp = b'b\xbe6a\x88\xb1Yu;\xfe\xdbB\x0f\\\xfb\x80\x0e\x11\x078\x81\x8fTc\xc6B'
    #     print("\nresult: ",res)
    #     assert res == temp

    def test_decrypt(self,test_user, aes_key):
        temp = PasswordEncryption(aes_key)
        encrypted_pass = temp.encrypt(test_user["password"])
        print(str(encrypted_pass, 'utf-8'))
        print(encrypted_pass)
        passwrod = temp.decrypt(str(encrypted_pass, 'utf-8'))
        print("passsword: ",passwrod)
        assert passwrod == test_user["password"]
    # def test_authentication_200(self,test_user, aes_key):
    #     resp = authenticate(test_user["email"], test_user["password"], aes_key)
    #     assert resp["status_code"] == 200


