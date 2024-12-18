from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

from app.extension import database

from ..inheritable import Model, TimestampMixin


Users = List['User']


class User(database.Model, Model, TimestampMixin):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    password = Column(String(60), nullable=True)

    @classmethod
    def find_all_by(cls, **values) -> Users:
        return cls._query_all(
            icontains=values,
            ordinances=[
                cls.name,
                cls.email
            ]
        )

    @classmethod
    def find_first_by_id(cls, id: int) -> 'User':
        return cls._query_first(filters=[cls.id == id])

    @classmethod
    def find_first_by_email(cls, email: str) -> 'User':
        return cls._query_first(filters=[cls.email == email])
