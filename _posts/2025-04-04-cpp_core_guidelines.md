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

### Catch run-time errors early

- Do range-checking early.
- Don’t repeatedly check the same value.
- Don't excess checking.

- Don't leak any resources
  RAII

- on't waste time ot space
  使用前缀自增，避免后缀自增产生的临时变量。
- Prefer immutable data to mutable data
- Encapsulate messy constructs, rather than spreading through the code
  使用或者实现那些关键抽象，避免反复完成底层代码。
  抽象复杂的指针操作。
- Use supporting tools as appropriate
  使用静态分析工具、并发工具、测试工具。
  不要构建过于复杂的工具链，这会增加移植的难度。
- Use support libraries as appropriate
  建议使用应用领域的库。
  std 和 gsl

## Interfaces

### Make Interfaces explicit


