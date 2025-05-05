![What-is-the-best-framework-for-Unit-Testing](https://github.com/user-attachments/assets/b346ba98-f47e-4aa2-921d-f0ae75f3f233)

# Unit Testing Framework

A lightweight, extensible unit testing framework built with Python, designed for simplicity and flexibility. It provides a set of custom assertion classes, decorators, and a test runner for effective testing.

## Features

- **Custom Assertions**: Grouped by comparison, truthiness, identity, collections, exceptions, and timing.
- **Test Runner**: A simple test runner that discovers and runs tests with clear, colorful output.
- **Modular Design**: Easy to extend and modify for custom use cases.
- **Performance Testing**: Supports timing assertions to ensure code performance.

## Project Structure

unit-testing/  
├── framework/  
│   ├── core.py         # Registers and provides test functions  
│   ├── assertions.py   # Custom assertion logic grouped by purpose  
│   └── runner.py       # Main test runner  
├── tests/  
│   └── test_samples.py # Example tests using all assertion types  
└── README.md           # Project documentation  

## Installation

Clone the repository:

```
git clone https://github.com/Hasan-Shkoukani/unit-testing.git  
cd unit-testing
```

## Usage
### Running Tests
To run the tests, simply execute the test runner:


The test runner will discover all tests in the tests/ directory and display the results in the terminal with color-coded output.

## Example Test
Here's an example of how to write tests using the framework:

```
from framework.assertions import Assert

def test_addition():
    result = 2 + 2
    Assert.equal(result, 4)

def test_is_true():
    Assert.is_true(True)

def test_performance():
    Assert.less_than_execution_time(lambda: [x**2 for x in range(1000)], 0.1)
```

## Creating Custom Assertions
You can create your own assertions by extending the Assertion base class. Each assertion is designed to be intuitive and easy to use.

## Contributing
Feel free to fork the repository, create a branch, and submit a pull request for new features, improvements, or bug fixes.

## Note
This framework is submitted to Dr Amr Abdelbari in Near East University for Software Testing ( SWE302 ) Final Project
