from sqlalchemy import Column, String, or_
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extension import database

from ..inheritable import AddressMixin, Model, TimestampMixin


Suppliers = List['Supplier']


class Supplier(database.Model, Model, AddressMixin, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    company_name = Column(String(80), nullable=False)
    trading_name = Column(String(80), nullable=False)
    cnpj = Column(String(18), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)

    products: Mapped[List['Product']] = relationship('Product', back_populates='supplier')

    @classmethod
    def find_all_by(cls, **values) -> Suppliers:
        return cls._query_all(
            icontains=values,
            ordinances=[
                cls.company_name,
                cls.trading_name,
                cls.cnpj,
                cls.phone
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Supplier':
        return cls._query_first(filters=[cls.id == id])
    
    @classmethod
    def find_first_by_cnpj(cls, cnpj: str) -> 'Supplier':
        return cls._query_first(filters=[cls.cnpj == cnpj])


