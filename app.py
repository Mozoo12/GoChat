from flask import Flask, request

app = Flask(__name__)

@app.route("/app")
def index():
    return "Success"
