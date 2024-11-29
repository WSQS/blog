---
title: How and When to write a C++ Template by Roth Michaels
date: 2024-11-26
url: https://www.bilibili.com/video/BV1opSnYHEd4/
tags:
  - Cpp
  - Template
---

Templates: recipes for generating specializations.

Types of templates

- class templates
- function templates
- alias templates(C++11)
- variable templates(C++17)
- lambda templates(C++20)
- Concepts(C++20)

ref:Templates made easy with C++20 by Roth Michaels in CppOnSea 2023

Reason: don't repeat yourself.

class is equal to typename.

- Specialization
  - Instantiation
    - Implicit Instantiation
    - Explicit Instantiation
  - Explicit Specialization

`std::vector<bool>` is Explicit specialization

auto

alias templates: using.

ref:modern Template Metaprogramming

variable templates

Default template parameters

Variadic templates

```cpp
template <class... Types>
class variant;
```

NTTP: None type template parameter

Template template parameters

the necessary of `typename`.

For Specialize functions, try to use overloads. Overloads is before specialization. But It can work in one interface.

For SFINAE(Substitution Failure Is Not An Error), use concepts instead.

SFINAE `std::void_t<decltype()>`

template and alternatives: template, variants, virtual interfaces

template can work with lambdas, also can use std::function

ref:std::forward

ref:std::any_of

Can put template in two header file, with and without definition.

using [cppinsights](https://cppinsights.io) to learn template and lambda.
