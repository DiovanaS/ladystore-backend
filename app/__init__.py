from flask import Flask

from .config import configure_enviroment, configure_extensions
from .modules.customer.controller import customer
from .modules.error import error
from .modules.product import product
from .modules.supplier import supplier


app = Flask(__name__)
configure_enviroment(app)
configure_extensions(app)
app.register_blueprint(customer)
app.register_blueprint(error)
app.register_blueprint(product)
app.register_blueprint(supplier)
