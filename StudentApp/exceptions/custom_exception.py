class CustomExceptions(Exception):
    """Error passing query params"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidRequestException(CustomExceptions):

    def __init__(self, message):
        self.message = message
        self.status = 400
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'