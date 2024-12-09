from app.database import Sale, Sales, Stock, Customer
from app.exception import SaleNotFound, StockNotSufficient, CustomerNotFound
from app.model import SaleModel


def create(data: SaleModel) -> Sale:
    customer = find_customer_by_id(data['customer_id'])
    if not customer: raise CustomerNotFound()
    stock = Stock.find_first_by_id(data['stock_id'])
    if not stock or stock.quantity < data['quantity']:
        raise StockNotSufficient()
    sale = Sale(**data)
    Sale.save(sale)
    stock.quantity -= data['quantity']
    Stock.save(stock)
    return sale


def find_all() -> Sales:
    return Sale.find_all()


def find_first_by_id(id: int) -> Sale:
    sale = Sale.find_first_by_id(id)
    if not sale:
        raise SaleNotFound()
    return sale


def update(id: int, data: SaleModel) -> Sale:
    sale = find_first_by_id(id)
    stock = Stock.find_first_by_id(data['stock_id'])
    if stock.quantity < data['quantity']:
        raise StockNotSufficient()
    sale.update(**data)
    Sale.save(sale)
    stock.quantity -= data['quantity']
    Stock.save(stock)
    return sale

def delete(id: int) -> None:
    sale = find_first_by_id(id)
    Stock.restore_stock_after_sale(sale)
    Sale.delete(sale)

def find_customer_by_id(customer_id: int):
    return Customer.find_first_by_id(customer_id)
