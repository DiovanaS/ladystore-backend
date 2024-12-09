from flask_restx.fields import Integer, Nested
from typing import NotRequired, TypedDict

from app.extension import api
from .financial import FinancialModel, financial_model
from .sale import SaleModel, sale_model  

class FinancialSaleModel(TypedDict):
    financial_id: int
    financial: NotRequired[FinancialModel]
    sale_id: int
    sale: NotRequired[SaleModel]

financial_sale_model = api.model('FinancialSale', FinancialSaleModel(
    financial_id=Integer(
        title='Financial ID',
        required=True
    ),
    financial=Nested(
        financial_model,
        title='Financial',
        readonly=True
    ),
    sale_id=Integer(
        title='Sale ID',
        required=True
    ),
    sale=Nested(
        sale_model,
        title='Sale',
        readonly=True
    )
))
