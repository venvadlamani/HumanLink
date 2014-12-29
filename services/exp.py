from exceptions import Exception


class ServiceExp(Exception):
    """Base class for service exceptions."""
    message = 'Unknown service exception'

    def __init__(self, msg=None):
        super(ServiceExp, self).__init__()
        self.message = msg if msg else self.message


class BadRequestExp(ServiceExp):
    """Bad request exception.

    Use cases:
        - Unexpected behavior from the service.
    """
    message = 'Bad request.'


class PermissionExp(ServiceExp):
    """Permission denied exception.

    Use cases:
        - The user is not allowed to perform a specific action.
    """
    message = 'Permission denied.'


class NotFoundExp(ServiceExp):
    """Something not found exception.

    Use cases:
        - The requested resource not found.
    """
    message = 'Resource not found.'


class ValueExp(ServiceExp):
    """Unexpected or bad value exception.

    Use cases:
        - Input validations.
    """
    message = 'Unexpected or bad value.'


class UnexpectedTypeExp(ServiceExp):
    """Unexpected object type exception.

    Use cases:
        - Expected int as an arg, but received a str.
    """
    message = 'Unexpected type.'
    message_format = 'Unexpected type. Expected: %s, Actual: %s'

    def __init__(self, exp, act):
        self.message = self.message_format % (exp, act)
