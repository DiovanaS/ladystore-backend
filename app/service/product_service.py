from app.database import (
    Product, Products,
    ProductSupplier, ProductSuppliers
)
from app.exception import (
    ProductNotFound,
    ProductSupplierAlreadyExists,
    ProductSupplierNotFound,
)
from app.model import ProductModel, ProductSupplierModel
from app.service import supplier_service


def create(data: ProductModel) -> Product:
    product = Product(**data)
    Product.save(product)
    return product


def create_supplier_rel(data: ProductSupplierModel) -> ProductSupplier:
    find_first_by_id(data['product_id'])
    supplier_service.find_first_by_id(data['supplier_id'])
    already_exists = ProductSupplier.find_first_by_ids(
        data['product_id'],
        data['supplier_id']
    )
    if already_exists: raise ProductSupplierAlreadyExists()
    product_supplier = ProductSupplier(**data)
    ProductSupplier.save(product_supplier)
    return product_supplier

def find_all():
    return Product._query_all()

def find_all_by(**values) -> Products:
    return Product.find_all_by(**values)


def find_all_supplier_rels_by_id(id: int) -> ProductSuppliers:
    return ProductSupplier.find_all_by_product_id(id)


def find_first_by_id(id: int) -> Product:
    product = Product.find_first_by_id(id)
    if not product: raise ProductNotFound()
    return product


def find_first_supplier_rel_by_ids(
    id: int,
    supplier_id: int
) -> ProductSupplier:
    product_supplier = ProductSupplier.find_first_by_ids(
        id, 
        supplier_id
    )
    if not product_supplier: raise ProductSupplierNotFound()
    return product_supplier


def update(id: int, data: ProductModel) -> Product:
    product = find_first_by_id(id)
    product.update(**data)
    Product.save(product)
    return product


def delete(id: int) -> None:
    product = find_first_by_id(id)
    Product.delete(product)


def delete_supplier_rel(id: int, supplier_id: int) -> None:
    product_supplier = find_first_supplier_rel_by_ids(id, supplier_id)
    ProductSupplier.delete(product_supplier)
