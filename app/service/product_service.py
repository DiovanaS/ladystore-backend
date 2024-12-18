from app.database import (
    Product, Products,
)
from app.exception import (
    ProductNotFound,
)
from app.model import ProductModel
from app.service import supplier_service


def create(data: ProductModel) -> Product:
    product = Product(**data)
    Product.save(product)
    return product

def find_all():
    return Product._query_all()

def find_all_by(**values) -> Products:
    return Product.find_all_by(**values)


def find_first_by_id(id: int) -> Product:
    product = Product.find_first_by_id(id)
    if not product: raise ProductNotFound()
    return product

def update(id: int, data: ProductModel) -> Product:
    product = find_first_by_id(id)
    product.update(**data)
    Product.save(product)
    return product


def delete(id: int) -> None:
    product = find_first_by_id(id)
    Product.delete(product)