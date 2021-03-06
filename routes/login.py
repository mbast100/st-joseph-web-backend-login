from app import app
from flask import jsonify, request
from controller.json_web_token.json_web_token import *
from controller.aws.get_users import *
from controller.aws.authenticate import *
from api_exceptions import ApiException

"""
login API
- authenticate user with email and password
- if successful authentication (login) return 200 status code with a JWT token, 
    - JWT token must contain : [first_name,last_name, email]
- if not successful return status code 401
"""


@app.route('/api/login', methods=['POST', 'PUT', 'GET'])
def login_api():

    if request.method == 'GET':
        token = request.headers.get('authorization')
        jwt = Jwt(token=token)
        if jwt.is_valid:
            return jsonify({
                "first_name": jwt.get_first_name(),
                "last_name": jwt.get_last_name(),
                'message': 'Valid jwt.'
            }), 200
        else:
            return jsonify({"message": "invalid token."}), 401

    if request.method == 'POST':
        data = request.get_json()
        try:
            response = authenticate(
                data['email'],
                data['password'],
                key=app.config['AES_KEY'],
            )
            if response['status_code'] == 200:
                jwt = Jwt()
                email = data['email']
                return jsonify({
                    'message': response['message'],
                    'token': jwt.encode_token(get_first_name(email), get_last_name(email), email, get_role(email)),
                    "firstName": get_first_name(email),
                    "lastName": get_last_name(email)
                }), response['status_code']
            elif response['status_code'] == 404:
                return jsonify({'message': response['message']}), 404
            elif response['status_code'] == 400:
                return jsonify({'message': response['message']}), 400
            elif response['status_code'] == 401:
                return jsonify({'message': response['message']}), 401
        except ApiException as e:
            return jsonify({'message': str(e.message)}), e.status_code

    if request.method == 'PUT':
        jwt_token = Jwt(token=request.headers.get("Authorization"))
        resp= jwt_token.validate_token()
        return jsonify({"message":resp["message"]}), resp["status_code"]




@app.route('/api/test/login', methods=['GET'])
def test_login():
    return jsonify({'message': 'Login API is up and running.'}), 200