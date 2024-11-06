from flask import Flask
from .config import setup_enviroment, setup_extensions


app = Flask(__name__)
setup_enviroment(app)
setup_extensions(app)
