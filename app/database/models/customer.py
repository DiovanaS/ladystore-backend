from datetime import date
from sqlalchemy import Column, Integer, Date, String, or_
from typing import List

from app.extensions import database

from ..inheritable import AddressMixin, Model


Customers = List['Customer']


class Customer(database.Model, AddressMixin, Model):
    id = Column(
        Integer(),
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(80), nullable=False)
    cpf = Column(String(14), unique=True, nullable=True)
    birthdate = Column(Date, nullable=True)
    email = Column(String(80), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)

    @classmethod
    def __query_all(cls, filters: List = None) -> Customers:
        return cls._query_all(
            filters=filters,
            ordinances=[
                cls.name,
                cls.email,
                cls.birthdate,
                cls.cpf,
                cls.phone
            ]
        )

    @classmethod
    def find_all(cls) -> Customers:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> Customers:
        return cls.__query_all(
            filters=[cls.name.icontains(name)]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Customer':
        return cls._query_first(filters=[cls.id == id])

    @classmethod
    def find_first_by_cpf_or_email(
        cls,
        cpf: str,
        email: str
    ) -> 'Customer':
        return cls._query_first(
            filters=[
                or_(
                    cls.cpf == cpf,
                    cls.email == email
                )
            ]
        )

    def __init__(
        self,
        name: str,
        cpf: str,
        birthdate: date,
        email: str,
        phone: str,
        postal_code: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
        complement: str = None
    ) -> None:
        self.name = name
        self.cpf = cpf
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.postal_code = postal_code
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.number = number
        self.complement = complement
