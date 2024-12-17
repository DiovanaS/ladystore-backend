from flask_restx.fields import Integer, String, Float, Nested
from typing import TypedDict
from app.extension import api
from .product import ProductModel, product_model


class StockModel(TypedDict):
    id: int
    name: str
    unit: str
    quantity: float
    code: str
    complement: str
    product_id: int
    product: ProductModel


stock_model = api.model('Stock', StockModel(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Stock Name',
        required=True,
        min_length=1,
        max_length=100
    ),
    unit=String(
        title='Unit',
        required=True,
        min_length=1,
        max_length=20
    ),
    quantity=Float(
        title='Quantity',
        required=True
    ),
    code=String(
        title='Code',
        required=True,
        min_length=1,
        max_length=50
    ),
    complement=String(
        title='Complement',
        required=False,
        max_length=200
    ),
    product_id=Integer(title='Product ID', required=True),
    product=Nested(
        product_model,
        title='Product',
        readonly=True
    ),
))
