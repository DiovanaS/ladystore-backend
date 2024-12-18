from flask_restx.fields import Integer, String, DateTime, Nested
from app.extension import api
from typing import TypedDict
from .product import ProductModel, product_model
from .customer import CustomerModel, customer_model
from .stock import StockModel, stock_model

class SaleModel(TypedDict):
    id: int
    sale_date: str
    sale_state: str
    observation: str
    stock_id: int
    customer_id: int
    product_id: int
    product: ProductModel
    stock: StockModel
    customer: CustomerModel

sale_model = api.model('Sale', SaleModel(
    id=Integer(title='ID', readonly=True),
    sale_date=DateTime(
        title='Sale Date',
        required=True
    ),
    sale_state=String(
        title='Sale State',
        required=True,
        min_length=1,
        max_length=50
    ),
    observation=String(
        title='Observation',
        required=False,
        max_length=200
    ),
    customer_id=Integer(
        title='Customer ID',
        required=True
    ),
    product_id=Integer(
        title='Product ID',
        required=True
    ),
    stock_id=Integer(
        title='Stock ID',
        required=True
    ),
    product=Nested(
        product_model,
        title='Product',
        readonly=True
    ),
    customer=Nested(
        customer_model,
        title='Customer',
        readonly=True
    ),
    stock=Nested(
        stock_model,
        title='Stock',
        readonly=True
    ),
))
