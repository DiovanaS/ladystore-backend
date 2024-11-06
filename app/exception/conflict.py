from http import HTTPStatus
from werkzeug.exceptions import Conflict


class CustomerAlreadyExists(Conflict):
    description = 'CPF and/or email already registered'


class ProductSupplierAlreadyExists(Conflict):
    description = 'Product-supplier relation already exists'


class SupplierAlreadyExists(Conflict):
    description = 'CNPJ already registered'


_response = lambda exception: (HTTPStatus.CONFLICT, exception.description)

customer_already_exists = _response(CustomerAlreadyExists)

product_supplier_already_exists = _response(ProductSupplierAlreadyExists)

supplier_already_exists = _response(SupplierAlreadyExists)
