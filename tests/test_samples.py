import time
from framework.assertions import Comparison, Truthiness, Identification, Collections, Exceptions, Timing
from framework.core import test

# COMPARISON FAMILY TESTS
# Decorator to register tests into our framework
@test
def test_comparison_equal():
    comparison = Comparison(1, 1)
    comparison.assertEqual()

@test
def test_comparison_not_equal():
    comparison = Comparison(1, 2)
    comparison.assertNotEqual()

@test
def test_comparison_greater():
    comparison = Comparison(3, 2)
    comparison.assertGreater()

@test
def test_comparison_greater_equal():
    comparison = Comparison(3, 3)
    comparison.assertGreaterEqual()

@test
def test_comparison_less():
    comparison = Comparison(2, 3)
    comparison.assertLess()

@test
def test_comparison_less_equal():
    comparison = Comparison(2, 3)
    comparison.assertLessEqual()

# TRUTHINESS FAMILY TESTS
@test
def test_truthiness_true():
    truthiness = Truthiness(True)
    truthiness.assertTrue()

@test
def test_truthiness_false():
    truthiness = Truthiness(False)
    truthiness.assertFalse()

@test
def test_truthiness_none():
    truthiness = Truthiness(None)
    truthiness.assertNone()

@test
def test_truthiness_not_none():
    truthiness = Truthiness(1)
    truthiness.assertNotNone()

# IDENTIFICATION FAMILY TESTS
@test
def test_identification_is():
    a = [1]
    b = a
    identification = Identification(a, b)
    identification.assertIs()

@test
def test_identification_is_not():
    a = [1]
    b = [1]
    identification = Identification(a, b)
    identification.assertIsNot()

@test
def test_identification_instance_of():
    identification = Identification("hello", str)
    identification.assertIsInstanceOf()

@test
def test_identification_not_instance_of():
    identification = Identification(1, str)
    identification.assertIsNotInstanceOf()

# COLLECTIONS FAMILY TESTS
@test
def test_collections_in():
    collections = Collections(1, [1, 2, 3])
    collections.assertIn()

@test
def test_collections_not_in():
    collections = Collections(4, [1, 2, 3])
    collections.assertNotIn()

@test
def test_collections_count_equal():
    collections = Collections([1, 2, 3], [3, 2, 1])
    collections.countEqual()

@test
def test_collections_list_equal():
    collections = Collections([1, 2, 3], [1, 2, 3])
    collections.assertListEqual()

@test
def test_collections_tuple_equal():
    collections = Collections((1, 2, 3), (1, 2, 3))
    collections.assertTupleEqual()

@test
def test_collections_set_equal():
    collections = Collections({1, 2, 3}, {1, 2, 3})
    collections.assertSetEqual()

@test
def test_collections_dict_equal():
    collections = Collections({"a": 1}, {"a": 1})
    collections.assertDictEqual()

# EXCEPTIONS FAMILY TESTS
@test
def test_exceptions_raises():
    def test_func():
        raise ValueError("An error occurred")
    
    exceptions = Exceptions(ValueError, test_func)
    exceptions.assertRaises()

@test
def test_exceptions_raises_no_error():
    def test_func():
        pass
    
    exceptions = Exceptions(ValueError, test_func)
    exceptions.assertRaises()

# TIMING FAMILY TESTS
@test
def test_timing_runs_under():
    def slow_func():
        time.sleep(0.5)
    
    timing = Timing(1, slow_func)
    timing.assertRunsUnder()

@test
def test_timing_runs_over():
    def slow_func():
        time.sleep(1.5)
    
    timing = Timing(1, slow_func)
    timing.assertRunsUnder()

@test
def test_timing_takes_at_least():
    def slow_func():
        time.sleep(2)
    
    timing = Timing(1, slow_func)
    timing.assertTakesAtleast()

@test
def test_timing_takes_less_than():
    def slow_func():
        time.sleep(0.5)
    
    timing = Timing(1, slow_func)
    timing.assertTakesAtleast()