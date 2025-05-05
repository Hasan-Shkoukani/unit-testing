import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tests.test_samples
from framework.core import get_tests

def testSummary(t: int, p: int, f: int):
    print(">>> Test Summary:")
    print(f">>> Total Tests: {t}")
    print(f">>> Total Passed Tests: {p}")
    print(f">>> Total Failed Tests: {f}")


def runTests():

    tests = get_tests()
    total_tests = len(tests)
    passed, failed = 0,0

    for test in tests:
        try:
            test()
            print(f"{test.__name__}\n>>> PASS <<<")
            passed += 1
        except AssertionError as e:
            print(f"{test.__name__}\n>>> FAIL: {str(e)} <<<")
            failed += 1
    
    testSummary(total_tests, passed, failed)

    return ">>> TESTING COMPLETED <<<"

if __name__ == "__main__":
    runTests()