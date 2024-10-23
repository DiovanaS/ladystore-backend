from werkzeug.exceptions import Conflict, NotFound


class CustomerAlreadyExists(Conflict):
    def __init__(self) -> None:
        super().__init__(
            'A customer with the given CPF and/or email already exists.'
        )


class CustomerNotFound(NotFound):
    def __init__(self) -> None:
        super().__init__('Customer not found.')
