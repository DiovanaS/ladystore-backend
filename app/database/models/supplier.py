from sqlalchemy import Column, String, or_
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from app.extensions import database

from ..inheritable import AddressMixin, Model


Suppliers = List['Supplier']


class Supplier(database.Model, AddressMixin, Model):
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

    product_rels: Mapped[List['ProductSupplier']] = relationship(
        back_populates='supplier',
        cascade='all, delete'
    )

    @classmethod
    def __query_all(cls, filters: List = None) -> Suppliers:
        return cls._query_all(
            filters=filters,
            ordinances=[
                cls.company_name,
                cls.trading_name,
                cls.cnpj,
                cls.phone
            ]
        )

    @classmethod
    def find_all(cls) -> Suppliers:
        return cls.__query_all()

    @classmethod
    def find_all_by_company_name_or_trading_name(
        cls,
        name: str
    ) -> Suppliers:
        return cls.__query_all(
            filters=[
                or_(
                    cls.company_name.icontains(name),
                    cls.trading_name.icontains(name)
                )
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'Supplier':
        return cls._query_first(filters=[cls.id == id])
    
    @classmethod
    def find_first_by_cnpj(cls, cnpj: str) -> 'Supplier':
        return cls._query_first(filters=[cls.cnpj == cnpj])

    def __init__(
        self,
        name: str,
        brand: str,
        model: str,
        type: str,
        size: str,
        color: str,
        price: float,
        postal_code: str,
        state: str,
        city: str,
        neighborhood: str,
        street: str,
        number: int,
        complement: str = None
    ) -> None:
        self.name = name
        self.brand = brand
        self.model = model
        self.type = type
        self.size = size
        self.color = color
        self.price = price
        self.postal_code = postal_code
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.number = number
        self.complement = complement


from .product_supplier import ProductSupplier
