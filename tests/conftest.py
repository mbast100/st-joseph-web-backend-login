import pytest
from controller.json_web_token.json_web_token import Jwt

@pytest.fixture(scope='session')
def prod_endpoint():
    return "https://xb54882p49.execute-api.us-east-1.amazonaws.com/prod/api/login"

@pytest.fixture(scope='session')
def valid_token():
    temp = Jwt()
    return temp.encode_token('john', 'smith', 'john@smith.com', 'admin')