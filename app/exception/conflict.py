from http import HTTPStatus
from werkzeug.exceptions import Conflict


class CustomerAlreadyExists(Conflict):
    description = 'CPF and/or email already registered'

class SupplierAlreadyExists(Conflict):
    description = 'CNPJ already registered'


class StockNotSufficient(Conflict):
    description = 'Insufficient stock for this sale'


class SaleAlreadyExists(Conflict):
    description = 'Sale already exists for the given client and product'


class FinancialAlreadyExists(Conflict):
    description = 'Financial transaction already exists for this sale'


class FinancialSaleAlreadyExists(Conflict):
    description = 'Financial-sale relationship already exists'

class StockNotSufficient(Conflict):
    description = 'Insufficient stock for the requested product'
    

_response = lambda exception: (HTTPStatus.CONFLICT, exception.description)

customer_already_exists = _response(CustomerAlreadyExists)


supplier_already_exists = _response(SupplierAlreadyExists)

stock_not_sufficient = _response(StockNotSufficient)

sale_already_exists = _response(SaleAlreadyExists)

financial_already_exists = _response(FinancialAlreadyExists)

financial_sale_already_exists = _response(FinancialSaleAlreadyExists)

stock_not_sufficient = _response(StockNotSufficient)