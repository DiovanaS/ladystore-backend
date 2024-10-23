from typing import Dict

from app.database import Supplier, Suppliers

from .exception import SupplierAlreadyExists, SupplierNotFound
from .schema import supplier_schema


def create(data: Dict[str, object]) -> Supplier:
    supplier = supplier_schema.load(data)
    already_exists = Supplier.find_first_by_cnpj(
        supplier.cnpj
    )
    if already_exists: raise SupplierAlreadyExists()
    Supplier.save(supplier)
    return supplier


def find_all() -> Suppliers:
    return Supplier.find_all()


def find_all_by_company_name_or_trading_name(
    name: str
) -> Suppliers:
    return Supplier.find_all_by_company_name_or_trading_name(
        name
    )


def find_first_by_id(id: str) -> Supplier:
    supplier = Supplier.find_first_by_id(id)
    if not supplier: raise SupplierNotFound()
    return supplier


def update(id: int, data: Dict[str, object]) -> Supplier:
    supplier = supplier_schema.load(
        data,
        instance=find_first_by_id(id),
        partial=True
    )
    existing_supplier = Supplier.find_first_by_cnpj(
        supplier.cnpj
    )
    already_exists = existing_supplier and existing_supplier.id != id
    if already_exists: raise SupplierAlreadyExists()
    Supplier.save(supplier)
    return supplier


def delete(id: int) -> None:
    Supplier.delete(find_first_by_id(id))
