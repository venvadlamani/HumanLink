from exceptions import Exception


class ServiceError(Exception):
    """Base class for service exceptions."""
    message = 'Unknown service exception'

    def __init__(self, msg=None):
        super(Exception, self).__init__(msg if msg else self.message)


class PermissionError(ServiceError):
    """Permission denied exception."""
    message = 'Permission denied.'


class NotFoundError(ServiceError):
    """Something not found exception."""
    message = 'Resource not found.'
