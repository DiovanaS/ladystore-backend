from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


api = Api()
cors = CORS()
database = SQLAlchemy()
