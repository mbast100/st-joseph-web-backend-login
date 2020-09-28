import pytest

@pytest.fixture(scope='session')
def prod_endpoint():
    return "https://xb54882p49.execute-api.us-east-1.amazonaws.com/prod/api/login"