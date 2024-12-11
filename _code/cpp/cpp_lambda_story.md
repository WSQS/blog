---
title: C++ Lambda Story
date: 2024-12-09
tags:
  - Cpp
---

ref:[List of online C++ compilers](https://github.com/arnemertz/online-compilers)

these is good:[paiza.io](https://paiza.io/en/projects/new?language=cpp) [geeksforgeeks](http://code.geeksforgeeks.org/)

## Lambdas in C++98/03

### Callable Objects in C++98/03

callable object is only function pointer and functor at that time.

### What is a "Functor"

functor is "function object class type".

ref:[functors](https://bartoszmilewski.com/2015/01/20/functors/)

> A functor is a mapping between categories. Given two categories, C and D, a functor F maps objects in C to objects in D — it’s a function on objects.

ref:Functional Programming in C++

> A class template F is a functor if it has a transform (or map) function defined on it.

Two rules: identity and composition.

### Issues with Function Object Class Types

The problem of functor is the definition and the usage maybe faraway in code. Because in C++98/03, you couldn’t instantiate a template with a local type.

onr of the solutions is to prepare a set of helpers functor.

### Composing with Functional Helpers

In `<functional>`, there are a lot of helper functions.

ref:boost library

### Motivation for a New Feature
