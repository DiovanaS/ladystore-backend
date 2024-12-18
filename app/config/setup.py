from dotenv import load_dotenv
from flask import Flask

from app.database import *
from app.extension import api, cors, database
from app.resource import customer_ns, product_ns, supplier_ns, stock_ns, sales_ns, financial_ns

from . import parameter, path


def _apply_parameteres(app: Flask) -> None:
    app.json.sort_keys = parameter.JSON_SORT_KEYS
    for key in dir(parameter):
        is_parameter = key.isupper()
        if is_parameter:
            app.config[key] = getattr(parameter, key)


def _create_storage_dir() -> None:
    path.STORAGE_DIR.mkdir(exist_ok=True)


def setup_enviroment(app: Flask) -> None:
    load_dotenv(path.ENV_FILE)
    _apply_parameteres(app)
    _create_storage_dir()


def _setup_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def _setup_api(app: Flask) -> None:
    api.init_app(
        app,
        title='LadyStore Server',
        description=(
            'Server that meets the demands of LadyStore, in internal '
            'activities such as managing customers and suppliers, as '
            'well as recording sales.'
        )
    )
    api.add_namespace(customer_ns)
    api.add_namespace(product_ns)
    api.add_namespace(supplier_ns)
    api.add_namespace(stock_ns)
    api.add_namespace(sales_ns)
    api.add_namespace(financial_ns)


def _setup_cors(app: Flask) -> None:
    cors.init_app(app, resources={r"/*": {"origins": "http://localhost:5173", "methods": ["GET", "POST", "DELETE", "PUT", "PATCH", "OPTIONS"]}})


def setup_extensions(app: Flask) -> None:
    _setup_database(app)
    _setup_api(app)
    _setup_cors(app)
