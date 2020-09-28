import pytest
from controller.json_web_token.json_web_token import Jwt

def test_valid_token():
    jwt = Jwt()
    jwt = Jwt(token=jwt.encode_token('john', 'smith', 'john@smith.com', 'admin'))
    assert jwt.is_valid == True


def test_invalid_token():
    jwt = Jwt(token="randomstringthatisnotvalid")
    assert jwt.is_valid == False