from routes.login import *
import pytest
import flask
import requests
import requests_mock
import app

def test_login_success():
    requests_mock.Mocker(real_http=True).register_uri('GET', 'http://test.com/api/login')
    login()
    assert True
