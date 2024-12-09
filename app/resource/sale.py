from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    sale_not_found,
    customer_not_found,
    stock_not_sufficient
)
from app.model import sale_model
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
