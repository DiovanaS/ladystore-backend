from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extension import database
from ..inheritable import Model, TimestampMixin

SaleCustomerStocks = List['SaleCustomerStock']


class SaleCustomerStock(database.Model, Model, TimestampMixin):
    sale_id: Mapped[int] = mapped_column(
        ForeignKey('sale.id'),
        nullable=False,
        primary_key=True
    )
    customer_id: Mapped[int] = mapped_column(
        ForeignKey('customer.id'),
        nullable=False,
        primary_key=True
    )
    stock_id: Mapped[int] = mapped_column(
        ForeignKey('stock.id'),
        nullable=False,
        primary_key=True
    )

    sale: Mapped['Sale'] = relationship(
        back_populates='customer_stock_rels'
    )
    customer: Mapped['Customer'] = relationship()
    stock: Mapped['Stock'] = relationship()

    @classmethod
    def __query_all(cls, filters: List = None) -> SaleCustomerStocks:
        return cls._query_all(
            filters=filters,
            ordinances=[cls.created_at]
        )

    @classmethod
    def find_by_ids(cls, sale_id: int, customer_id: int, stock_id: int) -> 'SaleCustomerStock':
        return cls._query_first(
            filters=[
                cls.sale_id == sale_id,
                cls.customer_id == customer_id,
                cls.stock_id == stock_id
            ]
        )


from .sale import Sale
from .customer import Customer
from .stock import Stock
