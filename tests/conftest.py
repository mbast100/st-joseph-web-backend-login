import pytest
import os
from flask import current_app
from app import app
from controller.aws.ssm import ParameterStore

@pytest.fixture(scope="session")
def client():
    client = app.test_client()
    return client

@pytest.fixture(autouse=True, scope="session")
def setup_cleanup():
    print("\nSetting up tests.")
    ctx = app.app_context()
    ctx.push()
    with ctx:
        current_app.config['TESTING'] = True
        current_app.config['ENV'] = 'testing'
        assert current_app.testing
    yield
    ctx.pop()
    print("\nTearing down tests")


@pytest.fixture(scope='session')
def prod_endpoint():
    return "https://xb54882p49.execute-api.us-east-1.amazonaws.com/prod/api/login"


@pytest.fixture(scope="session")
def aes_key():
    return app.config['AES_KEY']


@pytest.fixture(scope='session')
def test_user():
    return {
        "email": "test@test.com",
        "first_name": "test",
        "last_name": "test",
        "password": "DnwIVK2TH/GUjBoYo2pyIN4mSvkRK0r3yMH6w+h+2cE=",
        "role": "test",
    }


@pytest.fixture(scope='session')
def test_user_2():
    return {
        "email": "test@test.ca",
        "first_name": "Jhon",
        "last_name": "Doe",
        "password": "kyfKcodTJ5bkZ6uGYI53/2H8WXSZdC/gB7xh+Xtu21w=",
        "role": "test",
        "id": "23ca88b3-84ef-42be-9dd6-efb7426ec500",
    }


@pytest.fixture(scope='session')
def test_user_2_input():
    return {
        "email": "test@test.ca",
        "password": "helloworld",
    }


@pytest.fixture(scope='session')
def test_user_input():
    return {
        "email": "test@test.com",
        "password": "stjosephtest",
    }


@pytest.fixture(scope="session")
def store(scope="session"):
    return ParameterStore(prefix='/TEST')
