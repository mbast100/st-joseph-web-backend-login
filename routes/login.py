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
<<<<<<< Updated upstream
- if not successful return status code 401
=======
- if not succseful return status code 401
{
email:,
passwor:""
}
>>>>>>> Stashed changes
"""


@app.route('/api/login', methods=['POST'])
def login_api():
    if request.method == 'POST':
        data = request.get_json()
        try:
            response = authenticate(
                data['email'],
                data['password']
            )
            if response['status_code'] == 200:
                jwt = Jwt()
                email = data['email']
                return jsonify({
                    'message': response['message'],
                    'token': jwt.encode_token(get_first_name(email), get_last_name(email), email, get_role(email)),
                    "firstName":get_first_name(email),
                    "lastName":get_first_name(email)
                }), response['status_code']
            elif response['status_code'] == 404:
                return jsonify({'message': response['message']}), 404
            elif response['status_code'] == 400:
                return jsonify({'message': response['message']}), 400
            elif response['status_code'] == 401:
                return jsonify({'message': response['message']}), 401
        except ApiException as e:
            return jsonify({'message': str(e)}), 401


@app.route('/api/test/login', methods=['GET'])
def test_login():
    return jsonify({'message': 'Login API is up and running.'}), 200
