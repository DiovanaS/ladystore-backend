from flask import Response, jsonify, make_response
from http import HTTPStatus
from typing import Union

from app.database import Model, Models
from app.extensions import marshmallow


Schema = marshmallow.Schema


class ResponseFacade():
    def as_message(
        self,
        message: str,
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return make_response(
            jsonify({'message': message}),
            status
        )

    def as_schema(
        self,
        schema: Schema,
        model_or_models: Union[Model, Models],
        status: HTTPStatus = HTTPStatus.OK
    ) -> Response:
        return make_response(
            schema.jsonify(model_or_models),
            status
        )


response = ResponseFacade()
