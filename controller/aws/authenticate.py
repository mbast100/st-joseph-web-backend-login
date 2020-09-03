import boto3
from boto3.dynamodb.conditions import Key


def authenticate(email, password):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    list = response['Items']
    if len(list) == 0:
        return {"message": 'Email not found.', "status_code": 401}
    elif list[0].get("password") == password:
        return {"message": 'Authentication successful', "status_code": 200}
    else:
        return {"message": 'Incorrect password.', "status_code": 401}


def get_first_name(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    list = response['Items']
    if len(list) != 0:
        return list[0].get("first_name")


def get_last_name(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    list = response['Items']
    if len(list) != 0:
        return list[0].get("last_name")


def get_role(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=(Key('email').eq(email))
    )
    list = response['Items']
    if len(list) != 0:
        return list[0].get("role")
