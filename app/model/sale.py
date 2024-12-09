from flask_restx.fields import Integer, String, DateTime
from app.extension import api

class SaleModel:
    id: int
    product: str
    client: str
    sale_date: str
    sale_state: str
    observation: str

sale_model = api.model('Sale', SaleModel(
    id=Integer(title='ID', readonly=True),
    product=String(
        title='Product',
        required=True,
        min_length=1,
        max_length=100
    ),
    client=String(
        title='Client',
        required=True,
        min_length=1,
        max_length=100
    ),
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
    )
))
