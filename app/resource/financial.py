from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    financial_already_exists,
    financial_sale_already_exists,
    financial_not_found,
    financial_sale_not_found,
    sale_not_found
)
from app.model import financial_model, financial_sale_model
from app.service import financial_service

ns = Namespace(
    'financial',
    description='Financial operations',
    path='/financial',
    validate=True
)

@ns.route('/')
class Financial(Resource):
    @ns.doc('create')
    @ns.expect(financial_model)
    @ns.marshal_with(financial_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(*financial_already_exists)
    @ns.response(*sale_not_found)
    def post(self):
        ''' Create a new financial transaction '''
        return financial_service.create(ns.payload), HTTPStatus.CREATED

    @ns.doc('get_all')
    @ns.marshal_list_with(financial_model)
    def get(self):
        ''' Get all financial transactions '''
        return financial_service.find_all()


@ns.route('/<int:id>')
@ns.param('id', 'The financial transaction identifier')
@ns.response(*financial_not_found)
class FinancialById(Resource):
    @ns.doc('get_one')
    @ns.marshal_with(financial_model)
    def get(self, id: int):
        ''' Get a financial transaction by ID '''
        return financial_service.find_first_by_id(id)

    @ns.doc('update')
    @ns.expect(financial_model)
    @ns.marshal_with(financial_model)
    @ns.response(*invalid_payload)
    def put(self, id: int):
        ''' Update a financial transaction by ID '''
        return financial_service.update(id, ns.payload)

    @ns.doc('delete')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int):
        ''' Delete a financial transaction by ID '''
        financial_service.delete(id)
        return None, HTTPStatus.NO_CONTENT


@ns.route('/sale')
class FinancialSale(Resource):
    @ns.doc('create_financial_sale_rel')
    @ns.expect(financial_sale_model)
    @ns.marshal_with(financial_sale_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(HTTPStatus.NOT_FOUND, 'Financial transaction or sale not found')
    @ns.response(*financial_sale_already_exists)
    def post(self):
        ''' Create a new financial-sale relationship '''
        return financial_service.create_financial_sale_rel(ns.payload), HTTPStatus.CREATED



@ns.route('/<int:id>/sale')
@ns.param('id', 'The financial transaction identifier')
@ns.response(*financial_not_found)
class FinancialSaleById(Resource):
    @ns.doc('get_all_sales_by_financial_id')
    @ns.marshal_list_with(financial_sale_model)
    def get(self, id: int):
        ''' Get all sales related to a financial transaction by ID '''
        return financial_service.find_all_sales_by_financial_id(id)


@ns.route('/<int:id>/sale/<int:sale_id>')
@ns.param('id', 'The financial transaction identifier')
@ns.param('sale_id', 'The sale identifier')
@ns.response(*financial_sale_not_found)
class FinancialSaleByIds(Resource):
    @ns.doc('get_one_sale_rel_by_ids')
    @ns.marshal_with(financial_sale_model)
    def get(self, id: int, sale_id: int):
        ''' Get a financial-sale relationship by financial ID and sale ID '''
        return financial_service.find_first_sale_rel_by_ids(id, sale_id)

    @ns.doc('delete_sale_rel')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int, sale_id: int):
        ''' Delete a financial-sale relationship by financial ID and sale ID '''
        financial_service.delete_sale_rel(id, sale_id)
        return None, HTTPStatus.NO_CONTENT
