from flask import Flask
import os
from flask_bootstrap import Bootstrap


class SingletonApp:

    __INSTANCE = Flask(__name__)

    @staticmethod
    def get_instance():
        return SingletonApp.__INSTANCE

    @staticmethod
    def gen_servlet_secret_key():
        key = os.urandom(32)
        SingletonApp.__INSTANCE.config['SECRET_KEY'] = key

    @staticmethod
    def do_bootstrap():
        Bootstrap(SingletonApp.__INSTANCE)

    @staticmethod
    def update_jinja_env(function):
        SingletonApp.__INSTANCE.jinja_env.globals.update(get_labels=function)