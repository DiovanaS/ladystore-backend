from flask import request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    customer_already_exists,
    customer_not_found,
    invalid_payload
)
from app.model import customer_model
from app.service import customer_service


ns = Namespace(
    'customer', 
    description='Customer operations',
    path='/customer',
    validate=True
)


@ns.route('/')
class Customer(Resource):
    _SEARCH_ARGS = ('name', 'email', 'cpf', 'phone', 'birthdate')

    @ns.doc('create')
    @ns.expect(customer_model)
    @ns.marshal_with(customer_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(*customer_already_exists)
    def post(self):
        ''' Create a new customer '''
        return (
            customer_service.create(ns.payload),
            HTTPStatus.CREATED
        )

    @ns.doc('get_all')
    @ns.param(_SEARCH_ARGS[0], 'Filter by name', required=False)
    @ns.param(_SEARCH_ARGS[1], 'Filter by e-mail', required=False)
    @ns.param(_SEARCH_ARGS[2], 'Filter by CPF', required=False)
    @ns.param(_SEARCH_ARGS[3], 'Filter by phone', required=False)
    @ns.param(_SEARCH_ARGS[4], 'Filter by birthdate', required=False)
    @ns.marshal_list_with(customer_model)
    def get(self):
        ''' Get all customers '''
        return customer_service.find_all_by(**{
            arg: request.args.get(arg)
            for arg in self._SEARCH_ARGS
        })


@ns.route('/<int:id>')
@ns.param('id', 'The customer identifier')
@ns.response(*customer_not_found)
class CustomerById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(customer_model)
    def get(self, id: int):
        ''' Get a customer by ID '''
        return customer_service.find_first_by_id(id)

    @ns.doc('update')
    @ns.expect(customer_model)
    @ns.marshal_with(customer_model)
    @ns.response(*invalid_payload)
    @ns.response(*customer_already_exists)
    def put(self, id: int):
        ''' Update a customer by ID '''
        return customer_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a customer by ID '''
        customer_service.delete(id)
        return (None, HTTPStatus.NO_CONTENT)
