from datetime import date
from sqlalchemy import Column, Integer, Date, String, or_
from typing import List, Union

from app.extension import database

from ..inheritable import AddressMixin, Model, TimestampMixin


Customers = List['Customer']


class Customer(database.Model, Model, AddressMixin, TimestampMixin):
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

    def __init__(self, **data) -> None:
        data['birthdate'] = self.__parse_birthdate(data['birthdate'])
        super().__init__(**data)

    def update(self, **data) -> None:
        data['birthdate'] = self.__parse_birthdate(data['birthdate'])
        super().update(**data)

    def __parse_birthdate(self, birthdate: Union[date, str]) -> str:
        is_date = isinstance(birthdate, date)
        return birthdate if is_date else date.fromisoformat(birthdate)
