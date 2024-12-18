from http import HTTPStatus
from werkzeug.exceptions import NotFound


class CustomerNotFound(NotFound):
    description = 'Customer not found'


class ProductNotFound(NotFound):
    description = 'Product not found'

class SupplierNotFound(NotFound):
    description = 'Supplier not found'


class SaleNotFound(NotFound):
    description = 'Sale not found'


class FinancialNotFound(NotFound):
    description = 'Financial transaction not found'


class FinancialSaleNotFound(NotFound):
    description = 'Financial-sale relationship not found'


class StockRelationshipNotFound(NotFound):
    description = 'Stock-product relationship not found'


class StockNotFound(NotFound):
    description = 'Stock not found'

_response = lambda exception: (HTTPStatus.NOT_FOUND, exception.description)

customer_not_found = _response(CustomerNotFound)

product_not_found = _response(ProductNotFound)

supplier_not_found = _response(SupplierNotFound)

sale_not_found = _response(SaleNotFound)

financial_not_found = _response(FinancialNotFound)

financial_sale_not_found = _response(FinancialSaleNotFound)

stock_relationship_not_found = _response(StockRelationshipNotFound)

stock_not_found = _response(StockNotFound)
