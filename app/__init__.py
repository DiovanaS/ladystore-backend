from flask import Flask
from .config import configure_enviroment, configure_extensions

app = Flask(__name__)
configure_enviroment(app)
configure_extensions(app)
