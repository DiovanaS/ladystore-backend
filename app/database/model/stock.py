from datetime import date
from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.model.product import Product
from app.extension import database
from ..inheritable import Model, TimestampMixin

Stocks = List['Stock']

class Stock(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    unit: Mapped[str] = mapped_column(String(50), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    complement: Mapped[str] = mapped_column(String(40), nullable=True)
    
    # Add product_id column as a foreign key referencing the Product model
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False)
    
    # Establish relationship to Product
    product: Mapped['Product'] = relationship('Product', back_populates='stocks')
    
    @classmethod
    def find_all(cls) -> Stocks:
        return cls._query_all(
            ordinances=[cls.name, cls.unit, cls.quantity, cls.complement]
        )

    @classmethod
    def find_all_by_name(cls, name: str) -> Stocks:
        return cls._query_all(
            icontains={'name': name},
            ordinances=[cls.name]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Stock':
        return cls._query_first(filters=[cls.id == id])

    @classmethod
    def find_all_by(cls, **values) -> Stocks:
        return cls._query_all(
            icontains=values,
            ordinances=[cls.name, cls.unit, cls.quantity, cls.code, cls.complement]
        )
