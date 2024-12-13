from os import environ
from . import path


SECRET_KEY = environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/lady_store'

SQLALCHEMY_TRACK_MODIFICATIONS = False

ALLOWED_HOSTS = [*environ.get('ALLOWED_HOSTS', 'localhost').split(' '), 'http://localhost:5173']

JSON_SORT_KEYS = False
