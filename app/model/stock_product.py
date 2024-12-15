from flask_restx.fields import Integer, Nested
from typing import TypedDict
from app.extension import api
from .stock import StockModel, stock_model
from .product import ProductModel, product_model


class StockProductModel(TypedDict):
    stock_id: int
    stock: StockModel
    product_id: int
    product: ProductModel


stock_product_model = api.model('StockProduct', StockProductModel(
    stock_id=Integer(title='Stock ID', required=True),
    stock=Nested(
        stock_model,
        title='Stock',
        readonly=True
    ),
    product_id=Integer(title='Product ID', required=True),
    product=Nested(
        product_model,
        title='Product',
        readonly=True
    )
))
