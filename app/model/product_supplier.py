from flask_restx.fields import Integer, Nested
from typing import NotRequired, TypedDict

from app.extension import api

from .product import ProductModel, product_model
from .supplier import SupplierModel, supplier_model


class ProductSupplierModel(TypedDict):
    product_id: int
    product: NotRequired[ProductModel]
    supplier_id: int
    supplier: NotRequired[SupplierModel]


product_supplier_model = api.model('ProductSupplier', ProductSupplierModel(
    product_id=Integer(title='Product ID', required=True),
    product=Nested(
        product_model,
        title='Product',
        readonly=True
    ),
    supplier_id=Integer(title='Supplier ID', required=True),
    supplier=Nested(
        supplier_model,
        title='Supplier',
        readonly=True
    )
))
