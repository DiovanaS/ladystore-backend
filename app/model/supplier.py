from flask_restx.fields import Integer, String
from app.extension import api
from .address import AddressModel, address_model


_CNPJ_REGEX = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
''' 00.000.000/0000-00 '''

_PHONE_REGEX = r'^\(\d{2}\) \d{5}-\d{4}$'
''' (00) 00000-0000 '''


class SupplierModel(AddressModel):
    id: int
    company_name: str
    trading_name: str
    cnpj: str
    phone: str


supplier_model = api.model('Supplier', SupplierModel(
    id=Integer(title='ID', readonly=True),
    company_name=String(
        title='Company name',
        required=True,
        min_length=1,
        max_length=80
    ),
    trading_name=String(
        title='Trading name',
        required=True,
        min_length=1,
        max_length=80
    ),
    cnpj=String(
        title='CNPJ',
        required=True,
        pattern=_CNPJ_REGEX
    ),
    phone=String(
        title='Phone',
        required=True,
        min_length=1,
        max_length=15,
        pattern=_PHONE_REGEX
    ),
    **address_model
))
