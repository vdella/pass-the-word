from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import DataRequired


class FrontpageForm(FlaskForm):
    """
    Shown just as the execution begins. Gives user only 2 choices:
        * Sign up;
        * or Sign in.
    :warning for comparisons, one must use self.choice.data, NOT self.choice.choices.
    """
    choice = RadioField('Choose an option', choices=[(0, 'Sign up'), (1, 'Sign in')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    """Will be used as sign up and as sign form. Programmatically,
    will have the same functionalities, as they need only to
    get user inputs. We must user session's dictionary to
    check if the intended use is the one of a sign up or
    sign in (will differ as we will need a database read or write.
    """
    username = StringField('Username', validators=[DataRequired()])
    userkey = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
