def map_props(target, source, properties):
    """Maps the given property values of target object to source object.

    Example:
        given:
            source = A,
            target = B (B.hi == '11', B.hello == '22'),
            properties = ['hi']
        after the function:
            A: A.hi == '11'
            B: not changed

    :param source: an instance of target object.
    :param target: an instance of source object.
    :param properties: list of properties to map
    :return: (None)
    """
    for k in properties:
        if not hasattr(source, k):
            continue
        v = getattr(source, k)
        setattr(target, k, v)
