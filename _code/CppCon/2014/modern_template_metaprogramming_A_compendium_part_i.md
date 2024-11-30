---
title: "Modern Template Metaprogramming: A Compendium, Part I By Walter E. Brown"
date: 2024-11-29
url: https://www.bilibili.com/video/BV12x411P7fU?p=57
tags:
  - Cpp
  - Template
---
- [Compile-time recursion with specialization as base](#compile-time-recursion-with-specialization-as-base)
- [A metafunction can take a type as parameter/argument](#a-metafunction-can-take-a-type-as-parameterargument)
- [A metafunction can also produce a type as its result](#a-metafunction-can-also-produce-a-type-as-its-result)
- [Compile-time decision-making](#compile-time-decision-making)
- [A single-type variation on conditional](#a-single-type-variation-on-conditional)
- [SFINAE applies during implicit template instantiation](#sfinae-applies-during-implicit-template-instantiation)
- [A taste of the future](#a-taste-of-the-future)

ref:ACCU

meta programming:

- write computer programs that write ot manipulate other programs(or themselves) as their data
- do work at compile time that other wise would otherwise be done at runtime

C++ template meta programming uses template instantiation to drive compile-time evaluation

template meta programmers exploit this machinery to improve source code flexibility and runtime performance

ref:Representative timings

when meta programming, runtime == compile-time

using constexpr to initialize.

constexpr function is like meta function, but meta function offer more tools

- public member type declarations
- public member data declarations, each is initialized via a constant expression.
- public member function declaration adn constexpr member function definitions
- public member templates, static_asserts, and more.

## Compile-time recursion with specialization as base

call the metafunction inside the metafunction.

I think it's really like haskell which has pattern matching. Just using partial specialization to define the edge case.

## A metafunction can take a type as parameter/argument

constexpr can't do this.

such as sizeof function.

## A metafunction can also produce a type as its result

such as remove a type's const-qualification.

convention: A metafunction with a type result aliases that result to type.

Can now apply the convention via inheritance.

## Compile-time decision-making

`std::conditional` to select one of two types. And a convenience call alias is `std::conditional_t`.

## A single-type variation on conditional

If true, use the given type; if false use no type at all.

`std::enable_if`，it only sometimes an error: SFINAE.

## SFINAE applies during implicit template instantiation

During template instantiation, the compiler will:

- Obtain(or figure out)the template arguments:
  - Taken verbatim if explicitly supplied at template's point of use
  - Else deduced from function arguments at point of call.
  - Else taken from the declaration's default template arguments.
- Replace each template parameter, throughout the template, by its corresponding template argument.
  - If these steps produce well-formed code, the instantiation succeeds
  - If the resulting code is ill-formed, it is considered not viable(due to substitution failure) and is silently discarded.

`std::is_integral` and `std::is_floating_point`.

## A taste of the future

Concepts will take the place of SFINAE

ref:Generic Programming with Concepts Lite in CppCon 2014

concepts has a very solid mathematical foundation, abstract algebra create by Emmy Noether.

convention: A metafunction with a value result has a static constexpr member, value, giving its result, and a few convenience member types and constexpr functions.

`std::integral_constant`

```cpp
template<bool b>
using bool_constant = integral_constant<bool,b>
```

```cpp
is_void<T>::value
bool(is_void<T>{}) // cast member function
is_void<T>{}()
is_void_v<Y>
```

next part:[markdown](./modern_template_metaprogramming_A_compendium_part_ii.md) [html](./modern_template_metaprogramming_A_compendium_part_ii.html)
