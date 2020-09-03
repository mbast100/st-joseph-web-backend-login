from controller.json_web_token.json_web_token import Jwt


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
