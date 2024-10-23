from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr


class AddressMixin():
    @declared_attr
    def postal_code(cls):
        return Column(String(9), nullable=False)

    @declared_attr
    def state(cls):
        return Column(String(2), nullable=False)

    @declared_attr
    def city(cls):
        return Column(String(40), nullable=False)

    @declared_attr
    def neighborhood(cls):
        return Column(String(40), nullable=False)

    @declared_attr
    def street(cls):
        return Column(String(80), nullable=False)

    @declared_attr
    def number(cls):
        return Column(Integer, nullable=False)

    @declared_attr
    def complement(cls):
        return Column(String(40), nullable=True)
