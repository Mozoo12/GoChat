from flask import Flask, request

app = Flask(__name__)

@app.route("/app")
def index():
    return "Success"
    
app.run("0.0.0.0",8080)
