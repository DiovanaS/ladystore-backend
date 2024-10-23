from werkzeug.exceptions import Conflict, NotFound


class SupplierAlreadyExists(Conflict):
    def __init__(self) -> None:
        super().__init__(
            'A supplier with the given CNPJ already exists.'
        )


class SupplierNotFound(NotFound):
    def __init__(self) -> None:
        super().__init__('Supplier not found.')
