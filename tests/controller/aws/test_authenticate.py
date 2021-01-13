from controller.aws.authenticate import authenticate


class TestAuthenticate():

    def test_successful_authentication(self, aes_key, test_user_input):
        resp = authenticate(
            test_user_input['email'], test_user_input['password'], key=aes_key)
        assert resp["status_code"] == 200

    def test_unsuccessful_authentication(self, aes_key, test_user_input):
        resp = authenticate(
            test_user_input['email'], "rnadom", key=aes_key)
        assert resp["status_code"] == 401