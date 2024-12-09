from http import HTTPStatus
from werkzeug.exceptions import NotFound


class CustomerNotFound(NotFound):
    description = 'Customer not found'


class ProductNotFound(NotFound):
    description = 'Product not found'


class ProductSupplierNotFound(NotFound):
    description = 'Product-supplier relation not found'


class SupplierNotFound(NotFound):
    description = 'Supplier not found'

class SaleNotFound(NotFound):
    description = 'Sale not found'


class FinancialNotFound(NotFound):
    description = 'Financial transaction not found'

class FinancialSaleNotFound(NotFound):
    description = 'Financial-sale relationship not found'


_response = lambda exception: (HTTPStatus.NOT_FOUND, exception.description)

customer_not_found = _response(CustomerNotFound)

product_not_found = _response(ProductNotFound)

product_supplier_not_found = _response(ProductSupplierNotFound)

supplier_not_found = _response(SupplierNotFound)

sale_not_found = _response(SaleNotFound)

financial_not_found = _response(FinancialNotFound)

financial_sale_not_found = _response(FinancialSaleNotFound)
