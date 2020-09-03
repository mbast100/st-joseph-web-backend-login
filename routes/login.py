from app import app
from flask import jsonify, request
from controller.json_web_token.json_web_token import *
from controller.aws.authenticate import *
from api_exceptions import ApiException

"""
login API
- authenticate user with email and password
- if successful authentication (login) return 200 status code with a JWT token, 
    - JWT token must contain : [first_name,last_name, email]
- if not successful return status code 401
"""


@app.route('/api/login', methods=['GET'])
def login():
    if request.method == 'GET':
        data = request.get_json()
        try:
            response = authenticate(
                data['email'],
                data['password']
            )
            if response['status_code'] == 201:
                jwt = Jwt()
                email = data['email']
                return jsonify({
                    'message': response['message'],
                    'token': jwt.encode_token(get_first_name(email), get_last_name(email), email, get_role(email))
                    }), response['status_code']
        except ApiException as e:
            return jsonify({'message': str(e)}), 401
