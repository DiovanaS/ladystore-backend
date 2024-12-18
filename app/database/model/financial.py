from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extension import database
from ..inheritable import Model, TimestampMixin

Financials = List['Financial']


class Financial(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    operation_date = Column(String(50), nullable=False)
    operation_type = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(200), nullable=True)

    sale_id: Mapped[int] = mapped_column(ForeignKey('sale.id'), nullable=False)
    sale: Mapped['Sale'] = relationship('Sale', back_populates='financials')


    @classmethod
    def __query_all(cls, filters: List = None) -> Financials:
        return cls._query_all(
            filters=filters,
            ordinances=[cls.operation_date, cls.amount]
        )

    @classmethod
    def find_all(cls):
        return cls._query_all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Financial':
        return cls._query_first(filters=[cls.id == id])


from .financial_sale import FinancialSale
