import jwt
import datetime
from api_exceptions import ApiException
from flask import current_app

class Jwt:
    secret_key = current_app.config['JWT_SECRET']

    def __init__(self, token =''):
        self.token = token
        self.expired_token_message = "Token expired"
        self.invalid_token_message = "Invalid token"

    def encode_token(self, first_name, last_name, email, role):
        """
        Generates JWT, given a valid email, password and role
        :param first_name: user's first name (string)
        :param last_name: user's last name (string)
        :param email: user's email address (string)
        :param role: user's role (string)
        :return: json_web_token (bytes)
        """
        current_date = datetime.datetime.now()
        try:
            payload = {
                'iat': current_date,
                'exp': current_date + datetime.timedelta(days=60),
                'sub': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'role': role
                }
            }
            return jwt.encode(
                payload,
                self.secret_key,
                algorithm='HS256'
            ).decode('UTF-8')
        except Exception as e:
            return e

    def decode_token(self, jwt_token):
        """
        Decrypts json_web_token and returns the token's content
        :param jwt_token: generated json_web_token (string)
        :return: payload containing json_web_token content (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return self.expired_token_message
        except jwt.InvalidTokenError:
            return self.invalid_token_message

    def validate_token(self):
        decode = self.decode_token(self.token)
        if decode == self.expired_token_message or decode == self.invalid_token_message:
            return {"message": "failed token validation", "status_code": 401}
        else:
            return {"message": "valid token", "status_code": 200}

    def get_first_name(self):
        """
        Decrypts json_web_token and returns the user's first name
        :param jwt_token: generated json_web_token (string)
        :return: user's first name (string)
        """
        try:
            payload = jwt.decode(self.token, key=self.secret_key)
            return payload['sub']['first_name']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def get_last_name(self):
        """
        Decrypts json_web_token and returns the user's last name
        :param jwt_token: generated json_web_token (string)
        :return: user's last name (string)
        """
        try:
            payload = jwt.decode(self.token, key=self.secret_key)
            return payload['sub']['last_name']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def get_email(self, jwt_token):
        """
        Decrypts json_web_token and returns the user's email
        :param jwt_token: generated json_web_token (string)
        :return: user's email (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']['email']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def get_role(self, jwt_token):
        """
        Decrypts json_web_token and returns the user's role
        :param jwt_token: generated json_web_token (string)
        :return: user's role (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']['role']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def is_jwt_expired(self, jwt_token):
        """
        Decrypts json_web_token and returns boolean
        :param jwt_token: generated json_web_token (string)
        :return: True if jwt is expired (boolean)
        """
        payload = jwt.decode(jwt_token, key=self.secret_key)
        if payload['exp'] < datetime.datetime.now():
            return True
    
    @property
    def is_valid(self):
        resp = self.validate_token()
        if resp.get("status_code") == 200:
            return True
        else:
            return False