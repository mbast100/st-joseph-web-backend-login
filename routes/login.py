from app import app
from flask import jsonify

"""
login API
- authenticate user with email and password
- if succsseful authentication (login) return 200 status code with a JWT token, 
    - JWT token must contain : [first_name,last_name, email]
- if not succseful return status code 401
"""


@app.route("/api/login", methods=["GET", "POST"])
def login():
    pass