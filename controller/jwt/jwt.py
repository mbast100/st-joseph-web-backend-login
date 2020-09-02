import jwt
import datetime


class Jwt:

    secret_key = '63vwlxbVi15X030EVlkPodAieJWI-qoMImXJZW6lg_P3v80oMlqPdDJOuiNSALzelN1AWv2bk28FE4coyZnzU6ZTbUb24bVwqwX9o0ZUWwkfLtRthkLr42rodz0deAHkKNu0LNpW1thKg5kkxiq8n_t6UnKLpam2lM-b92NfmlUbdgOgry1HtLu-GKP5lJBmclTX4yCaKnKSWPW1XKlB49r8sodjiAFGz-Egm8edIBpMkrwjOP_2a34I3l9Fz0m9vwoMY5eg5Vc13QiGyypajrimraPkR-lLcTgSJ4knZd2rP0fkBqpnvDwLD9PygOjLrowy-CjnMnVidtHSWvP_0A'

    def encode_token(self, user_first_name, user_last_name, user_email, user_role):
        """
        Generates JWT, given a valid email, password and role
        :param user_first_name: user's first name (string)
        :param user_last_name: user's last name (string)
        :param user_email: user's email address (string)
        :param user_role: user's role (string)
        :return: jwt (string)
        """
        current_date = datetime.datetime.now()
        try:
            payload = {
                'iat': current_date,
                'exp': current_date + datetime.timedelta(days=60),
                'sub': {
                    'user_first_name': user_first_name,
                    'user_last_name': user_last_name,
                    'user_email': user_email,
                    'user_role': user_role
                }
            }
            return jwt.encode(
                payload,
                self.secret_key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def decode_token(self, jwt_token):
        """
        Decrypts jwt and returns the token's content
        :param jwt_token: generated jwt (string)
        :return: payload containing jwt content (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


    def get_first_name(self, jwt_token):
        """
        Decrypts jwt and returns the user's first name
        :param jwt_token: generated jwt (string)
        :return: user's first name (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']['user_first_name']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def get_last_name(self, jwt_token):
        """
        Decrypts jwt and returns the user's last name
        :param jwt_token: generated jwt (string)
        :return: user's last name (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']['user_last_name']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def get_email(self, jwt_token):
        """
        Decrypts jwt and returns the user's email
        :param jwt_token: generated jwt (string)
        :return: user's email (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']['user_email']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def get_role(self, jwt_token):
        """
        Decrypts jwt and returns the user's role
        :param jwt_token: generated jwt (string)
        :return: user's role (string)
        """
        try:
            payload = jwt.decode(jwt_token, key=self.secret_key)
            return payload['sub']['user_role']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
