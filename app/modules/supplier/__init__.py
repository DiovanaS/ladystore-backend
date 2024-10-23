from flask import Blueprint


supplier = Blueprint('supplier', __name__, url_prefix='/supplier')


from .controller import *
