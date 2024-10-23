from typing import Dict

from app.database import Product, Products

from .exception import ProductNotFound
from .schema import product_schema


def create(data: Dict[str, object]) -> Product:
    product = product_schema.load(data)
    Product.save(product)
    return product


def find_all() -> Products:
    return Product.find_all()


def find_all_by_name(name: str) -> Products:
    return Product.find_all_by_name(name)


def find_first_by_id(id: str) -> Product:
    product = Product.find_first_by_id(id)
    if not product: raise ProductNotFound()
    return product


def update(id: str, data: Dict[str, object]) -> Product:
    product = product_schema.load(
        data,
        instance=find_first_by_id(id),
        partial=True
    )
    Product.save(product)
    return product


def delete(id: str) -> None:
    Product.delete(find_first_by_id(id))
