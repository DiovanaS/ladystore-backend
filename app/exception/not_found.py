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


_response = lambda exception: (HTTPStatus.NOT_FOUND, exception.description)

customer_not_found = _response(CustomerNotFound)

product_not_found = _response(ProductNotFound)

product_supplier_not_found = _response(ProductSupplierNotFound)

supplier_not_found = _response(SupplierNotFound)
