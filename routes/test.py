from app import app
from flask import jsonify, request


@app.route('/', methods=["GET"])
def test():
    return jsonify({"message":"login api is up and running"})