from app.database import Stock, Product
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

def search(name: str = None, barcode: str = None, code: str = None):
    filters = []
    if name:
        filters.append(Stock.name.ilike(f'%{name}%'))
    if barcode:
        filters.append(Product.barcode.ilike(f'%{barcode}%'))
    if code:
        filters.append(Stock.code == code)

    query = Stock.query

    return query.all()

