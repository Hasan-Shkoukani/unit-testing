###Unit Testing Framework

A lightweight, extensible unit testing framework built with Python, designed for simplicity and flexibility. It provides a set of custom assertion classes, decorators, and a test runner for effective testing.

Features
Custom Assertions: Grouped by comparison, truthiness, identity, collections, exceptions, and timing.

Test Runner: A simple test runner that discovers and runs tests with clear, colorful output.

Modular Design: Easy to extend and modify for custom use cases.

Performance Testing: Supports timing assertions to ensure code performance.

##Project Structure

unit-testing/
├── framework/
│   ├── core.py         # Registers and provides test functions
│   ├── assertions.py   # Custom assertion logic grouped by purpose
│   └── runner.py       # Main test runner
├── tests/
│   └── test_samples.py # Example tests using all assertion types
└── README.md           # Project documentation
