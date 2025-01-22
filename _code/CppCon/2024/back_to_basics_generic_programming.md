---
title: "Back to Basics: Generic Programming by David Olsen"
date: 2025-01-20
url: https://www.bilibili.com/video/BV14YyfYhE3C?p=10
tags:
  - Cpp
  - Template
---

## Generic Programming

Generic Programming: Same code works on different, unrelated types

Static polymorphism

template

metaprogram

## Basics

template <template-parameters> declaration;

declaration:

- class/struct
- function
- type alias
- variable
- concept

Template definition should be in a header file.

Template Parameters

- Type template parameter: class|typename identifier
- Non-type template parameter(NTTP): type|auto identifier
- Template template parameter: template<template-parameters> class|typename identifier

re: godbolt.org

name is optional.

Variadic Template Parameters.

Define member function inline.

use a template

template-name<template-arguments>

Template argument kind must match template parameter kind

## Substitution & Instantiation

Substitution: Substitute template argument for template parameter

Instantiation: Full definition.

### Substitution

Substitution without instantiation in two contexts:

- Incomplete type is sufficient
- Class template partial specialization resolution

for function, substitution happens during overload resolution, check function signature. Then only the best match one instantiation.

### Instantiation

Class: Member functions are not instantiated until they are used.

Function

### SFINAE

Substitution Failure Is Not An Error

## Using Class Templates

clss-template-name<template-arguments>

Each instantiation is distinct and unrelated type.

## Using Function Templates

Let Compiler deduce the arguments.

## Constraints

Requirements on a template argument.

concepts and requires clauses.

`std::enable_if`

`std::is_intergral`

`std::integral`

ref: Back to Basics: Concepts in CppCon 2024

## Writing Class Templates

KISS Principle: Keep It Simple and Straightforward

Document Requirements

Member functions can have additional requirements

Specialization

Partial Specialization

Class and Variable template allowed specialization

`typename`

## Writing Function Templates

Deducible Template Parameters

Can't deduce the parent type of a function parameter

Avoid complicated overload sets

Avoid function templates that accept anything especially ones with common names.

Don't specialize function templates.

If you want a full specialization, create a non-template overload.

If you want a partial specialization, create template overload.

## Conclusion

re: Modern Template Metaprogramming: A Compendium [Markdown I](../2014/modern_template_metaprogramming_A_compendium_part_i.md) [html I](../2014/modern_template_metaprogramming_A_compendium_part_i.html) [Markdown II](../2014/modern_template_metaprogramming_A_compendium_part_ii.md)  [html II](../2014/modern_template_metaprogramming_A_compendium_part_ii.html)
