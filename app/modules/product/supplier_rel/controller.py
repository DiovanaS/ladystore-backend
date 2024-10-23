from flask import request
from http import HTTPStatus

from app.facades import response

from . import service as supplier_rel_service, supplier_rel
from .schema import supplier_rel_schema, supplier_rels_schema


@supplier_rel.post('/create')
def create():
    return response.as_schema(
        supplier_rel_schema,
        supplier_rel_service.create(request.get_json()),
        HTTPStatus.CREATED
    )


@supplier_rel.get('/all/<int:product_id>')
def get_all_by_product_id(product_id: int):
    return response.as_schema(
        supplier_rels_schema,
        supplier_rel_service.find_all_by_product_id(
            product_id
        )
    )


@supplier_rel.get('/one/<int:product_id>/<int:supplier_id>')
def get_one(product_id: int, supplier_id: int):
    return response.as_schema(
        supplier_rel_schema,
        supplier_rel_service.find_first_by_ids(
            product_id,
            supplier_id
        )
    )


@supplier_rel.delete('/delete/<int:product_id>/<int:supplier_id>')
def delete(product_id: int, supplier_id: int):
    supplier_rel_service.delete(product_id, supplier_id)
    return response.as_message('Supplier relation deleted.')
