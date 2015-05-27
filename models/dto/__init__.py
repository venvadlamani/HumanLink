def map_props(target, source, properties):
    """Maps the given property values of source object to target object.
    If the target object already has the property, that property is skipped.

    Example:
        given:
            target: A (A.hello == '00')
            source: B (B.hi == '11', B.hello == '22', B.foo == '33'),
            properties: ['hi', 'hello']
        after the function:
            A: A.hi == '11', A.hello == '00'
            B: not changed

    :param target: an instance of the target object.
    :param source: an instance of the source object.
    :param properties: list of properties to map
    :return: (None)
    """
    for k in properties:
        if not hasattr(source, k) or getattr(target, k, None) is not None:
            continue
        v = getattr(source, k)
        setattr(target, k, v)
