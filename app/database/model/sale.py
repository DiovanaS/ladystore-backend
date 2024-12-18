from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extension import database
from ..inheritable import Model, TimestampMixin

Sales = List['Sale']


class Sale(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    sale_date = Column(String(50), nullable=False)
    sale_state = Column(String(50), nullable=False)
    observation = Column(String(200), nullable=True)

    financial_rels: Mapped[List['FinancialSale']] = relationship(
        back_populates='sale',
        cascade='all, delete'
    )

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False)
    product: Mapped['Product'] = relationship('Product', back_populates='sales')

    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'), nullable=False)
    customer: Mapped['Customer'] = relationship('Customer', back_populates='sales')

    stock_id: Mapped[int] = mapped_column(ForeignKey('stock.id'), nullable=False)
    stock: Mapped['Stock'] = relationship('Stock', back_populates='sales')

    @classmethod
    def find_all(cls):
        return cls._query_all() 


    @classmethod
    def find_first_by_id(cls, id: int) -> 'Sale':
        return cls._query_first(filters=[cls.id == id])
