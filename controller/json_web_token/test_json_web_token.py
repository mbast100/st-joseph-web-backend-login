from jwt import ExpiredSignatureError
import pytest
from controller.json_web_token.json_web_token import Jwt
import datetime
import jwt


def test_encode_token():
    jwt = Jwt()
    first_name = 'john'
    last_name = 'smith'
    email = 'john@smith.com'
    role = 'admin'
    response = jwt.encode_token(first_name, last_name, email, role)
    assert type(response) == str


def test_decode_token():
    jwt = Jwt()
    first_name = 'john'
    last_name = 'smith'
    email = 'john@smith.com'
    role = 'admin'
    response = jwt.encode_token(first_name, last_name, email, role)
    payload = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'role': role
    }
    decode_payload = jwt.decode_token(response)
    assert payload == decode_payload


def test_get_first_name():
    jwt = Jwt()
    first_name = 'john'
    last_name = 'smith'
    email = 'john@smith.com'
    role = 'admin'
    response = jwt.encode_token(first_name, last_name, email, role)
    get_first_name = jwt.get_first_name(response)
    assert first_name == get_first_name


def test_get_last_name():
    jwt = Jwt()
    first_name = 'john'
    last_name = 'smith'
    email = 'john@smith.com'
    role = 'admin'
    response = jwt.encode_token(first_name, last_name, email, role)
    get_last_name = jwt.get_last_name(response)
    assert last_name == get_last_name


def test_get_email():
    jwt = Jwt()
    first_name = 'john'
    last_name = 'smith'
    email = 'john@smith.com'
    role = 'admin'
    response = jwt.encode_token(first_name, last_name, email, role)
    get_email = jwt.get_email(response)
    assert email == get_email


def test_get_role():
    jwt = Jwt()
    first_name = 'john'
    last_name = 'smith'
    email = 'john@smith.com'
    role = 'admin'
    response = jwt.encode_token(first_name, last_name, email, role)
    get_role = jwt.get_role(response)
    assert role == get_role


def test_is_jwt_expired():
    first_name = 'john'
    last_name = 'smith'
    email = 'john@smith.com'
    role = 'admin'
    current_date = datetime.datetime.now()
    payload = {
        'iat': current_date,
        'exp': current_date - datetime.timedelta(seconds=30),
        'sub': {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'role': role
        }
    }
    token = jwt.encode(payload, 'secret_key', algorithm='HS256').decode('UTF-8')
    with pytest.raises(ExpiredSignatureError):
        assert jwt.decode(token, 'secret_key')
