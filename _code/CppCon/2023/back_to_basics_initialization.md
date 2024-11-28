---
title: "Back to Basics: Initialization by Ben Saks"
date: 2024-11-24
url: https://www.bilibili.com/video/BV1BC4y1R7iL?p=42
tags:
  - Cpp
---

Initialization in C++ can be quite complex

history:c, c++03, modern c++

## Initialization rules from c

Scalars are simple values.

Aggregates are object that are made up of smaller pieces. Union is Aggregates.

Scalars can be initialize with a single value. It's copy-initialization.

aggregate-initialization. It's like `{...}`

Aggregate also can do copy-initialization.

For a object without ana explicit initializer

- object has static or thread storage duration, it has zero-initialized.
- Otherwise the object is left uninitialized
- If the member not include in brace-enclosed list, it will zero-initialized.

## On the origins of constructors

class invariant need class constructor.

A class type is an aggregate if it has

- no user-declared constructors
- no private or protected non-static data members
- no base classes
- no virtual functions

direct-initialization is in parentheses.

C++ strives to treat user-defined types and built-in type uniformly.

direct-initialization can call copy constructor, but it's not copy-initialization.

Distinguish between initialization and assignment.

Assignment is the only way to call operator= member function.

Explicit

TODO:Not finished
