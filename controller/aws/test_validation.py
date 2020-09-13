from controller.aws.validation import *


def test_validate_email_success():
    email = "test.test@test.com"
    response = validate_email(email)
    assert response is None


def test_validate_invalid_email():
    email = "test@te@st@test@com"
    response = validate_email(email)
    assert response['status_code'] == 400


def test_validate_name_success():
    name = "Test Test"
    response = validate_name(name)
    assert response is None

def test_validate_invalid_name():
    name = "Test 123"
    response = validate_name(name)
    assert response['status_code'] == 400