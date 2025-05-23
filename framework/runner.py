import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
load_dotenv()

import tests.test_samples
from framework.core import get_tests
from framework.ai_helper import explain_failure  


# this function will give you the summary of our testing system
# here we check the amount of tests that passed, and failed
def testSummary(t: int, p: int, f: int):
    print(">>> Test Summary:")
    print(f">>> Total Tests: {t}")
    print(f">>> Total Passed Tests: {p}")
    print(f">>> Total Failed Tests: {f}")


# this function will run the tests one by one, and will classify them as "pass" and "fail"
# "fail" will be fixed with ( ai code ) 
def runTests():
    tests = get_tests()
    total_tests = len(tests)
    passed, failed = 0, 0

    # we iterate the tests one by one, and assert them
    for test in tests:
        try:
            test()
            print(f"{test.__name__}\n>>> ✅ PASS <<<")
            passed += 1
        except AssertionError as e:
            print(f"{test.__name__}\n>>> ❌ FAIL: {str(e)} <<<")
            print("💡 AI Açıklaması:")
            print(explain_failure(test.__name__, str(e)))
            failed += 1

    testSummary(total_tests, passed, failed)
    return ">>> TESTING COMPLETED <<<"

#driver code
if __name__ == "__main__":
    runTests()
