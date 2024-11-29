---
title: "Modern Template Metaprogramming: A Compendium, Part I By Walter E. Brown"
date: 2024-11-29
url: https://www.bilibili.com/video/BV12x411P7fU?p=57
tags:
---

ref:ACCU

Metaprogramming:

- write computer programs that write ot manipulate other programs(or themselves) as their data
- do work at compile time that other wise would otherwise be done at runtime

C++ template meta programming uses template instantiation to drive compile-time evaluation

template metaprogrammers exploit this machinery to improve source code flexibility and runtime performance

ref:Representative timings

when metaprogramming, runtime == compile-time

using constexpr to initialize.

constexpr function is like meta function, but meta function offer more tools

- public member type declarations
- public member data declarations
