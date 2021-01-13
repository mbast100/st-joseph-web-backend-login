from flask import Flask
from flask_cors import CORS
from controller.aws.ssm import ParameterStore
from flask import current_app

app = Flask(__name__)
cors = CORS(app, resources={ r'/*': {'origins': "*"}}, supports_credentials=True)
store = ParameterStore('/AUTH')

ctx = app.app_context()
ctx.push()
with ctx:
    current_app.config['JWT_SECRET'] = store['JWT_SECRET']
    current_app.config['AES_KEY'] = 'AES_KEY'


from routes.login import *
from routes.users import *


if __name__ == '__main__':
    app.run(debug=True)
