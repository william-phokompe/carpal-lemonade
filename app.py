from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/greet')
def hello_world():
    return 'Hello from Server'

# Add variables to calls
@app.route('/user/<username>')
def get_user(username):
    return 'Username: %s' % username