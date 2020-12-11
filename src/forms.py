from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import DataRequired


class FrontpageForm(FlaskForm):
    """Shown just as the execution begins. Gives user only 2 choices:
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


class UserOperationForm(FlaskForm):
    choice = RadioField('Choose an option', choices=[(0, 'See labels'), (1, 'Create labels')])
    submit = SubmitField('Submit')


class LabelCreationForm(FlaskForm):
    """Works alongside a Generator() object. A user must choose one of 2 options:
    if the wanted password will be easy-to-remember (remarkable) or randomly generated.
    Fields 'text_field' and random_button_choice don't have the DataRequired() attribute,
    as the text field can be left empty and the seed will be generated in a purely random
    way; however, as radio button fields cannot be left empty, a third option was created
    to work with "not wanting to generate remarkable passwords" right now.
    """
    name = StringField('Type a reminder for the key', validators=[DataRequired()])
    choice = RadioField('Choose an option', choices=[(0, 'Remarkable'), (1, 'Random')])
    text_field = StringField('Type a seed if Random was chosen, if you want')
    random_button_choice = RadioField('Choose an option if Remarkable was chosen',
                                      choices=[(0, 'With slash'), (1, 'Without slash'),
                                               (2, 'Did not choose Remarkable')])
    submit = SubmitField('Submit')
