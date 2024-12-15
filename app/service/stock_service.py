from app.database import Stock, Product, StockProduct
from app.exception import StockNotFound, ProductNotFound, StockRelationshipNotFound
from app.model import StockModel


def create(data: StockModel) -> Stock:
    stock = Stock(**data)
    Stock.save(stock)
    return stock


def find_all():
    return Stock.find_all()


def find_first_by_id(id: int) -> Stock:
    stock = Stock.find_first_by_id(id)
    if not stock:
        raise StockNotFound()
    return stock


def update(id: int, data: StockModel) -> Stock:
    stock = find_first_by_id(id)
    stock.update(**data)
    Stock.save(stock)
    return stock


def delete(id: int):
    stock = find_first_by_id(id)
    Stock.delete(stock)


def create_product_rel(data):
    stock = Stock.find_first_by_id(data['stock_id'])
    if not stock:
        raise StockNotFound()

    product = Product.find_first_by_id(data['product_id'])
    if not product:
        raise ProductNotFound()

    existing_relation = StockProduct.find_first_by_ids(data['stock_id'], data['product_id'])
    if existing_relation:
        raise StockRelationshipNotFound("Relationship already exists")

    stock_product = StockProduct(
        stock_id=data['stock_id'],
        product_id=data['product_id']
    )
    StockProduct.save(stock_product)
    return stock_product


def find_product_rel_by_ids(stock_id: int, product_id: int):
    relation = StockProduct.find_first_by_ids(stock_id, product_id)
    if not relation:
        raise StockRelationshipNotFound()
    return relation


def delete_product_rel(stock_id: int, product_id: int):
    relation = find_product_rel_by_ids(stock_id, product_id)
    StockProduct.delete(relation)


def search(name: str = None, barcode: str = None, code: str = None):
    filters = []
    if name:
        filters.append(Stock.name.ilike(f'%{name}%'))
    if barcode:
        filters.append(Product.barcode.ilike(f'%{barcode}%'))
    if code:
        filters.append(Stock.code == code)

    query = Stock.query
    if filters:
        query = query.join(StockProduct).join(Product).filter(*filters)

    return query.all()

