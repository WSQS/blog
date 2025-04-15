---
title: C++ Core Guidelines
date: 2025-04-04
url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines
tags:
  - Cpp
  - multi_thread
---

## Abstract

代码的静态安全性。

代码的可读性。

## Introduction

通用规则和专门规则结合。

## Philosophy

### Express ideas directly in code

ref: [gsl](https://github.com/microsoft/GSL)

for for index using `std::ptrdiff_t` or `gsl::index`.

### Write in ISO Standard C++

Limit the influence of compiler extension.

Don't accept extension.

### Express intent

Say what should be done, rather than just how it should be done.

`std::span`

### Ideally, a program should be statically type safe

- union -> variant
- minimize cast
- span for array decay
- narrow or `gsl::narrow` cast fot narrowing conversion

- Prefer compile-time checking to run-time checking
  `std::span` and look for run-time checks for range violations.
- What cannot be checked at compile time should be checkable at run time
- Catch run-time errors early
  Don’t repeatedly check the same value.
- 
