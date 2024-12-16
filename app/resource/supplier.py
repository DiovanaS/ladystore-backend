from flask import request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    supplier_already_exists,
    supplier_not_found
)
from app.model import supplier_model
from app.service import supplier_service


ns = Namespace(
    'supplier',
    description='Supplier operations',
    path='/supplier',
    validate=True
)


@ns.route('/')
class Supplier(Resource):
    _SEARCH_ARGS = ('company_name', 'trading_name', 'cnpj', 'phone')

    @ns.doc('create')
    @ns.expect(supplier_model)
    @ns.marshal_with(supplier_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(*supplier_already_exists)
    def post(self):
        ''' Create a new supplier '''
        return (
            supplier_service.create(ns.payload),
            HTTPStatus.CREATED
        )

    @ns.doc('get_all')
    @ns.param(_SEARCH_ARGS[0], 'Filter by company name', required=False)
    @ns.param(_SEARCH_ARGS[1], 'Filter by trading name', required=False)
    @ns.param(_SEARCH_ARGS[2], 'Filter by cnpj', required=False)
    @ns.param(_SEARCH_ARGS[3], 'Filter by phone', required=False)
    @ns.marshal_list_with(supplier_model)
    def get(self):
        ''' Get all suppliers '''
        return supplier_service.find_all_by(**{
            arg: request.args.get(arg)
            for arg in self._SEARCH_ARGS
        })


@ns.route('/<int:id>')
@ns.param('id', 'The supplier identifier')
@ns.response(*supplier_not_found)
class SupplierById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(supplier_model)
    def get(self, id: int):
        ''' Get a supplier by ID '''
        return supplier_service.find_first_by_id(id)

    @ns.doc('update')
    @ns.expect(supplier_model)
    @ns.marshal_with(supplier_model)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a supplier by ID '''
        return supplier_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a supplier by ID '''
        supplier_service.delete(id)
        return (None, HTTPStatus.NO_CONTENT)

