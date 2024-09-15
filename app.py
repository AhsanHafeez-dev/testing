from flask import request,jsonify,Flask,Response
app=Flask(__name__)

@app.route("/")
def home():
    return "hello testing home"

@app.route("/test")
def test():
    return "test subroutine"