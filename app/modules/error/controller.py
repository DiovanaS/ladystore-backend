from http import HTTPStatus
from app.facades import response

from . import service as error_service, error


@error.app_errorhandler(Exception)
def handle_exception(e: Exception):
    code, description = error_service.get_details(e)
    return response.as_message(description, HTTPStatus(code))
