from app.database import Financial, Financials, Sale, FinancialSale
from app.exception import (
    FinancialAlreadyExists,
    FinancialNotFound,
    SaleNotFound,
    FinancialSaleAlreadyExists,
    FinancialSaleNotFound
)
from app.model import FinancialModel, FinancialSaleModel

def create(data: FinancialModel) -> Financial:
    sale = Sale.find_first_by_id(data['sale_id'])
    if not sale:  raise SaleNotFound()
    already_exists = Financial.find_first_by_sale_id(data['sale_id'])
    if already_exists:  raise FinancialAlreadyExists()
    financial = Financial(**data)
    Financial.save(financial)
    return financial


def find_all():
    return Financial._query_all()


def find_all_ordered_by_operation_date() -> Financials:
    return Financial.query.order_by(Financial.operation_date.asc()).all()


def find_first_by_id(id: int) -> Financial:
    financial = Financial.find_first_by_id(id)
    if not financial:
        raise FinancialNotFound()
    return financial


def update(id: int, data: FinancialModel) -> Financial:
    financial = find_first_by_id(id)
    financial.update(**data)
    Financial.save(financial)
    return financial


def delete(id: int) -> None:
    financial = find_first_by_id(id)
    Financial.delete(financial)


def create_financial_sale_rel(data: FinancialSaleModel) -> FinancialSale:
    financial = Financial.find_first_by_id(data['financial_id'])
    if not financial:  raise FinancialNotFound()
    sale = Sale.find_first_by_id(data['sale_id'])
    if not sale:  raise SaleNotFound()
    already_exists = FinancialSale.find_first_by_ids(data['financial_id'], data['sale_id'])
    if already_exists:  raise FinancialSaleAlreadyExists()
    financial_sale = FinancialSale(**data)
    FinancialSale.save(financial_sale)
    return financial_sale


def find_all_sales_by_financial_id(financial_id: int) -> Financials:
    return FinancialSale.find_all_by_financial_id(financial_id)


def find_first_sale_rel_by_ids(financial_id: int, sale_id: int) -> FinancialSale:
    relation = FinancialSale.find_first_by_ids(financial_id, sale_id)
    if not relation:
        raise FinancialSaleNotFound()
    return relation


def delete_sale_rel(financial_id: int, sale_id: int) -> None:
    relation = find_first_sale_rel_by_ids(financial_id, sale_id)
    FinancialSale.delete(relation)

