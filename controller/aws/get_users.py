import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')


def get_all_users():
    response = table.scan()
    list = response['Items']
    return list