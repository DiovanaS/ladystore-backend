from flask import Flask

from .config import configure_enviroment, configure_extensions
from .modules.customer import customer
from .modules.error import error


app = Flask(__name__)
configure_enviroment(app)
configure_extensions(app)
app.register_blueprint(customer)
app.register_blueprint(error)
