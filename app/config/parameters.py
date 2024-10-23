from os import environ
from . import paths


SECRET_KEY = environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = f'sqlite:///{paths.DATABASE_FILE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(' ')

JSON_SORT_KEYS = False
