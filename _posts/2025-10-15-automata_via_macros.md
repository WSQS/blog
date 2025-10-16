---
title: "Automata via Macros"
date: 2025-10-15
url: https://cs.brown.edu/~sk/Publications/Papers/Published/sk-automata-macros/
tags:
  - compile
  - scheme
  - programming language theory
  - Shriram Krishnamurthi
---

## Introduction

使用领域特定的结构拓展语言，近期的例子是轻量化的程序生成技术，最著名的就是C++的模板。

Lisp社区对宏的研究是比较深刻的。对Scheme来说，关键不是在特性的基础上增加特性，而是增加哪些移除弱点和限制所必需的特性。

Scheme添加了少量的特性和强大的宏系统，使得创建高阶的特定领域原语和通用原语成为可能。

宏常见的用法：

- 提供装饰
- 引入绑定结构
- 实现控制运算符，可以改变运算的顺序
- 定义数据语言

宏可以控制将一份数据描述用函数还是用结构体表示。

宏缺乏合适复杂度的例子。

Scheme成功的原因：

- 一组非常强大的核心特性
- 对表达式极少的限制
- 核心特性相对高角度的正交性

## About the Code in This Paper

Scheme和它的宏系统教程参见:

ref: [The Scheme Programming Language Second Edition](https://www.scheme.com/tspl2d/)

## Automata as Macros

将自动机用数据结构表示。并通过基于当前状态查找可能的变化并在变换中查找下一个状态来完成状态机的运作。

自动机的实现本质：

- 基于当前状态快速的条件分配来决定下一个状态
- 每一个状态都应该能快速的访问
- 状态转换的代价应该低

对应的，`fast conditional dispatch`意味着条件表达式，`rapid state access`意味着指针，`quick state transition`意味着函数调用。

对应的状态是函数，状态跳转通过函数调用来实现。

第一种方式实现了一个interpreter。对应的特点是：

- 输出是一个结果，而不是另一个程序
- 通过数据结构处理程序的源码，处理了所有输入
- 它消费程序和特定的输入

第二种方式是编译的结果。

第二种方式有两个未解决的问题，效率和准确性，前者和函数调用的成本有关，而后者在自动机变得愈发复杂时变得难以保证。这是需要的是一个真正的编译器生成编译结果，这就是宏的表现。

### Concision
