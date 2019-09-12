from flask import Flask, request

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

@app.route('/post/<int:post_id>')
def get_post_id(post_id):
    return 'Post: %s' % str(post_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_user()
    elif request.method == 'GET':
        serve_login()