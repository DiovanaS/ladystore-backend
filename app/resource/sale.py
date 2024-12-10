from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    sale_not_found,
    customer_not_found,
    stock_relationship_not_found,
    stock_not_sufficient
)
from app.model import sale_model, customer_model, sale_customer_stock_model
from app.service import sale_service


ns = Namespace(
    'sale',
    description='Sales operations',
    path='/sale',
    validate=True
)


@ns.route('/')
class Sale(Resource):
    @ns.doc('create')
    @ns.expect(sale_model)
    @ns.marshal_with(sale_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(*customer_not_found)
    @ns.response(*stock_not_sufficient)
    def post(self):
        ''' Create a new sale '''
        return sale_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(sale_model)
    def get(self):
        ''' Get all sales '''
        return sale_service.find_all()


@ns.route('/<int:id>')
@ns.param('id', 'The sale identifier')
@ns.response(*sale_not_found)
class SaleById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(sale_model)
    def get(self, id: int):
        ''' Get a sale by ID '''
        return sale_service.find_first_by_id(id)

    @ns.doc('update')
    @ns.expect(sale_model)
    @ns.marshal_with(sale_model)
    @ns.response(*invalid_payload)
    @ns.response(*customer_not_found)
    @ns.response(*stock_not_sufficient)
    def put(self, id: int):
        ''' Update a sale by ID '''
        return sale_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a sale by ID '''
        sale_service.delete(id)
        return None, HTTPStatus.NO_CONTENT


@ns.route('/customer')
class SaleCustomer(Resource):
    @ns.doc('create_customer_rel')
    @ns.expect(customer_model)
    @ns.marshal_with(customer_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(HTTPStatus.NOT_FOUND, 'Sale or customer not found')
    def post(self):
        ''' Assign a customer to a sale '''
        return (
            sale_service.assign_customer_to_sale(ns.payload),
            HTTPStatus.CREATED
        )


@ns.route('/<int:id>/customer')
@ns.param('id', 'The sale identifier')
class SaleCustomerById(Resource):
    @ns.doc('get_customer_by_sale_id')
    @ns.marshal_with(customer_model)
    def get(self, id: int):
        ''' Get the customer associated with a sale '''
        return sale_service.find_customer_by_sale_id(id)

    @ns.doc('delete_customer_rel')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Remove the customer relationship from a sale '''
        sale_service.delete_customer_rel(id)
        return None, HTTPStatus.NO_CONTENT


@ns.route('/<int:id>/stock')
@ns.param('id', 'The sale identifier')
class SaleStock(Resource):
    @ns.doc('get_all_stock_rels_by_id')
    @ns.marshal_list_with(sale_customer_stock_model)  
    def get(self, id: int):
        ''' Get all stock-product relationships by sale ID '''
        return sale_service.find_all_stock_rels_by_sale_id(id)

    @ns.doc('create_stock_rel')
    @ns.expect(sale_customer_stock_model)  
    @ns.marshal_with(sale_customer_stock_model, code=HTTPStatus.CREATED)  
    @ns.response(*invalid_payload)
    @ns.response(HTTPStatus.NOT_FOUND, 'Sale or product not found')
    @ns.response(*stock_not_sufficient)
    def post(self, id: int):
        ''' Add a product to a sale and update stock '''
        return sale_service.create_stock_rel(id, ns.payload), HTTPStatus.CREATED


@ns.route('/<int:id>/stock/<int:product_id>')
@ns.param('id', 'The sale identifier')
@ns.param('product_id', 'The product identifier')
@ns.response(*sale_not_found)
@ns.response(*stock_relationship_not_found)
class SaleStockById(Resource):
    @ns.doc('get_one_stock_rel_by_ids')
    @ns.marshal_with(sale_customer_stock_model)  
    def get(self, id: int, product_id: int):
        ''' Get a specific stock-product relationship by sale ID and product ID '''
        return sale_service.find_stock_rel_by_ids(id, product_id)

    @ns.doc('delete_stock_rel')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int, product_id: int):
        ''' Delete a specific stock-product relationship by sale ID and product ID '''
        sale_service.delete_stock_rel(id, product_id)
        return None, HTTPStatus.NO_CONTENT


@ns.route('/search')
class SaleSearch(Resource):
    @ns.doc('search_sales')
    @ns.param('product', 'The product name to search for', required=False)
    @ns.param('customer', 'The customer name to search for', required=False)
    @ns.param('code', 'The sale code to search for', required=False)
    @ns.marshal_list_with(sale_model)
    def get(self):
        ''' Search sales by product, customer, or code '''
        product = ns.payload.get('product')
        customer = ns.payload.get('customer')
        code = ns.payload.get('code')
        return sale_service.search(product=product, customer=customer, code=code)
