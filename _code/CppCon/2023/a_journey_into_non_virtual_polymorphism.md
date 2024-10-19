---
title: A Journey into Non Virtual Polymorphism Rud Merriam
date: 2024-10-17
url:  https://www.bilibili.com/video/BV1BC4y1R7iL?p=40
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

Too difficult to determine data types

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

Template with template pack

Moving call operators into the structures.

CppInsights

Lambda capture adds flexibility.

- Usable a Polymorphism invokable
- Can return values as well as output parameters
- calling signatures can be different
  - different number of parameters and returns
  - take care not to dupilcate signatures.

the Overload Idiom can work well with std::variant

## std::tuple

A container like type.

Can get type with index or type.

`std::apply` `std::make_tuple`

`tuple_cat`can work with`std::array`, can replace for in some placek.

- `std::tuple`is container like
- `std::apply`is loop like
- Overload Idiom works with`std::apply`

## Curiously Recurring Template Pattern(CRTP)

C++23: Explicit Object Parameter

- The CRTP is an abstrction
- CRTP defines an interface for related types
- Remember CRTP does not directly-provide compile time Polymorphism
- The addition of concepts will change CRTP.
