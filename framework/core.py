_registered_tests = []


def test(func):
    """
    decorator to register all tests to the private
    _registered_tests array
    """
    _registered_tests.append(func)
    print("test?")
    return func


def get_tests():
    """
    returns all the registered tests
    """
    return _registered_tests