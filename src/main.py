from flask import Flask, render_template, request
from password.generator import Generator

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def gen_password():
    if request.method == 'POST':
        if request.form['password_gen_type'] == 'random':
            return str(Generator.gen_password_base64(request.form.get('phrase')))
        return str(Generator.gen_password_by_dict(request.form.get('trailing')))
    return render_template('hello.html')
