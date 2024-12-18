from flask import request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    product_not_found,
)
from app.model import product_model
from app.service import product_service


ns = Namespace(
    'product',
    description='Product operations',
    path='/product',
    validate=True
)


@ns.route('/')
class Product(Resource):
    _SEARCH_ARGS = ('name', 'size')

    @ns.doc('create')
    @ns.expect(product_model)
    @ns.marshal_with(product_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    def post(self):
        ''' Create a new product '''
        return (
            product_service.create(ns.payload),
            HTTPStatus.CREATED
        )

    @ns.doc('get_all')
    @ns.param(_SEARCH_ARGS[0], 'Filter by name', required=False)
    @ns.param(_SEARCH_ARGS[1], 'Filter by size', required=False)
    @ns.marshal_list_with(product_model)
    def get(self):
        ''' Get all products '''
        return product_service.find_all_by(**{
            arg: request.args.get(arg)
            for arg in self._SEARCH_ARGS
        })




@ns.route('/<int:id>')
@ns.param('id', 'The product identifier')
@ns.response(*product_not_found)
class ProductById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(product_model)
    def get(self, id: int):
        ''' Get a product by ID '''
        return product_service.find_first_by_id(id)

    @ns.doc('update')
    @ns.expect(product_model)
    @ns.marshal_with(product_model)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a product by ID '''
        return product_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a product by ID '''
        product_service.delete(id)
        return (None, HTTPStatus.NO_CONTENT)