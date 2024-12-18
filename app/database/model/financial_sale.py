from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extension import database
from ..inheritable import Model, TimestampMixin

FinancialSales = List['FinancialSale']


class FinancialSale(database.Model, Model, TimestampMixin):
    financial_id: Mapped[int] = mapped_column(
        ForeignKey('financial.id'),
        nullable=False,
        primary_key=True
    )
    sale_id: Mapped[int] = mapped_column(
        ForeignKey('sale.id'),
        nullable=False,
        primary_key=True
    )



    @classmethod
    def __query_all(cls, filters: List = None) -> FinancialSales:
        return cls._query_all(
            filters=filters,
            ordinances=[cls.created_at]
        )

    @classmethod
    def find_by_ids(cls, financial_id: int, sale_id: int) -> 'FinancialSale':
        return cls._query_first(
            filters=[
                cls.financial_id == financial_id,
                cls.sale_id == sale_id
            ]
        )


from .financial import Financial
from .sale import Sale
