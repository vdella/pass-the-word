from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import LoginForm, FrontpageForm, UserOperationForm, LabelCreationForm
import database
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.jinja_env.globals.update(get_labels=database.retrieve_labels)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


signing_up: bool = False
session_user = tuple()


@app.route('/', methods=['POST', 'GET'])
def index():
    global signing_up
    form = FrontpageForm()
    if form.validate_on_submit():
        print(form.choice.data)
        signing_up = True if int(form.choice.data) == 0 else False
        print(signing_up)
        return redirect(url_for('access_db'))
    return render_template('index.html', form=form)


@app.route('/access', methods=['POST', 'GET'])
def access_db():
    form = LoginForm()
    global session_user
    if form.validate_on_submit():
        session_user = database.check_user(form.username.data)
        if not signing_up:
            if session_user is not None:
                flash('Username taken!')
                return redirect(url_for('access_db'))
            else:
                database.create_user(form.username.data, form.userkey.data)
                return redirect(url_for('user_choice'))
        else:
            if session_user is None:
                flash('Cannot find username in database!')
            else:
                return redirect(url_for('user_choice'))
    return render_template('user.html', form=form)


@app.route('/choice', methods=['POST', 'GET'])
def user_choice():
    form = UserOperationForm()
    if form.validate_on_submit():
        if int(form.choice.data) == 0:
            return redirect(url_for('label_view'))
        else:
            return redirect(url_for('label_creation'))
    return render_template('choice.html', form=form)


@app.route('/creation', methods=['POST', 'GET'])
def label_creation():
    form = LabelCreationForm()
    if form.validate_on_submit():
        database.create_label(form.name.data, form.key.data, session_user[0])
        return redirect(url_for('user_choice'))
    return render_template('label_creation.html', form=form)


@app.route('/view', methods=['POST', 'GET'])
def label_view():
    return render_template('label_view.html', session_user_id=session_user[0])
