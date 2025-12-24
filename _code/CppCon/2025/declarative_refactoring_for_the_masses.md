---
title: "Declarative Refactoring for the Masses by Andy Soffer"
date: 2025-12-23
url: https://www.bilibili.com/video/BV1RMB5BoE4f/
tags:
  - Cpp
---

Declarative: what should be done

Refactoring: Modifying a program's implementation

for the Masses: Usable by any C++ engineer

C++ has indeed become too "expert friendly". -- Bjarne Stroustrup Nov. 2006

## Declarative style

- Unspecified control flow. Regular expression.
- Describe a solution's constraints. SQL query.

Benefits

- Easier to reason about
- Less error-prone

Drawbacks

- Implementation difficulty
- Tend to be more restrictive

## Declarative Refactoring

- Describe what your looking for, not how to find it.
- Describe what to replace it with, not how to next munge.
- Make description language as intuitive as possible.
- Access to the type system.
- Access to the preprocessor.

## Clang-Tidy

ref: How to Build Your First C++ Automated Refactoring Tool in CppCon 2023

Benefits:

- Checks and Fixes.
- Free.
- Can write you own.

Pain points:

- Distribution
- Maintenance
- Clang AST matcher are complicated
  - Clang's implementation details matter
  - Language details must be handled explicitly
  - Standard library details matter

## Vibe Tidying
