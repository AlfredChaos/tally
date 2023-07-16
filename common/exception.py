
class InvalidParamsException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ObjectNotExistException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    

class ObjectDeleteException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    

class ObjectUpdateException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message