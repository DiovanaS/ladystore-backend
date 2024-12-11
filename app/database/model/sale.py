from sqlalchemy import Column, String, DateTime
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
    product = Column(String(100), nullable=False)
    client = Column(String(100), nullable=False)
    sale_date = Column(DateTime, nullable=False)
    sale_state = Column(String(50), nullable=False)
    observation = Column(String(200), nullable=True)

    financial_rels: Mapped[List['FinancialSale']] = relationship(
        back_populates='sale',
        cascade='all, delete'
    )

    customer_stock_rels: Mapped[List['SaleCustomerStock']] = relationship(
        back_populates='sale',
        cascade='all, delete'
    )

    @classmethod
    def __query_all(cls, filters: List = None) -> Sales:
        return cls._query_all(
            filters=filters,
            ordinances=[
                cls.sale_date,
                cls.sale_state,
                cls.product,
                cls.client
            ]
        )

    @classmethod
    def find_all(cls) -> Sales:
        return cls.__query_all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Sale':
        return cls._query_first(filters=[cls.id == id])


from .financial_sale import FinancialSale
from .sale_customer_stock import SaleCustomerStock
