from app.database import Customer
from app.extensions import marshmallow


class CustomerSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
