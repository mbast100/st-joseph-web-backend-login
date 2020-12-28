import pytest

@pytest.fixture(scope='session')
def prod_endpoint():
    return "https://xb54882p49.execute-api.us-east-1.amazonaws.com/prod/api/login"


@pytest.fixture(scope="session")
def aes_key():
    return 'F6CBE7F43612B9BE'


@pytest.fixture(scope='session')
def test_user():
    return {
        "email": "test@test.com",
        "first_name": "test",
        "last_name": "test",
        "password": "stjosephtest",
        "role": "test",
    }