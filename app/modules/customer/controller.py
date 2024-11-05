from flask import Blueprint
from flask import request
from http import HTTPStatus

from app.facades import response

from . import service as customer_service
from .schema import customer_schema, customers_schema

customer = Blueprint('customer', __name__, url_prefix='/customer')

@customer.post('/create')
def create():
    return response.as_schema(
        customer_schema,
        customer_service.create(request.get_json()),
        HTTPStatus.CREATED
    )


@customer.get('/all')
def get_all():
    return response.as_schema(
        customers_schema,
        customer_service.find_all()
    )


@customer.get('/all/<string:name>')
def get_all_by_name(name: str):
    return response.as_schema(
        customers_schema,
        customer_service.find_all_by_name(name)
    )


@customer.get('/one/<int:id>')
def get_one_by_id(id: int):
    return response.as_schema(
        customer_schema,
        customer_service.find_first_by_id(id)
    )

@customer.patch('/update/<int:id>')
def update(id: int):
    return response.as_schema(
        customer_schema,
        customer_service.update(id, request.get_json())
    )

@customer.delete('/delete/<int:id>')
def delete(id: int):
    customer_service.delete(id)
    return response.as_message('Customer deleted.')

