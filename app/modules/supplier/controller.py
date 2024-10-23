from flask import request
from http import HTTPStatus

from app.facades import response

from . import service as supplier_service, supplier
from .schema import supplier_schema, suppliers_schema


@supplier.post('/create')
def create():
    return response.as_schema(
        supplier_schema,
        supplier_service.create(request.get_json()),
        HTTPStatus.CREATED
    )


@supplier.get('/all')
def get_all():
    return response.as_schema(
        suppliers_schema,
        supplier_service.find_all()
    )


@supplier.get('/all/<string:name>')
def get_all_by_company_name_or_trading_name(name: str):
    return response.as_schema(
        suppliers_schema,
        supplier_service.find_all_by_company_name_or_trading_name(
            name
        )
    )


@supplier.get('/one/<int:id>')
def get_one_by_id(id: int):
    return response.as_schema(
        supplier_schema,
        supplier_service.find_first_by_id(id)
    )


@supplier.patch('/update/<int:id>')
def update(id: int):
    return response.as_schema(
        supplier_schema,
        supplier_service.update(id, request.get_json())
    )


@supplier.delete('/delete/<int:id>')
def delete(id: int):
    supplier_service.delete(id)
    return response.as_message('Supplier deleted.')
