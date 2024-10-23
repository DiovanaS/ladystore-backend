from marshmallow import ValidationError
from typing import Tuple
from werkzeug.exceptions import (
    BadRequest,
    HTTPException,
    InternalServerError
)


def _is_http_exception(e: Exception) -> bool:
    return isinstance(e, HTTPException)


def _is_validation_error(e: Exception) -> bool:
    return type(e) is ValidationError


def get_details(e: Exception) -> Tuple[int, str]:
    if _is_http_exception(e):
        return (e.code, e.description)
    if _is_validation_error(e):
        return (BadRequest.code, e.messages)
    return (
        InternalServerError.code,
        'An internal server error occurred.'
    )
