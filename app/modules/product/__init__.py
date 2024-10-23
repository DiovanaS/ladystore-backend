from flask import Blueprint
from .supplier_rel import supplier_rel


product = Blueprint('product', __name__, url_prefix='/product')
product.register_blueprint(supplier_rel)


from .controller import *
