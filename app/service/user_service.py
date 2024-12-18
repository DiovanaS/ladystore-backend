from app.database import User, Users
from app.exception import UserAlreadyExists, UserNotFound
from app.model import UserModel


def create(data: UserModel) -> User:
    already_exists = User.find_first_by_email(
        data['email']
    )
    if already_exists: raise UserAlreadyExists()
    user = User(**data)
    User.save(user)
    return user


def find_all_by(**values) -> Users:
    return User.find_all_by(**values)


def find_first_by_id(id: int) -> User:
    user = User.find_first_by_id(id)
    if not user:
        raise UserNotFound()
    return user


def update(id: int, data: UserModel) -> User:
    user = find_first_by_id(id)
    existing_user = User.find_first_by_email(
        data['email']
    )
    already_exists = existing_user and existing_user.id != id
    if already_exists: raise UserAlreadyExists()
    user.update(**data)
    User.save(user)
    return user


def delete(id: int) -> None:
    user = find_first_by_id(id)
    User.delete(user)
