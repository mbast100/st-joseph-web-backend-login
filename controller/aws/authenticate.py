import boto3
from boto3.dynamodb.conditions import Key
from controller.password_encryption import PasswordEncryption
import os
from flask import current_app
from api_exceptions import ApiException

def authenticate(email, password, key="", user=''):
    """
    Validates email and password provided with the ones from the DB
    Assumes that each user is only in the DB once
    :param email: user's email (string)
    :param password: user's password (string)
    :return: response payload containing message and HTTP code
    """
    if current_app.testing:
        user = [user]
    else:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        response = table.query(
            KeyConditionExpression=(Key('email').eq(email))
        )
        try:
            user = response['Items']
        except KeyError:
            return ''

    password_enc = PasswordEncryption(key)
    decrypted_password = ''
    try:
        decrypted_password = password_enc.decrypt(user[0].get("password"))
    except ValueError:
        raise ApiException(message='Invalid password length. This password encryption isnt correct', status_code= 401)

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
