from app.database import Customer, Customers
from app.exception import CustomerAlreadyExists, CustomerNotFound
from app.model import CustomerModel


def create(data: CustomerModel) -> Customer:
    already_exists = Customer.find_first_by_cpf_or_email(
        data['cpf'],
        data['email']
    )
    if already_exists: raise CustomerAlreadyExists()
    customer = Customer(**data)
    Customer.save(customer)
    return customer


def find_all_by(**values) -> Customers:
    return Customer.find_all_by(**values)


def find_first_by_id(id: int) -> Customer:
    customer = Customer.find_first_by_id(id)
    if not customer: raise CustomerNotFound()
    return customer


def update(id: int, data: CustomerModel) -> Customer:
    customer = find_first_by_id(id)
    existing_customer = Customer.find_first_by_cpf_or_email(
        data['cpf'],
        data['email']
    )
    already_exists = existing_customer and existing_customer.id != id
    if already_exists: raise CustomerAlreadyExists()
    customer.update(**data)
    Customer.save(customer)
    return customer


def delete(id: int) -> None:
    customer = find_first_by_id(id)
    Customer.delete(customer)
