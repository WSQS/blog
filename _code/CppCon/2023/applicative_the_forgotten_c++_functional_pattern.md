---
title: "Applicative: The Forgotten C++ Functional Pattern by Ben Deane"
date: 2024-10-31
url: https://www.bilibili.com/video/BV1BC4y1R7iL?p=43
---

> I hope that by the end of the talk some of you will look at your code with new eyes.

## One

Applicative: a programming Pattern that fits in functors and monads

Functors: a parameterized type(a class template) of one(free) argument.

fmap

Monad: a parameterized type(a class template) of one(free) argument.

bind join

returns a functorial value

fmap + join = bind

std::optional

transform in Cpp23 this is fmap

and_then is bind

Applicative

## Two

ref: Functional Programming: Functors and Mondas CppCon2015

ref: Monoids, Monads and Applicative Functors: Repeated Software Patterns C++Now 2015 && CppCon 2020
