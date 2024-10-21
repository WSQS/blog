---
title: Back to Basics： Functions in C++ by Mike Shah
date: 2024-10-20
url: https://www.bilibili.com/video/BV1BC4y1R7iL?p=15
---

ref:[web](http://mshah.io/)

Functions in programing languages are used to express math and more exciting ideas.

Functions are a way to group related code.

- Some functions purely run a routine of code -- no return value.
- Some functions compute a new value from 0 or more inputs.
- Some functions mutate a given input and/or output.

std::optional means 0 or 1 value are returned.

- Separating functions into separate files
  - reuse your functions in other projects
  - hide your implementation details from users
  - protentially speed up compilation
  - utilize only the functionality you need by breaking up source in to modules of related functions.

objdump

static function to hide function from user.

using namespace to grout functions together.

C++20 include Modules.

- Virtual functionality
- Vtable

ref: back to bask: object-oriented programming in cppcon 2019&2021

ref: object-oriented programming in c++ in cppcon 2023

ref: Shah's youtube video.

constexpr: compute at compile time.

ref:[CppCoreGuidelines](https://isocpp.github.io/CppCoreGuidelines/)

pure function: same input same output.

std::span can both hold the pointer and the length.

ref: Back to Basics: Lambfas from scratch in cppcon 2019

ref: Back to Basics: Lambdas in cppcon 2021

ref: C++ Lambda Idioms in cppcon 2022

`std::function`

Coroutines

ref: Coroutines from scratch in cppcon 2022

function should only do one thing.
