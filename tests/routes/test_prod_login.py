import pytest
from utils.web import HTTPcore
from controller.json_web_token.json_web_token import Jwt
import json

class TestProdLoginApi:

    def test_successful_token_validation(self,prod_endpoint, valid_token):
        core = HTTPcore(prod_endpoint)
        core.core("GET",headers={"Authorization": valid_token})
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
    
    def test_get_current_user_info(self,prod_endpoint, valid_token):
        web = HTTPcore(prod_endpoint)
        web.core("GET", headers={"Authorization": valid_token})
        assert web.get_status_code == 200
        assert web.json_response["first_name"] == "john"
        assert web.json_response["last_name"] == "smith"



    
