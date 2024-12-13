from datetime import date
from sqlalchemy import Column, Integer, String
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin

Stocks = List['Stock']

class Stock(database.Model, Model, TimestampMixin):
    id = Column(
        Integer(),
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(40), nullable=False)
    unit = Column(Integer(), nullable=False)
    quantity = Column(Integer(), nullable=False)
    complement = Column(String(40), nullable=True)

    @classmethod
    def __query_all(cls, filters: List = None) -> List['Stock']:
        return cls._query_all(
            filters=filters,
            ordinances=[cls.name, cls.unit, cls.quantity, cls.complement]
        )

    @classmethod
    def find_all(cls) -> List['Stock']:
        return cls.__query_all()

    @classmethod
    def find_all_by_name(cls, name: str) -> List['Stock']:
        return cls.__query_all(
            filters=[cls.name.icontains(name)]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Stock':
        return cls._query_first(filters=[cls.id == id])

    def __init__(self, **data) -> None:
        super().__init__(**data)

    def update(self, **data) -> None:
        super().update(**data)
