from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    stock_not_found,
    product_not_found,
    stock_relationship_not_found
)
from app.model import stock_model
from app.service import stock_service

ns = Namespace(
    'stock',
    description='Stock operations',
    path='/stock',
    validate=True
)


@ns.route('/')
class Stock(Resource):
    @ns.doc('create')
    @ns.expect(stock_model)
    @ns.marshal_with(stock_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new stock entry '''
        return stock_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(stock_model)
    def get(self):
        ''' Get all stock entries '''
        return stock_service.find_all()


@ns.route('/<int:id>')
@ns.param('id', 'The stock identifier')
@ns.response(*stock_not_found)
class StockById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(stock_model)
    def get(self, id: int):
        ''' Get a stock entry by ID '''
        return stock_service.find_first_by_id(id)

    @ns.doc('update')
    @ns.expect(stock_model)
    @ns.marshal_with(stock_model)
    def put(self, id: int):
        ''' Update a stock entry by ID '''
        return stock_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a stock entry by ID '''
        stock_service.delete(id)
        return None, HTTPStatus.NO_CONTENT
    
@ns.route('/search')
class StockSearch(Resource):
    @ns.doc('search_stock')
    @ns.param('name', 'The stock name to search for', required=False)
    @ns.param('barcode', 'The product barcode to search for', required=False)
    @ns.param('code', 'The stock code to search for', required=False)
    @ns.marshal_list_with(stock_model)
    def get(self):
        ''' Search stock by name, barcode, or code '''
        name = ns.payload.get('name')
        barcode = ns.payload.get('barcode')
        code = ns.payload.get('code')
        return stock_service.search(name=name, barcode=barcode, code=code)


