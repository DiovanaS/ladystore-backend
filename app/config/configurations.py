from dotenv import load_dotenv
from flask import Flask

from app.database import *
from app.extensions import cors, database, marshmallow

from . import parameters
from . import paths


def _apply_parameteres(app: Flask) -> None:
    app.json.sort_keys = parameters.JSON_SORT_KEYS
    for key in dir(parameters):
        is_parameter = key.isupper()
        if is_parameter:
            parameter = getattr(parameters, key)
            app.config[key] = parameter


def _create_storage_dir() -> None:
    paths.STORAGE_DIR.mkdir(exist_ok=True)


def configure_enviroment(app: Flask) -> None:
    load_dotenv(paths.ENV_FILE)
    _apply_parameteres(app)
    _create_storage_dir()


def _configure_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def _configure_marshmallow(app: Flask) -> None:
    marshmallow.init_app(app)


def _configure_cors(app: Flask) -> None:
    cors.init_app(app, origins=parameters.ALLOWED_HOSTS)


def configure_extensions(app: Flask) -> None:
    _configure_database(app)
    _configure_marshmallow(app)
    _configure_cors(app)
