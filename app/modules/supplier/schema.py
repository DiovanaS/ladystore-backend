from app.database import Supplier
from app.extensions import marshmallow


class SupplierSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        load_instance = True
        include_relationships = True


supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)
