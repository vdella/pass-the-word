from flask import Flask
import os
from flask_bootstrap import Bootstrap
import database


class SingletonApp:

    __INSTANCE = Flask(__name__)

    @staticmethod
    def get_instance():
        return SingletonApp.__INSTANCE

    @staticmethod
    def gen_servlet_secret_key() -> ():
        """Generates random key to allow Flask's web app secure execution. Needed
        in order to not raise exceptions."""
        key = os.urandom(32)
        SingletonApp.__INSTANCE.config['SECRET_KEY'] = key

    @staticmethod
    def do_bootstrap() -> ():
        """Loads all .css standard Bootstrap's templates for app instance."""
        Bootstrap(SingletonApp.__INSTANCE)

    @staticmethod
    def set_get_labels_jinja_env() -> ():
        """Maps labels dictionaries to jinja2's .HTML script named as 'get_labels', as
        this allows 'get_labels' to be called inside the .HTML script just like a native Jinja2 function."""
        SingletonApp.__INSTANCE.jinja_env.globals.update(get_labels=database.retrieve_labels)
