from flask_restx.fields import Integer, String, Date
from app.extension import api
from .address import AddressModel, address_model


_CPF_REGEX = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
''' 000.000.000-00 '''

_EMAIL_REGEX = r'^[\w\-.]+@([\w-]+\.)+[\w-]{2,4}$'
''' address@domain.com '''

_PHONE_REGEX = r'^\(\d{2}\) \d{5}-\d{4}$'
''' (00) 00000-0000 '''


class CustomerModel(AddressModel):
    id: int
    name: str
    cpf: str
    birthdate: str
    email: str
    phone: str


customer_model = api.model('Customer', CustomerModel(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=80
    ),
    cpf=String(
        title='CPF',
        required=True,
        pattern=_CPF_REGEX
    ),
    birthdate=Date(title='Birthdate', required=True),
    email=String(
        title='E-mail',
        required=True,
        max_length=80,
        pattern=_EMAIL_REGEX,
        example='address@domain.com'
    ),
    phone=String(
        title='Phone',
        required=True,
        pattern=_PHONE_REGEX
    ),
    **address_model
))
