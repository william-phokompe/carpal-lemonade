from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/greet')
def hello_world():
    return 'Hello from Server'