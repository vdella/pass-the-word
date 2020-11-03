from flask import Flask, render_template, request
from password.generator import Generator


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/show', methods=['POST'])
def gen_password():
    # TODO redirect in case none option is chosen
    if 'random' in request.form:
        return Generator.gen_password_base64()
    elif 'dict' in request.form:
        return Generator.gen_password_by_dict(True)
