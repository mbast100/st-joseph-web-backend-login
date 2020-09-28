import pytest
from utils.web import HTTPcore
from controller.json_web_token.json_web_token import Jwt

class TestProdLoginApi:

    def test_succsseful_token_validation(self,prod_endpoint):
        core = HTTPcore(prod_endpoint)
        temp = Jwt()
        token = temp.encode_token('john', 'smith', 'john@smith.com', 'admin')
        core.core("GET",headers={"Authorization": token})
        assert core.get_status_code == 200

    def test_unsuccsseful_token_validation(self,prod_endpoint):
        core = HTTPcore(prod_endpoint)
        core.core("GET",headers={"Authorization": "randomtokennotours12321"})
        assert core.get_status_code == 401