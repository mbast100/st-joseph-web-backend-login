from controller.aws.authenticate import *


def test_authenticate_success():
    email = 'mbast.amin97@gmail.com'
    password = 'Marc1997'
    payload = authenticate(email, password)
    response = {"message": 'Authentication successful', "status_code": 200}
    assert payload == response


def test_authenticate_incorrect_password():
    email = 'mbast.amin97@gmail.com'
    password = 'WrongPassword'
    payload = authenticate(email, password)
    response = {"message": 'Incorrect password.', "status_code": 404}
    assert payload == response


def test_authenticate_email_not_found():
    email = 'email@not_found.ca'
    password = 'test123'
    payload = authenticate(email, password)
    response = {"message": 'Email not found.', "status_code": 404}
    assert payload == response


def test_get_first_name():
    email = 'mbast.amin97@gmail.com'
    first_name = get_first_name(email)
    assert first_name == 'Mark'


def test_get_last_name():
    email = 'mbast.amin97@gmail.com'
    last_name = get_last_name(email)
    assert last_name == 'Bastawros'


def test_get_role():
    email = 'mbast.amin97@gmail.com'
    role = get_role(email)
    assert role == 'admin'
