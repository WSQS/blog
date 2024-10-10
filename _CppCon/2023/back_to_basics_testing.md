---
title: "Back to Basics: Testing by Phil Nash"
date: 2024-10-08
---

testing = operation + input values + expected output values

## Test

the testing pyramid

- Unit Tests : most test
- Integration Tests
- System Tests : hard to do, takes a lot of time.

## Unit Test

Unit test : Michael Feathers

A Set of Unit Testing Rules

run fast whenever we make our changes.

## Test Framework

`<cassert>`in std

pros

- no dependencies
- some useful output
- natural, familiar, syntax and usage

cons

- not enough feedback
- only console output
- no test name, groups/ suites
- aborts on first failure

84 cpp test frameworks

- CppUnit: first unit test framework in cpp
- CooUnitLite
- Boost.Test
- Google Test
- Catch/ Catch2
- doctest: consider performance
- UT

## Testing Best Practices

Unit Tests should:

- Run fast
- Be deterministic & reproducible
- Be self-contained/ isolated
- Be consistent & reliable
- Be obvious & self-documenting
- Be focused on one thing("single assert")
- Use public interfaces

All tests should:

- Be well named
- Provide clear and useful feedback
- Have a clear reason
- Have low cyclomatic complexity

Have a single "logical" assert

## The challenges & pitfalls of testing

- Flakey test: zero tolerance in unit test
- slow test
- brittle test: don't do this, delete the test
- hard to write: separate the code

## what next

- Get comfortable with the best practices
- Become familiar with the design principles
- pay attention to when testing is harding
- then consider trying TDD: red-green-refactor cycle

Design Principles: SOLID

See CppCon2020: Breaking Dependencies: The SOLID Principles, also The design of Everyday things.[note](../2020/breaking_dependencies_the_solid_principles.md)

ref:[levelofindrection.com/refs/testing.html](https://levelofindirection.com/refs/testing.html)
