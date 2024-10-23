from app.database import ProductSupplier
from app.extensions import marshmallow


class SupplierRelSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = ProductSupplier
        load_instance = True
        include_fks = True
        include_relationships = True

    product_id = marshmallow.auto_field()
    supplier_id = marshmallow.auto_field()


supplier_rel_schema = SupplierRelSchema()
supplier_rels_schema = SupplierRelSchema(many=True)
