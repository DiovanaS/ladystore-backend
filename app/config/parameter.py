from os import environ
from . import path


SECRET_KEY = environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/lady_store'

SQLALCHEMY_TRACK_MODIFICATIONS = False

JSON_SORT_KEYS = False
