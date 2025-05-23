_registered_tests = [] # list of tests

# decorator function, Object-Oriented Programming Principle, that takes all
# tests from test_samples ( qais code )
def test(func):
    """
    decorator to register all tests to the private
    _registered_tests array
    """
    _registered_tests.append(func)
    return func


# will return all the tests that we got with "test" decorator up
def get_tests():
    """
    returns all the registered tests
    """
    return _registered_tests