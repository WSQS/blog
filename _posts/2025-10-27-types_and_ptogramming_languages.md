---
title: Types and Programming Languages
date: 2025-10-27
tags:
  - programming_language_theory
---

## Preface

### Goals

- 覆盖核心概念
- 使用主义
- 包含多种领域
- 易于使用
- 诚实。

### Structure

类型系统和逻辑的连接。

### Required Background

ref: Essentials of Programming Languages by Friedman, Wand, and Haynes (2001)

ref: Programming Language Pragmatics by Scott (1999)

ref: The Functional Approach to Programming by Cousineau and Mauny

### Course Outlines

ref: Communicating and Mobile Systems: the Pi-Calculus Milner Robin

### Exercises

### Typographic Conventions

### Electronic Resources

ref:[book's website](http://www.cis.upenn.edu/~bcpierce/tapl)

### Acknowledgments

## Introduction

### Types in Computer Science

类型系统是一种轻量的形式方法。

A type system is a tractable syntactic method for proving the absence of certain program behaviors by classifying phrases according to the kinds of values they compute.

类型系统最先在数学理论中出现。

计算机对类型系统的研究分为实践派和理论派。

类型系统是对运行时值的一种近似。

静态类型和动态类型。

静态类型检查是保守的，会拒绝一些实际上能正常运行的程序的。类型系统研究的主要目的就是允许更多的程序被类型化，也就是让类型系统拥有更强的表达能力。

类型系统只能判断一部分问题，另一些问题只能留到运行时进行检查。

这些可以被处理的问题是`run-time type errors`，不同的语言，不同的类型系统能够处理的运行时类型错误都不同。

类型检查器是编译器的一部分。程序员可以添加类型注解，这样类型检查器就变成了一个证明检查器。

### What Type Systems Are Good For

#### Detecting Errors

静态类型检查的优点是允许提前检查一些编程报错。除了一些简单的错误，还有一些复杂的类型错误，这些能力取决于类型系统本身的表达能力。

有力的类型系统会提供多种技巧来将结构的信息编码进类型的。

#### Abstraction

分类接口和实现。

#### Documentation

类型及接口可以成为一种文档。

#### Language Safety

安全语言是一个有争议的概念，不同语言社区对它的理解都不同。

静态类型安全和安全语言两者不相关。静态类型语言的安全也需要通过动态检查来达成。

#### Efficiency

静态类型可以避免动态类型检查。

#### Further Applications

计算机和网络安全。

类型推断技术可以用于其他领域。

自动理论证明。

数据库。

计算语言学。

### Type Systems and Language Design

向一个不包含类型系统的语言嵌入类型是复杂的。类型系统是语言设计的核心。

### Capsule History

### Related Reading

## Mathematical Preliminaries

必要时来查阅。

### Sets, Relations, and Functions

## Untyped Arithmetic Expressions

### Introduction

BNF语法格式。

`metavariable`占位符。

括号是为了一致性。

### Syntax

格式：归纳定义。

格式：推导规则。

格式：具体规则

前两个视角描述了集合是满足给定封闭性性质的最小集合，是一种归纳定义。第三种视角描述了集合是如何构造出来的。
