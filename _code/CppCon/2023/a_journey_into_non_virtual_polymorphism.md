---
title: A Journey into Non Virtual Polymorphism Rud Merriam
date: 2024-10-17
---

Polymorphism(geek): many forms

Polymorphism: type based dispatch.

Problem is how to get variable.

Virtual functions are not bad.

- Standard template library:std::any, std::variant, std::tuple.
- Overloaded functions and operators
- Auto parameters and Template
- Curiously Recurring Template Pattern(CRTP)

We need a polymorphic type and polymorphic invocation.

## std::any 

A Type that can contain any type chanllenging as a Polymorphic variable.

- std::any is allowed to dynamically allocate memory
  - id may use Small Buffer Optimization(SBO)
- Use `std::any_cast<type>`to access value
  - No easy way to determine type in the variable.
  - No easy way to invoke function with Type.
  - Users must know what types might be used.

using `std::type_index()`

## std:variant

Type safe Union

- Types enumrated in template parameter list
- Values are stored in the variant
  - No dynamic memory allocation
  - Types may dynamically allocate memory
- Straightforward access to Values
  - Uses data type or position in template pack

`std::get<>()`

Immediate call of lambda

`.index()`returns position of data type in template pack.

`std::get_if<>()`returns value* or nullptr.

`std::visit(func,o)`determine type of o and calls the function`func(cast<T>(o))`


## The Overload Idiom

A Polymorphic Invokable with lambdas all the way down.

