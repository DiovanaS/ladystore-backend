from flask_sqlalchemy.model import Model as SQLAlchemyModel
from re import findall
from sqlalchemy.ext.declarative import declared_attr
from typing import Dict, List

from app.extension import database


Models = List['Model']


class Model(SQLAlchemyModel):
    @declared_attr
    def __tablename__(cls):
        cls_name_words = findall(r'[A-Z][a-z]*', cls.__name__)
        return '_'.join(cls_name_words).lower()

    @staticmethod
    def save(model: 'Model') -> None:
        try:
            database.session.add(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @staticmethod
    def delete(model: 'Model') -> None:
        try:
            database.session.delete(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def _query_all(
        cls,
        columns: List | None = None,
        joins: List | None = None,
        icontains: Dict | None = None,
        ordinances: List | None = None
    ) -> Models:
        query = cls.query
        if columns: query = query.with_entities(*columns)
        for join in joins or []: query = query.join(join)
        if icontains:
            filters = [
                getattr(cls, key).icontains(value) 
                for key, value in icontains.items()
                if value is not None
            ]
            query = query.filter(*filters)
        if ordinances: query = query.order_by(*ordinances)
        return query.all()

    @classmethod
    def _query_first(cls, filters=[]) -> 'Model':
        return cls.query.filter(*filters).first()

    def __init__(self, **data) -> None:
        self.__dict__.update(data)

    def update(self, **data) -> None:
        for field, value in data.items():
            setattr(self, field, value)
