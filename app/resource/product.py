from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.exception import (
    invalid_payload,
    product_not_found,
    product_supplier_already_exists,
    product_supplier_not_found
)
from app.model import product_model, product_supplier_model
from app.service import product_service


ns = Namespace(
    'product',
    description='Product operations',
    path='/product',
    validate=True
)


@ns.route('/')
class Product(Resource):
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
    @ns.marshal_list_with(product_model)
    def get(self):
        ''' Get all products '''
        return product_service.find_all()


@ns.route('/supplier')
class ProductSupplier(Resource):
    @ns.doc('create_supplier_rel')
    @ns.expect(product_supplier_model)
    @ns.marshal_with(product_supplier_model, code=HTTPStatus.CREATED)
    @ns.response(*invalid_payload)
    @ns.response(HTTPStatus.NOT_FOUND, 'Product or supplier not found')
    @ns.response(*product_supplier_already_exists)
    def post(self):
        ''' Create a new product-supplier relationship '''
        return (
            product_service.create_supplier_rel(ns.payload),
            HTTPStatus.CREATED
        )


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


@ns.route('/<int:id>/supplier')
@ns.param('id', 'The product identifier')
class ProductSupplierById(Resource):
    @ns.doc('get_all_supplier_rels_by_id')
    @ns.marshal_list_with(product_supplier_model)
    def get(self, id: int):
        ''' Get all product-supplier relatanships by (product) ID '''
        return product_service.find_all_supplier_rels_by_id(id)


@ns.route('/<int:id>/supplier/<int:supplier_id>')
@ns.param('id', 'The product identifier')
@ns.param('supplier_id', 'The supplier identifier')
@ns.response(*product_supplier_not_found)
class ProductSupplierByIds(Resource):
    @ns.doc('get_one_supplier_rel_by_ids')
    @ns.marshal_with(product_supplier_model)
    def get(self, id: int, supplier_id: int):
        ''' Get a product-supplier relationship by (product) ID and supplier ID '''
        return product_service.find_first_supplier_rel_by_ids(
            id,
            supplier_id
        )

    @ns.doc('delete_supplier_rel')
    @ns.response(HTTPStatus.NO_CONTENT, 'Success')
    def delete(self, id: int, supplier_id: int):
        ''' Delete a product-supplier relationship by (product) ID and supplier ID '''
        product_service.delete_supplier_rel(id, supplier_id)
        return (None, HTTPStatus.NO_CONTENT)


@ns.route('/search/<string:name>')
@ns.param('name', 'The product name')
class ProductByName(Resource):
    @ns.doc('get_all_by_name')
    @ns.marshal_list_with(product_model)
    def get(self, name: str):
        ''' Get all products by name '''
        return product_service.find_all_by_name(name)
