from werkzeug.exceptions import NotFound


class ProductNotFound(NotFound):
    def __init__(self) -> None:
        super().__init__('Product not found.')
