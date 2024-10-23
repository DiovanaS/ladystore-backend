from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extensions import database

from ..inheritable import Model


ProductSuppliers = List['ProductSupplier']


class ProductSupplier(database.Model, Model):
    product_id: Mapped[int] = mapped_column(
        ForeignKey('product.id'),
        nullable=False,
        primary_key=True
    )
    supplier_id: Mapped[int] = mapped_column(
        ForeignKey('supplier.id'),
        nullable=False,
        primary_key=True
    )

    product: Mapped['Product'] = relationship(
        back_populates='supplier_rels'
    )
    supplier: Mapped['Supplier'] = relationship(
        back_populates='product_rels'
    )

    @classmethod
    def __query_all(cls, filters: List = None) -> ProductSuppliers:
        return cls._query_all(
            filters=filters,
            ordinances=[cls.created_at]
        )

    @classmethod
    def find_all_by_product_id(cls, product_id: int) -> ProductSuppliers:
        return cls.__query_all(
            filters=[cls.product_id == product_id]
        )

    @classmethod
    def find_first_by_ids(
        cls,
        product_id: int,
        supplier_id: int
    ) -> 'ProductSupplier':
        return cls._query_first(
            filters=[
                cls.product_id == product_id,
                cls.supplier_id == supplier_id
            ]
        )

    def __init__(self, product_id: int, supplier_id: int) -> None:
        self.product_id = product_id
        self.supplier_id = supplier_id


from .supplier import Supplier
from .product import Product
