# 🧪 Python Unit Testing Framework

A lightweight, colorful, and extensible unit testing framework built from scratch using pure Python.  
Supports structured assertions across **comparison**, **truthiness**, **identity**, **collections**, **exceptions**, and **timing**.

---

## 🌈 Features

- 🔍 **Test Discovery** via `@test` decorator
- 🎨 **Colorful Terminal Output**
- 🧱 **Modular Assertion Classes**
- ⚡ **Performance Testing**
- 🚫 **Exception Handling**
- 🔧 **Minimal Setup**

---

## 📁 Project Structure

unit-testing/
├── framework/
│ ├── core.py # Registers and provides test functions
│ ├── assertions.py # Custom assertion logic grouped by purpose
│ └── runner.py # Main test runner
├── tests/
│ └── test_samples.py # Example tests using all assertion types
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

```bash
git clone https://github.com/Hasan-Shkoukani/unit-testing.git
cd unit-testing
python3 framework/runner.py
```
🔬 Assertion Families
🔁 Comparison
python
Copy
Edit
Comparison(a, b).assertEqual()
Comparison(a, b).assertGreater()
✅ Truthiness
python
Copy
Edit
Truthiness(val).assertTrue()
Truthiness(val).assertNone()
🧩 Identification
python
Copy
Edit
Identification(a, b).assertIs()
Identification(obj, cls).assertIsInstanceOf()
📚 Collections
python
Copy
Edit
Collections(val, collection).assertIn()
Collections(list1, list2).countEqual()
💥 Exceptions
python
Copy
Edit
Exceptions(ExpectedError, func, *args).assertRaises()
⏱️ Timing
python
Copy
Edit
Timing(seconds, func, *args).assertRunsUnder()
Timing(seconds, func, *args).assertTakesAtleast()
🧪 Sample Test
python
Copy
Edit
from framework.core import test
from framework.assertions import Comparison

@test
def test_numbers_equal():
    Comparison(5, 5).assertEqual()
📊 Output Example
test_numbers_equal
>>> ✅ PASS <<<

test_numbers_not_equal
>>> ❌ FAIL: 5 is not equal to 10 <<<

>>> Test Summary:
>>> Total Tests: 2
>>> Total Passed Tests: 1
>>> Total Failed Tests: 1
>>> TESTING COMPLETED <<<
🧱 Built With
Python standard library

No external dependencies

📜 License
MIT License

👨‍💻 Author
Made with ❤️ by Hasan Shkoukani

