import pytest
from utils.web import HTTPcore
from controller.json_web_token.json_web_token import Jwt
import json

class TestProdLoginApi:

    def test_successful_token_validation(self,prod_endpoint):
        core = HTTPcore(prod_endpoint)
        temp = Jwt()
        token = temp.encode_token('john', 'smith', 'john@smith.com', 'admin')
        core.core("GET",headers={"Authorization": token})
        assert core.get_status_code == 200

    def test_unsuccessful_token_validation(self,prod_endpoint):
        core = HTTPcore(prod_endpoint)
        core.core("GET",headers={"Authorization": "randomtokennotours12321"})
        assert core.get_status_code == 401
    
    def test_successful_login(self,prod_endpoint):
        web = HTTPcore(prod_endpoint)
        web.core("POST",data=json.dumps({
            "email": "test@test.com",
            "password": "stjosephtest"
             }))
        print("res: ",web.json_response)
        assert web.get_status_code == 200
        assert web.json_response.get("firstName") == "test"
        assert web.json_response.get("message") == "Authentication successful"

    def test_unsuccessful_login(self,prod_endpoint):
        web = HTTPcore(prod_endpoint)
        web.core("POST",data=json.dumps({
            "email": "test@test.com",
            "password": "random"
             }))
        assert web.get_status_code == 401
    
