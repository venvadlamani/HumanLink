"""Various asserts and boolean checks."""
import services.exp as exp


def valid_id_type(obj):
    if not is_valid_id_type(obj):
        raise exp.UnexpectedTypeExp('int or long', type(obj))


def type_of(ins, cls):
    if not is_type_of(ins, cls):
        raise exp.UnexpectedTypeExp(cls, type(ins))


def is_valid_id_type(obj):
    return isinstance(obj, (int, long))


def is_type_of(ins, cls):
    return isinstance(ins, cls)
