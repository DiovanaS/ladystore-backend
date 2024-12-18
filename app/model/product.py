from flask_restx.fields import Float, Integer, String
from typing import TypedDict

from app.extension import api


class ProductModel(TypedDict):
    id: int
    name: str
    brand: str
    model: str
    type: str
    size: str
    color: str
    price: float


product_model = api.model('Product', ProductModel(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=80
    ),
    brand=String(
        title='Brand',
        required=True,
        min_length=1,
        max_length=80
    ),
    model=String(
        title='Model',
        required=True,
        min_length=1,
        max_length=80
    ),
    type=String(
        title='Type',
        required=True,
        min_length=1,
        max_length=20
    ),
    size=String(
        title='Size',
        required=True,
        min_length=1,
        max_length=20
    ),
    color=String(
        title='Color',
        required=True,
        min_length=1,
        max_length=40
    ),
    price=Float(
        title='Price',
        required=True,
        min=0
    ), 
    supplier_id=Integer(
        title='Surpplier ID',
        required=True
    )
))
