from app.database import Sale, Product, Stock, Customer, SaleCustomerStockModel
from app.exception import (
    SaleNotFound,
    CustomerNotFound,
    ProductNotFound,
    StockNotSufficient,
    StockRelationshipNotFound
)
from app.model import SaleModel, sale_customer_stock_model

def create(data: SaleModel) -> Sale:
    customer = Customer.find_first_by_id(data['customer_id'])
    if not customer:  raise CustomerNotFound()
    sale = Sale(**data)
    Sale.save(sale)
    return sale


def find_all():
    return Sale.find_all()


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
    SaleCustomerStockModel.query.filter_by(sale_id=sale.id).delete()
    for product in sale.products:
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
    Sale.save(sale)


def create_stock_rel(sale_id: int, data):
    sale = find_first_by_id(sale_id)
    if not sale:  raise SaleNotFound()
    product = Product.find_first_by_id(data['stock_id'])
    if not product:  raise ProductNotFound()
    customer = Customer.find_first_by_id(data['customer_id'])
    if not customer:  raise CustomerNotFound()
    stock = Stock.find_first_by_product_id(data['stock_id'])
    if not stock or stock.quantity < data['quantity']:
        raise StockNotSufficient(f"Insufficient stock for product ID {data['stock_id']}")
    stock.quantity -= data['quantity']
    Stock.save(stock)
    sale.products.append(product)
    sale.customer = customer  
    Sale.save(sale)

    sale_customer_stock = SaleCustomerStockModel(
        sale_id=sale.id,
        sale=sale,
        customer_id=customer.id,
        customer=customer,
        stock_id=stock.id,
        stock=stock
    )
    return sale_customer_stock 


def find_all_stock_rels_by_sale_id(sale_id: int):
    sale = find_first_by_id(sale_id)
    sale_customer_stock_rels = SaleCustomerStockModel.query.filter_by(sale_id=sale.id).all()
    return sale_customer_stock_rels 


def find_stock_rel_by_ids(sale_id: int, product_id: int):
    sale = find_first_by_id(sale_id)
    relation = SaleCustomerStockModel.query.filter_by(sale_id=sale.id, stock_id=product_id).first()
    if not relation:  raise StockRelationshipNotFound()
    return relation


def delete_stock_rel(sale_id: int, product_id: int):
    sale = find_first_by_id(sale_id)
    relation = find_stock_rel_by_ids(sale_id, product_id)
    stock = Stock.find_first_by_product_id(product_id)
    if stock:
        stock.quantity += relation.stock.quantity 
        Stock.save(stock)
    SaleCustomerStockModel.query.filter_by(sale_id=sale.id, stock_id=product_id).delete()
    Sale.save(sale)


def search(product: str = None, customer: str = None, code: str = None):
    query = Sale.query
    if product:
        query = query.join(Product).filter(Product.name.ilike(f'%{product}%'))
    if customer:
        query = query.join(Customer).filter(Customer.name.ilike(f'%{customer}%'))
    if code:
        query = query.filter(Sale.code.ilike(f'%{code}%'))
    return query.all()
