from flask_restx.fields import Integer, String
from app.extension import api
from typing import TypedDict


class StockModel(TypedDict):
    id: int
    name: str
    unit: int
    quantity: int
    complement: str


stock_model = api.model('Stock', StockModel(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=40
    ),
    unit=Integer(
        title='Unit of Measurement',
        required=True
    ),
    quantity=Integer(
        title='Quantity in Stock',
        required=True
    ),
    complement=String(
        title='Complementary Information',
        required=False,
        max_length=40
    )
))
