from authlib.integrations.flask_client import OAuth
from flask import Flask, jsonify, url_for

import conf

app = Flask(__name__)
app.secret_key = conf.APP_SECRET_KEY
oauth = OAuth(app)

github = oauth.register(
    name='github',
    client_id=conf.OAUTH_GITHUB_CLIENT_ID,
    client_secret=conf.OAUTH_GITHUB_SECRET,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    #client_kwargs={'scope': 'user:email'},
    client_kwargs={},
)

@app.route('/github_login')
def github_login():
    redirect_uri = url_for('github_authorize', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/github_authorize')
def github_authorize():
    token = github.authorize_access_token()
    profile = github.get('user', token=token).json()
    return jsonify(profile)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'

def file_to_bytes(fn):
    with open(fn, mode='rb') as fin:
        return fin.read()

def file_to_string(fn):
    b = file_to_bytes(fn)
    return b.decode('UTF-8')
