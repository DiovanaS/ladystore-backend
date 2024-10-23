from app.database import Product
from app.extensions import marshmallow


class ProductSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_relationships = True


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
