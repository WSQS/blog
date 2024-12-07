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
