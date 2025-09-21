---
title: "Programming Languages: Application and Interpretation"
date: 2025-09-21
url: https://www.plai.org
tags:
  - algorithm
  - compile
---

## Preface

### Why Study Programming Languages?

- 编程语言是人类创造的最美好和强大的对象
- 让我们准确的表达我们的想法，并利用计算机表达执行想法
- 编程语言是终极的人机交互的接口
- 在工业生产中十分重要
- 具象化了一种新知识: procedural epistemology 过程化认识论
- 允许我们证明关于方法和限制的表述

ref: Structure and Interpreteation of Computer Programs

### The Target Audience

本书的目标读者是剩下的百分之九十的学生。

### Why a Third Edition

[作者的研究](https://cs.brown.edu/~sk/Publications/Papers/Published/)

因为虚拟机的多样和鲁棒，例如Erlang，Java，JavaScript和Racket,使得创建一门新语言变得简单。

### Structuring Our Study

编程语言是特性的组合。理解特性和组装方式是理解语言的重要方法。

ref： [说明该观点的论文](https://cs.brown.edu/~sk/Publications/Papers/Published/sk-teach-pl-post-linnaean/)

本书围绕一个核心概念SMoL(the Standead Model of Languages)。

流行语言有着共同的计算核心: 安全的运行时系统、自动内存管理、立即执行表达式、第一类词法作用域函数、一阶可修改变量、第一类可变结构。这些是理解更复杂语言机制的基础。

同一个特性也存在不同的变体，可以使用mystery language方法来研究这些不同变体。基于相同的语法，但是特性的不同表现。

ref [mystery language的论文](https://cs.brown.edu/~sk/Publications/Papers/Published/pkf-teach-pl-exp-adv-think/)

另一个核心概念是SImPl(the Standard Implementation Plan)，将语言表示为抽象语法树，并使用代数数据类型来表示抽象语法树。

### Equipment for Learning

本书是CSCI 1730课程的一部分。

ref: [CSCI 1730](https://cs.brown.edu/courses/csci1730/)

本书大量基于Racket。Racket的能力在于可以定义新的语言。

ref: [A Programmable Programming Language](https://cs.brown.edu/~sk/Publications/Papers/Published/fffkbmt-programmable-prog-lang/)

ref: [From Macros to DSLs: The Evolution of Racket](https://cs.brown.edu/~sk/Publications/Papers/Published/cffk-macros-to-dsls/)

## Teach Yourself SMoL

ref: [SMoL Tutor](https://smol-tutor.xyz/tutor/)

## Evaluation on Paper

### Evaluators

两种求值器：解释器和编译器

解释器的优点在于：

- 实现一个简单的解释器比起一个编译器更容易
- debug一个解释器比debug一个编译器更容易

### Terminology

一个语言并不会指定是解释型语言或是编译型语言，这两种说法是无意义的。JIT的存在更是模糊了这一界限。

### Simulating an Interpreter by Hand

术语：形参是函数定义中的参数，实参是函数调用时传入的参数。

术语：eager evaluation立即求值，lazy evaluation延迟求值。

SMoL是立即求值的。

SMoL是顺序求值的，同时是从左向右求值的。

### Substitution

实现求值器的方法：

- 找到一种方式表示源码
- 寻找下一个用于需要求值的表达式
- 进行文本替换来得到一个新程序
- 持续替换知道只剩下值

这是一个缓慢的方法。

## Representing Arithmetic

先简单实现一个加法求值器。

### Representing Programs

如何表示程序。不管是源码还是二进制指令都是对程序的表示。

实际上需要先考虑表面语法(surface syntax)。

需要的是一种与表面语法无关的对程序的表达。

### Abstract Syntax

通过AST,可以忽略那些表面语法。

### Representing Abstract Syntax

本书使用Racket的plait来实现。

在我们的AST中，叶子是数字，节点是运算。

## Evaluating Arithmetic

### Defining the Evaluator

实现一个计算器。
