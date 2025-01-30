---
title: "Back to Basics: Almost Always Vector by Kevin Carpenter"
date: 2025-01-22
url: https://www.bilibili.com/video/BV14YyfYhE3C?p=14
tags:
  - Cpp
---

re: Data Structures and Algorithms with the C++ STL by JOHN FARRIER [markdown](../../cpp/data_structures_and_algorithms_with_the_cpp_stl.md) [html](../../cpp/data_structures_and_algorithms_with_the_cpp_stl.html)

ref: paper: Generic Dynamic Arrays in C++

## The Basics

DynArray to Vector

32 member functions

Creating std::vector

- empty and pushback
- initializer list
- construct with a size
- construct with a size and a default

Access data

- `operator[]`
- at: give range check

.data for c library

## Memory Management

stack vs heap

stack limit in size

stack is fast automatic predictable locality and safety

heap is flexible large lifetime sharing

`std::vector` don't need c style reallocation

reserve to prevent allocations, reverse is shrink_to_fit

ref: Getting Allocators out of Our Way in CppCon 2019

## Iterator

`begin()`

Iterator gives guard rails to the pointer.

`rbeind()`

range based for loop do copy.

invalidating iterators

ref: [C++ STL Write an iterator from scratch On Youtube](https://youtu.be/Fv8oj8EdssY?si=QRmDCTDYGeWBQtFZ)

## Algorithms

Unary Predicates

`std::find_if`

re: nlohmann::json

Choose std::list when you need frequent insertion/deletions at arbitrary positions.

Choose std::deque when you need efficient insertions/removals at both the front and back.

Vector

- Efficiency
- Practically
- Versatility
