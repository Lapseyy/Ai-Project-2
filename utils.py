def vector_add(a, b):
    """Component-wise addition of two vectors/tuples."""
    return tuple(x + y for x, y in zip(a, b)) 