from flask_restx.fields import Integer, String
from typing import TypedDict


_POSTAL_CODE_REGEX = r'^\d{5}-\d{3}$'
''' 00000-000 '''


class AddressModel(TypedDict):
    postal_code: str
    state: str
    city: str
    neighborhood: str
    street: str
    number: int
    complement: str


address_model = AddressModel(
    postal_code=String(
        title='Postal code',
        required=True,
        pattern=_POSTAL_CODE_REGEX
    ),
    state=String(
        title='State',
        required=True,
        min_length=2,
        max_length=2
    ),
    city=String(
        title='City',
        required=True,
        min_length=1,
        max_length=40
    ),
    neighborhood=String(
        title='Neighborhood',
        required=True,
        min_length=1,
        max_length=40
    ),
    street=String(
        title='Street',
        required=True,
        min_length=1,
        max_length=80
    ),
    number=Integer(
        title='Number',
        required=True,
        min=0
    ),
    complement=String(
        title='Complement',
        required=True,
        max_length=40
    )
)
