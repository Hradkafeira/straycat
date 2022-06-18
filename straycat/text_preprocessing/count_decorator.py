def counted(self):
    """decorator function to counting instantiation of object

    Returns:
        int: the number of object that instantiated

    """
    def wrapped(*args, **kwargs):
        """ inner function """
        wrapped.calls += 1
        return self(*args, **kwargs)
    wrapped.calls = 0
    return wrapped
