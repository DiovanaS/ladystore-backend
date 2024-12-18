from flask import request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    user_already_exists,
    user_not_found
)
from app.model import user_model
from app.service import user_service


ns = Namespace(
    'user',
    description='User operations',
    path='/user',
    validate=True
)


@ns.route('/')
class User(Resource):
    _SEARCH_ARGS = ('name', 'email')

    @ns.doc('create')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(*user_already_exists)
    def post(self):
        ''' Create a new user '''
        return (
            user_service.create(ns.payload),
            HTTPStatus.CREATED
        )

    @ns.doc('get_all')
    @ns.param(_SEARCH_ARGS[0], 'Filter by name', required=False)
    @ns.param(_SEARCH_ARGS[1], 'Filter by email', required=False)
    @ns.marshal_list_with(user_model)
    def get(self):
        ''' Get all users '''
        return user_service.find_all_by(**{
            arg: request.args.get(arg)
            for arg in self._SEARCH_ARGS
        })


@ns.route('/<int:id>')
@ns.param('id', 'The user identifier')
@ns.response(*user_not_found)
class UserById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(user_model)
    def get(self, id: int):
        ''' Get a user by ID '''
        return user_service.find_first_by_id(id)

    @ns.doc('update')
    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a user by ID '''
        return user_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a user by ID '''
        user_service.delete(id)
        return (None, HTTPStatus.NO_CONTENT)
