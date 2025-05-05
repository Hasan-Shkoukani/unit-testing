import time


# COMPARISON FAMILY
class Comparison:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def assertEqual(self):
        if self.a != self.b:
            raise AssertionError(f"{self.a} is not equal to {self.b}")
            
    def assertNotEqual(self):
        if self.a == self.b:
            raise AssertionError(f"{self.a} is equal to {self.b}")
            
    def assertGreater(self):
        if self.a <= self.b:
            raise AssertionError(f"{self.b} is greater than or equal to {self.a}")
    
    def assertGreaterEqual(self):
        if self.a < self.b:
            raise AssertionError(f"{self.b} is greater than {self.a}")
        
    def assertLess(self):
        if self.a >= self.b:
            raise AssertionError(f"{self.b} is less than or equal to {self.a}")
    
    def assertLessEqual(self):
        if self.a > self.b:
            raise AssertionError(f"{self.b} is less than {self.a}")

# TRUTHINESS FAMILY   
class Truthiness:

    def __init__(self, value):
        self.value = value

    def assertTrue(self):
        if not self.value:
            raise AssertionError(f"{self.value} is not a True boolean value")
        
    def assertFalse(self):
        if self.value:
            raise AssertionError(f"{self.value} is a True boolean value")
        
    def assertNone(self):
        if not (self.value is None):
            raise AssertionError(f"{self.value} is not None")
    
    def assertNotNone(self):
        if self.value is None:
            raise AssertionError(f"{self.value} is None")

# IDENTIFICATION FAMILY       
class Identification:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def assertIs(self):
        if not (self.a is self.b):
            raise AssertionError(f"the objects are not equal to each other")
        
    def assertIsNot(self):
        if (self.a is self.b):
            raise AssertionError(f"the objects are equal to each other")
        
    def assertIsInstanceOf(self):
        if not (isinstance(self.a, self.b)):
            raise AssertionError(f"{self.a} is not an instance of class {self.b}")
        
    def assertIsNotInstanceOf(self):
        if (isinstance(self.a, self.b)):
            raise AssertionError(f"{self.a} is an instance of class {self.b}")

# COLLECTIONS FAMILY     
class Collections:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def assertIn(self):
        if not (self.a in self.b):
            raise AssertionError(f"{self.a} is not in {self.b}")
        
    def assertNotIn(self):
        if (self.a in self.b):
            raise AssertionError(f"{self.a} is in {self.b}")
    
    def countEqual(self):
        if len(self.a) != len(self.b):
            raise AssertionError(f"length of {self.a} is not equal to the length of {self.b}")
        
        for elem in set(self.a + self.b):
            if elem not in self.a or elem not in self.b:
                raise AssertionError(f"The collections are not equal")
            if self.a.count(elem) != self.b.count(elem):
                raise AssertionError(f"The collections are not equal")
            
    def assertListEqual(self):
        if self.a != self.b:
            raise AssertionError("the lists are not equal!")
    
    def assertTupleEqual(self):
        if self.a != self.b:
            raise AssertionError("the tuples are not equal!")

    def assertSetEqual(self):
            if self.a != self.b:
                raise AssertionError("the sets are not equal!")

    def assertDictEqual(self):
                if self.a != self.b:
                    raise AssertionError("the dictionaries are not equal!")

# EXCEPTIONS FAMILY              
class Exceptions:

    def __init__(self, e, func, *args, **kwargs):
        self.e = e
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def assertRaises(self):
        try:
            self.func(*self.args, **self.kwargs)
        except Exception as e:
            if not isinstance(e, self.e):
                raise AssertionError(f"expected: {self.e}, got {type(e)}")
        else:
            raise AssertionError("no error was raised")
    
# TIMING FAMILY
class Timing:

    def __init__(self, seconds, func, *args, **kwargs):
        self.seconds = seconds
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def assertRunsUnder(self):
        start = time.perf_counter()
        self.func(*self.args, **self.kwargs)
        end = time.perf_counter()
        duration = end - start
        if duration > self.seconds:
            raise AssertionError(f"The function took longer than {self.seconds} seconds to execute")
        
    def assertTakesAtleast(self):
        start = time.perf_counter()
        self.func(*self.args, **self.kwargs)
        end = time.perf_counter()
        duration = end - start
        if duration < self.seconds:
            raise AssertionError(f"The function took less than {self.seconds} seconds to execute")