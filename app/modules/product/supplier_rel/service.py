from typing import Dict

from app.database import ProductSupplier, ProductSuppliers
from app.modules.product import service as product_service
from app.modules.supplier import service as supplier_service

from .exception import SupplierRelNotFound, SupplierRelAlreadyExists
from .schema import supplier_rel_schema


def create(
    data: Dict[str, object]
) -> ProductSupplier:
    supplier_rel = supplier_rel_schema.load(data)
    supplier_service.find_first_by_id(supplier_rel.supplier_id)
    product_service.find_first_by_id(supplier_rel.product_id)
    already_exists = ProductSupplier.find_first_by_ids(
        supplier_rel.product_id,
        supplier_rel.supplier_id
    )
    if already_exists: raise SupplierRelAlreadyExists()
    ProductSupplier.save(supplier_rel)
    return supplier_rel


def find_all_by_product_id(
    product_id: str
) -> ProductSuppliers:
    return ProductSupplier.find_all_by_product_id(product_id)


def find_first_by_ids(
    product_id: str,
    supplier_id: str
) -> ProductSupplier:
    supplier_rel = ProductSupplier.find_first_by_ids(
        product_id,
        supplier_id
    )
    if not supplier_rel: raise SupplierRelNotFound()
    return supplier_rel


def delete(
    product_id: str,
    supplier_id: str
) -> None:
    ProductSupplier.delete(
        find_first_by_ids(product_id, supplier_id)
    )
