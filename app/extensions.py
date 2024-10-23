from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


cors = CORS()
database = SQLAlchemy()
marshmallow = Marshmallow()
