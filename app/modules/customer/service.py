from typing import Dict

from app.database import Customer, Customers

from .exception import CustomerAlreadyExists, CustomerNotFound
from .schema import customer_schema


def create(data: Dict[str, object]) -> Customer:
    customer = customer_schema.load(data)
    already_exists = Customer.find_first_by_cpf_or_email(
        customer.cpf,
        customer.email
    )
    if already_exists: raise CustomerAlreadyExists()
    Customer.save(customer)
    return customer


def find_all() -> Customers:
    return Customer.find_all()


def find_all_by_name(name: str) -> Customers:
    return Customer.find_all_by_name(name)


def find_first_by_id(id: str) -> Customer:
    customer = Customer.find_first_by_id(id)
    if not customer: raise CustomerNotFound()
    return customer


def update(id: int, data: Dict[str, object]) -> Customer:
    customer = customer_schema.load(
        data,
        instance=find_first_by_id(id),
        partial=True
    )
    existing_customer = Customer.find_first_by_cpf_or_email(
        customer.cpf,
        customer.email
    )
    already_exists = existing_customer and existing_customer.id != id
    if already_exists: raise CustomerAlreadyExists()
    Customer.save(customer)
    return customer


def delete(id: int) -> None:
    Customer.delete(find_first_by_id(id))
