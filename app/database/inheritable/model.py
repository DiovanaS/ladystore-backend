from datetime import datetime
from flask_sqlalchemy.model import Model as SQLAlchemyModel
from re import findall
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
from typing import List

from app.extensions import database


Models = List['Model']


class Model(SQLAlchemyModel):
    @declared_attr
    def __tablename__(cls):
        cls_name_words = findall(r'[A-Z][a-z]*', cls.__name__)
        return '_'.join(cls_name_words).lower()

    @declared_attr
    def created_at(cls):
        return Column(
            DateTime,
            nullable=False,
            default=datetime.now()
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            nullable=False,
            default=datetime.now(),
            onupdate=datetime.now()
        )

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
        columns: List = None,
        joins: List = None,
        filters: List = None,
        ordinances: List = None
    ) -> Models:
        query = cls.query
        if columns:
            query = query.with_entities(*columns)
        for join in joins or []:
            query = query.join(join)
        if filters:
            query = query.filter(*filters)
        if ordinances:
            query = query.order_by(*ordinances)
        return query.all()

    @classmethod
    def _query_first(cls, filters=[]) -> 'Model':
        return cls.query.filter(*filters).first()
