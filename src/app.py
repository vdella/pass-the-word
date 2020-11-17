from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from password.generator import Generator


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/user/')
def user():
    return render_template('user.html')
