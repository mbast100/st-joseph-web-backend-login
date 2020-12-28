import pytest
import os
from flask import current_app
from app import app

@pytest.fixture(autouse=True, scope="session")
def setup_cleanup():
    print("\nSetting up tests.")
    ctx = app.app_context()
    ctx.push()
    with ctx:
        current_app.config['TESTING'] =  True
        current_app.config['ENV'] =  'testing'
        assert current_app.testing
    yield
    ctx.pop()
    print("\nTearing down tests")

@pytest.fixture(scope='session')
def prod_endpoint():
    return "https://xb54882p49.execute-api.us-east-1.amazonaws.com/prod/api/login"


@pytest.fixture(scope="session")
def aes_key():
    return app.config['aes_key']


@pytest.fixture(scope='session')
def test_user():
    return {
        "email": "test@test.com",
        "first_name": "test",
        "last_name": "test",
        "password": "Kp74MF8t77yh1cd3I70qnjQbkt3/9e78YkCngLqU0Lo=",
        "role": "test",
    }

@pytest.fixture(scope='session')
def test_user_input():
    return {
        "email": "test@test.com",
        "password": "stjosephtest",
    }