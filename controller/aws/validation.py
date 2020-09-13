import re


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex, email):
        return {"message": 'Invalid email format', "status_code": 400}


def validate_name(name):
    name = name.replace(' ', '')
    if not name.isalpha():
        return {"message": 'Invalid name format', "status_code": 400}
