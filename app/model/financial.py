from flask_restx.fields import Integer, String, Float, DateTime
from app.extension import api
from typing import TypedDict

class FinancialModel(TypedDict):
    id: int
    operation_date: str
    operation_type: str
    value: float
    description: str
    sale_id: int  

financial_model = api.model('Financial', FinancialModel(
    id=Integer(title='ID', readonly=True),
    operation_date=DateTime(
        title='Operation Date',
        required=True
    ),
    operation_type=String(
        title='Operation Type',
        required=True,
        min_length=1,
        max_length=50
    ),
    value=Float(
        title='Value',
        required=True
    ),
    description=String(
        title='Description',
        required=False,
        max_length=200
    ),
    sale_id=Integer(
        title='Sale ID',
        required=True
    )
))
