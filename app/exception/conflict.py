from http import HTTPStatus
from werkzeug.exceptions import Conflict


class CustomerAlreadyExists(Conflict):
    description = 'CPF and/or email already registered'


class ProductSupplierAlreadyExists(Conflict):
    description = 'Product-supplier relation already exists'


class SupplierAlreadyExists(Conflict):
    description = 'CNPJ already registered'


class StockNotSufficient(Conflict):
    description = 'Insufficient stock for this sale'


class SaleAlreadyExists(Conflict):
    description = 'Sale already exists for the given client and product'


_response = lambda exception: (HTTPStatus.CONFLICT, exception.description)

customer_already_exists = _response(CustomerAlreadyExists)

product_supplier_already_exists = _response(ProductSupplierAlreadyExists)

supplier_already_exists = _response(SupplierAlreadyExists)

stock_not_sufficient = _response(StockNotSufficient)

sale_already_exists = _response(SaleAlreadyExists)
