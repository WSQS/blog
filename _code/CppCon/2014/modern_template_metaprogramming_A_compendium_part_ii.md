---
title: "Modern Template Metaprogramming: A Compendium, Part II By Walter E. Brown"
date: 2024-11-30
url: https://www.bilibili.com/video/BV12x411P7fU?p=60
tags:
  - Cpp
  - Template
---

pre part:[markdown](./modern_template_metaprogramming_A_compendium_part_i.md) [html](./modern_template_metaprogramming_A_compendium_part_i.html)

## Using inheritance + specialization together

Example: Given a type, is it a void type?

```cpp
// primary template
template<class T> struct is_void:false_type{};
template<> struct is_void<void>:true_type{};
template<> struct is_void<void const>:true_type{};
```

It's in std, and also `std::is_same`.

## Forwarding/ delegating to other metafunctions

Using key words `using`.

## Using a parameter pack in a metafunction

```cpp
template<class T, class... P0toN>
struct is_one_of;
template<class T>
struct is_one_of<T>:false_type{};
template<class T, class... P0toN>
struct is_one_of<class T,class T,P1toN...>:true_type{};
struct is_one_of<T>:false_type{};
template<class T, class... P0toN>
struct is_one_of<class T,class P0,P1toN...>:is_one_of<T,P1toN...>{};
```

## Unevaluated operands

`sizeof`,`typeid`,`decltype`,`noexcept`never evaluated, not even at compile time.

- Implies that no code is generated(in these contexts) for such operand expression(no run time cost)
- Only a declaration, not a definition to use a function's or object's name in these contexts.

An unevaluated function call can usefully map a type to another

```cpp
decltype(foo(std::declval<T>()))
```

This just like `std::result_of()`.

- the unevaluated call `std::declval<T>()`is declared to give a rvalue result of type T(`std::declval<T&>()` gives lvalue)

## Proposed new type trait void_t

```cpp
template<class ...>
using void_t = void;
```

- Acts as a metafunction call that maps any well-formed types into the predictable type void
  - Initially an implementation detail while proposing SFINAE-friendly version of common-type and iterator_traits

default argument is essential.

ref:document N3911 for void_t

Name is the problem.
