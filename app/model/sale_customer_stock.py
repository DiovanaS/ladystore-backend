from flask_restx.fields import Integer, Nested
from typing import NotRequired, TypedDict

from app.extension import api
from .sale import SaleModel, sale_model
from .customer import CustomerModel, customer_model
from .stock import StockModel, stock_model

class SaleCustomerStockModel(TypedDict):
    sale_id: int
    sale: NotRequired[SaleModel]
    customer_id: int
    customer: NotRequired[CustomerModel]
    stock_id: int
    stock: NotRequired[StockModel]

sale_customer_stock_model = api.model('SaleCustomerStock', SaleCustomerStockModel(
    sale_id=Integer(
        title='Sale ID',
        required=True
    ),
    sale=Nested(
        sale_model,
        title='Sale',
        readonly=True
    ),
    customer_id=Integer(
        title='Customer ID',
        required=True
    ),
    customer=Nested(
        customer_model,
        title='Customer',
        readonly=True
    ),
    stock_id=Integer(
        title='Stock ID',
        required=True
    ),
    stock=Nested(
        stock_model,
        title='Stock',
        readonly=True
    )
))
