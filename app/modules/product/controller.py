from flask import request
from http import HTTPStatus

from app.facades import response

from . import service as product_service, product
from .schema import product_schema, products_schema


@product.post('/create')
def create():
    return response.as_schema(
        product_schema,
        product_service.create(request.get_json()),
        HTTPStatus.CREATED
    )


@product.get('/all')
def get_all():
    return response.as_schema(
        products_schema,
        product_service.find_all()
    )


@product.get('/all/<string:name>')
def get_all_by_name(name: str):
    return response.as_schema(
        products_schema,
        product_service.find_all_by_name(name)
    )


@product.get('/one/<int:id>')
def get_one_by_id(id: int):
    return response.as_schema(
        product_schema,
        product_service.find_first_by_id(id)
    )


@product.patch('/update/<int:id>')
def update(id: int):
    return response.as_schema(
        product_schema,
        product_service.update(id, request.get_json())
    )


@product.delete('/delete/<int:id>')
def delete(id: int):
    product_service.delete(id)
    return response.as_message('Product deleted.')
