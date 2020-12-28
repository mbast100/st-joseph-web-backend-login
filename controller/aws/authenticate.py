import boto3
from boto3.dynamodb.conditions import Key
from controller.aws.helper import *


aes_key = 'F6CBE7F43612B9BE'


def authenticate(email, password, key=""):
    """
    Validates email and password provided with the ones from the DB
    Assumes that each user is only in the DB once
    :param email: user's email (string)
    :param password: user's password (string)
    :return: response payload containing message and HTTP code
    """
    if email == '':
        return {"message": 'Missing email.', "status_code": 400}
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    try:
        user = response['Items']
    except KeyError:
        return ''

    decrypted_password = decrypt_password(user[0].get("password"), key)

    if len(user) == 0:
        return {"message": 'Email not found.', "status_code": 404}
    elif decrypted_password == password:
        return {"message": 'Authentication successful', "status_code": 200}
    else:
        return {"message": 'Authentication failed. Incorrect password.', "status_code": 401}


def get_first_name(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    user = response['Items']
    if len(user) != 0:
        return user[0].get("first_name")


def get_last_name(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    user = response['Items']
    if len(user) != 0:
        return user[0].get("last_name")


def get_role(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    user = response['Items']
    if len(user) != 0:
        return user[0].get("role")
