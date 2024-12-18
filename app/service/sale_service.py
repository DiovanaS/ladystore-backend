from app.database import Sale, Product, Stock, Customer
from app.exception import (
    SaleNotFound,
    CustomerNotFound,
    ProductNotFound,
    StockNotSufficient,
    StockRelationshipNotFound
)
from app.model import SaleModel

def create(data: SaleModel) -> Sale:
    customer = Customer.find_first_by_id(data['customer_id'])
    if not customer:  raise CustomerNotFound()
    sale = Sale(**data)
    Sale.save(sale)
    return sale


def find_all():
    return Sale._query_all()


def find_first_by_id(id: int) -> Sale:
    sale = Sale.find_first_by_id(id)
    if not sale:
        raise SaleNotFound()
    return sale


def update(id: int, data: SaleModel) -> Sale:
    sale = find_first_by_id(id)
    customer = Customer.find_first_by_id(data['customer_id'])
    if not customer:  raise CustomerNotFound()
    sale.update(**data)
    Sale.save(sale)
    return sale


def delete(id: int):
    sale = find_first_by_id(id)
    for product in sale.product:
        stock = Stock.find_first_by_product_id(product.id)
        if stock:
            stock.quantity += product.quantity
            Stock.save(stock)

    Sale.delete(sale)


def assign_customer_to_sale(data):
    sale = find_first_by_id(data['sale_id'])
    customer = Customer.find_first_by_id(data['customer_id'])
    if not customer: raise CustomerNotFound()
    sale.customer = customer
    Sale.save(sale)
    return customer


def find_customer_by_sale_id(sale_id: int):
    sale = find_first_by_id(sale_id)
    if not sale.customer:
        raise CustomerNotFound()
    return sale.customer


def delete_customer_rel(sale_id: int):
    sale = find_first_by_id(sale_id)
    if not sale.customer: raise CustomerNotFound()
    sale.customer = None
    Sale.delete(sale)



def search(product: str = None, customer: str = None, code: str = None):
    query = Sale.query
    if product:
        query = query.join(Product).filter(Product.name.ilike(f'%{product}%'))
    if customer:
        query = query.join(Customer).filter(Customer.name.ilike(f'%{customer}%'))
    if code:
        query = query.filter(Sale.code.ilike(f'%{code}%'))
    return query.all()
