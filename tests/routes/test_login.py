import json


class TestLogin():

    def test_succsseful_login(self, test_user_2_input, client):
        resp = client.post('/api/login', json=test_user_2_input)
        assert resp.status_code == 200
        assert "token" in resp.json

    def test_unsuccsseful_login_wrong_password(self, test_user_2, test_user_2_input, client):
        invalid_user_input = {
            "email": test_user_2_input["email"], "password": "random"}
        resp = client.post('/api/login', json=invalid_user_input)
        assert resp.status_code == 401
        assert "token" not in resp.json

    def test_unsuccsseful_login_wrong_email(self, test_user_2, test_user_2_input, client):
        invalid_user_input = {
            "email": "ranadom@gmail.com", "password": test_user_2_input["password"]}
        resp = client.post('/api/login', json=invalid_user_input)
        assert resp.status_code == 404
        assert "token" not in resp.json

    def test_token_validation(self, test_user_2, test_user_2_input, client):

        resp = client.post('/api/login', json=test_user_2_input)
        assert resp.status_code == 200

        token = resp.json.get("token")
        resp = client.put('/api/login', headers={"Authorization": token})
        assert resp.status_code == 200

    def test_token_fialed_validation(self, test_user_2, test_user_2_input, client):

        token = "rnaodwnfkjdw09234"
        resp = client.put('/api/login', headers={"Authorization": token})
        assert resp.status_code == 401
