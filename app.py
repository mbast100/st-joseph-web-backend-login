from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={ r'/*': {'origins': "*"}}, supports_credentials=True)


from routes.login import *


if __name__ == '__main__':
    app.run(debug=True)
