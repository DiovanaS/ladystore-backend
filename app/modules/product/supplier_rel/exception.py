from werkzeug.exceptions import Conflict, NotFound


class SupplierRelAlreadyExists(Conflict):
    def __init__(self) -> None:
        super().__init__('Supplier relation already exists.')


class SupplierRelNotFound(NotFound):
    def __init__(self) -> None:
        super().__init__('Supplier relation not found.')
