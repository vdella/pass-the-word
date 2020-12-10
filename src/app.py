from flask import Flask, render_template, redirect, session, url_for
from flask_bootstrap import Bootstrap
from forms import LoginForm, FrontpageForm
# from flask_sqlalchemy import SQLAlchemy
# import os
# from models import User

app = Flask(__name__)
bootstrap = Bootstrap(app)
# app.config['SECRET_KEY'] = 'Like a movie, you are the main role just like me.'

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database = SQLAlchemy(app)
# database.drop_all()
# database.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    form = FrontpageForm()
    if form.validate_on_submit():
        session['is_signup'] = form.choice.data == 0
        return redirect(url_for('access_db'))
    return render_template('index.html', form=form)


@app.route('/access')
def access_db():
    form = LoginForm()
    # if form.validate_on_submit():
    #
    #     # We need to see if a given user indeed exists inside the database.
    #     def user_exists():
    #         return database.Query(database.exists().where(User.name == form.username)).scalar()
    #
    #     if not session.get('is_signup'):
    #         if user_exists():
    #             flash('Username taken!')
    #             return redirect(url_for('access_db'))
    #         else:
    #             # We must save a digested user password to increase database invasion security.
    #             new_user = User(name=form.username, key=bcrypt.hashpw(form.userkey, bcrypt.gensalt()))
    #             db.session.add(new_user)
    #             db.session.commit()
    #     else:
    #         if not user_exists():
    #             flash('Cannot find username in database!')
    #         else:
    #             return
    return render_template('user.html', form=form)
