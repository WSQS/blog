---
title: Automatic synthesis of typed Λ-programs on term algebras
date: 2025-11-05
tags:
  - programming_language_theory
---

## Introduction and summary

代数和$\Lambda$系统地双向对应。

基于Church encoding，Curry-Church的类型还是太局限了，哥德尔在之后发展了有限类型函数理论。

等到Girard提出了二阶类型理论才有一个足够强大的lambda-calculus来表达自由代数。

Curry–Howard同构意味着类型与逻辑之间的一致性。

## Heterogeneous algebras

### Basic definitions

代数是载体和运算组成的二元组。

只有一个载体的代数是`homogeneous algebra`，有多个载体的被称为`heterogeneous algebra`。

### Term algebras

项代数中的一致就是形式完全一致，运算符号，参数格式和对应位置的参数都相同。

生成元: 不是任何基本运算的输出的元素。也就是参数。

### Data systems and data structures

data system: 没有载体既包含参数，又包含非参数，并且只有有限的载体和基础预算的代数。其中的载体被称作数据结构，数据结构也有参数的和非参数的。
