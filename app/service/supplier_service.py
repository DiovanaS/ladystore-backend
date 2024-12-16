from app.database import Supplier, Suppliers
from app.exception import SupplierAlreadyExists, SupplierNotFound
from app.model import SupplierModel


def create(data: SupplierModel) -> Supplier:
    already_exists = Supplier.find_first_by_cnpj(
        data['cnpj']
    )
    if already_exists: raise SupplierAlreadyExists()
    supplier = Supplier(**data)
    Supplier.save(supplier)
    return supplier


def find_all_by(**values) -> Suppliers:
    return Supplier.find_all_by(**values)


def find_first_by_id(id: int) -> Supplier:
    supplier = Supplier.find_first_by_id(id)
    if not supplier: raise SupplierNotFound()
    return supplier


def update(id: int, data: SupplierModel) -> Supplier:
    supplier = find_first_by_id(id)
    existing_supplier = Supplier.find_first_by_cnpj(
        data['cnpj']
    )
    already_exists = existing_supplier and existing_supplier.id != id
    if already_exists: raise SupplierAlreadyExists()
    supplier.update(**data)
    Supplier.save(supplier)
    return supplier


def delete(id: int) -> None:
    supplier = find_first_by_id(id)
    Supplier.delete(supplier)
