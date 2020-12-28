from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={ r'/*': {'origins': "*"}}, supports_credentials=True)
app.config['aes_key'] = 'F6CBE7F43612B9BE'

from routes.login import *
from routes.users import *


if __name__ == '__main__':
    app.run(debug=True)
