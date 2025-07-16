---
title: "cs143 01: Course Overview"
date: 2025-07-16
url: https://www.bilibili.com/video/BV1huRUYYEcw/
tags:
  - algorithm
---

## Intro to Compilers

编译器与解释器的区别。

起源：IBM 704。软件成本大大超过了硬件成本，需要加速软件开发。`speedcoding`->`fortran`，将公式转换成代码。

- fortran
  - 第一个编译器
  - 带来了大量的理论工作：编译理论是理论和实践的结合
  - 现代编译器维持了fortran的整体结构。

编译器结构

- Lexical Analysis: 词法分析
- Parsing: 语法分析
- Semantic Analysis: 语义分析
- Optimization: 优化
- Code Generation: 代码生成

## Structure of a Compiler

Lexical Analysis: divides program text into "words" or "tokens"

Parsing: Diagramming Sentences

Semantic Analysis: Semantic Checks

Optimization: Run faster and use less memory

Code Generation: Translation into another language

编译器都拥有这五个阶段，但是各个阶段的比例随时间发生了变化。

## The Economy of Programming Languages

- Why are there so many programming languages?
- Why are there new programming languages?
- What is a good programming languages?

不同的应用领域的需求不同。

培训程序员是编程语言的主要成本。因此越多人使用的编程语言变化的越慢，同时新的编程语言因为使用的人较少，所以变化的更快。

语言会在填补了空白时被接纳。

新语言会像旧语言，因为这样学习成本更低。

没有普遍的标准来评估编程语言。
