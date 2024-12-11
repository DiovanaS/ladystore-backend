from sqlalchemy import Column, String, Float, DateTime
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
    transaction_date = Column(DateTime, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(200), nullable=True)

    sale_rels: Mapped[List['FinancialSale']] = relationship(
        back_populates='financial',
        cascade='all, delete'
    )

    @classmethod
    def __query_all(cls, filters: List = None) -> Financials:
        return cls._query_all(
            filters=filters,
            ordinances=[cls.transaction_date, cls.amount]
        )

    @classmethod
    def find_all(cls) -> Financials:
        return cls.__query_all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Financial':
        return cls._query_first(filters=[cls.id == id])


from .financial_sale import FinancialSale
