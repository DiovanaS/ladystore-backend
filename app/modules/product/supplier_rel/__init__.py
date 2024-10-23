from flask import Blueprint


supplier_rel = Blueprint('supplier_rel', __name__, url_prefix='/supplier-rel')


from .controller import *
