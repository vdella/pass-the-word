from flask import render_template, redirect, url_for, flash
from forms import LoginForm, FrontpageForm, UserOperationForm, LabelCreationForm
from src import SingletonApp
import database
from generator import Generator

app = SingletonApp.get_instance()
SingletonApp.gen_servlet_secret_key()
SingletonApp.do_bootstrap()
SingletonApp.update_jinja_env(database.retrieve_labels)

signing_up: bool = False
session_user = tuple()


@app.route('/', methods=['POST', 'GET'])
def index():
    global signing_up
    form = FrontpageForm()
    if form.validate_on_submit():
        signing_up = True if int(form.choice.data) == 0 else False
        return redirect(url_for('access_db'))
    return render_template('index.html', form=form)


@app.route('/access', methods=['POST', 'GET'])
def access_db():
    form = LoginForm()
    global session_user
    if form.validate_on_submit():
        if not signing_up:
            if database.check_user(form.username.data) is not None:
                flash('Username taken!')
                return redirect(url_for('access_db'))
            else:
                database.create_user(form.username.data, form.userkey.data)
                session_user = database.check_user(form.username.data)
                return redirect(url_for('user_choice'))
        else:
            if database.check_user(form.username.data) is None:
                flash('Cannot find username in database!')
            else:
                session_user = database.check_user(form.username.data)
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
    generator = Generator()
    if form.validate_on_submit():
        if int(form.choice.data) == 0:
            database.create_label(form.name.data,
                                  generator.gen_password_by_dict(int(form.random_button_choice.data) == 0),
                                  session_user[0])
        else:
            database.create_label(form.name.data,
                                  str(generator.gen_password_base64(form.text_field.data)),
                                  session_user[0])
        return redirect(url_for('user_choice'))
    return render_template('label_creation.html', form=form)


@app.route('/view', methods=['POST', 'GET'])
def label_view():
    return render_template('label_view.html', session_user_id=session_user[0])
