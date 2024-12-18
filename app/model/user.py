from flask_restx.fields import Integer, String
from typing import TypedDict

from app.extension import api


_EMAIL_REGEX = r'^[\w\-.]+@([\w-]+\.)+[\w-]{2,4}$'
''' address@domain.com '''


class UserModel(TypedDict):
    id: int
    name: str
    email: str
    password: str


user_model = api.model('User', UserModel(
    id=Integer(title='ID', readonly=True),
    name=String(
        title='Name',
        required=True,
        min_length=1,
        max_length=80
    ),
    email=String(
        title='Email',
        required=True,
        min_length=1,
        max_length=80,
        pattern=_EMAIL_REGEX
    ),
    password=String(
        title='Password',
        required=True,
        max_length=80
    )
))
