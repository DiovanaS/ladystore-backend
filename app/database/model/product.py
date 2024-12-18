from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Products = List['Product']


class Product(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(80), nullable=False)
    brand = Column(String(80), nullable=False)
    model = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    size = Column(String(20), nullable=False)
    color = Column(String(40), nullable=False)
    price = Column(Float(), nullable=False)

    stocks: Mapped[List['Stock']] = relationship('Stock', back_populates='product')

    supplier_id: Mapped[int] = mapped_column(ForeignKey('supplier.id'), nullable=False)

    supplier: Mapped['Supplier'] = relationship('Supplier', back_populates='products')

    @classmethod
    def find_all_by(cls, **values) -> Products:
        return cls._query_all(
            icontains=values,
            ordinances=[
                cls.name,
                cls.brand,
                cls.model,
                cls.type,
                cls.size,
                cls.color,
                cls.price
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Product':
        return cls._query_first(filters=[cls.id == id])

