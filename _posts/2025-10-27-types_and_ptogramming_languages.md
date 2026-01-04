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

### Induction on Terms

因为集合T的归纳特性，所以可以给出归纳定义的函数。

项上归纳原理，对深度、长度和结构归纳。

### Semantic Styles

定义语言的语义。

三种语义形式化的方式：

- 运算语义
- 指称语义，Domain Theory，将递归的语义映射到数学结构中。
- 公理语义：将规则本身作为语言的定义。

运算语义早期被认为是后两者的中间状态，但是随着编程语言发展速度的加快，简单直接的运算语义变得更流行。书中只使用运算语义。

### Evaluation

对布尔值的运算语义。evaluation relation，求值关系，表达式的简化过程。

if表达式的求值策略，先求guard。

对给定的语句，求值的顺序是固定的。

normal form：不能再应用求值关系的表达式。

多步求值关系，经过零或多步求值关系可以达到的表达式。

一个表达式最终得到的normal form是只有一个的。涉及到停机问题。

一个表达式存在normal form。

增加代数的运算语义。

stuck: 是normal form但是却不是value。其实也就是运行时异常。

定义异常的值来给出更明确的报错，这和正常求值的逻辑是一致的。

### Notes

## An ML Implementation of Arithmetic Expressions

基于OCaml实现。

### Syntax

ast的节点开头包含一个info，描述了节点的来源。

`rec`关键字说明函数调用是递归的。

### Evaluation

对于无法使用求值规则的情况，抛出异常。

对变量的类型进行更严格的限制。

### The Rest of the Story

对AST求值只是编译器的一个步骤。

## The Untyped Lambda-Calculus

语言可以拆分成核心和语法糖。

lambda-calculus可以作为核心语言，只包含函数定义和函数应用。类似的还有pi-calculus和object-calculus。这些运算可以互相迁移。

ref: [Church, Alonzo. The Calculi of Lambda Conversion. Princeton University Press, 1941.](https://archive.org/details/the-calculi-of-lambda-conversion-couverture-alonzo-church-princeton-university-p)

丰富lambda-calculus，对各种特性增加语法糖，增加复杂的特性。对核心语言的拓展通常也会涉及类型系统的拓展。

### Basics

计算或函数抽象是所有编程语言的本质核心特性。

函数求值的直接理解是函数替换。

lambda-calculus只有三种语法，变量、函数声明和函数应用。

#### Abstract and Concrete Syntax

两层语法结构：准确语法和抽象语法。

从准确语法转换为抽象语法可以通过lexer和parser。

#### Variables and Metavariables

#### Scope

绑定变量，函数的形参，自由变量，函数形参之外的变量。

无自由变量的表达式封闭表达式，或组合子(combinators),不依赖外部变量的函数。

#### Operational Semantics

纯粹的lambda-calculus的计算就只是将函数应用于参数。也就是将所有形参的自由变量都替换为实参。

$(\lambda x. t_{12})t_2$被称作可约式(reducible expression ,redex)重写redex的规则是beta-reduction。

求值策略。

- `full beta-reduction`: 所有redex都可以被先求值
- `normal order strategy`: 最左侧最外侧的redex被先求值，求值过程是确定的
- `call by name strategy`: 与`normal order strategy`类似，但是不能直接化简函数中的内容，Haskell采用变体`call by need`
- `call by value strategy`: 只有最外侧的redex可以被先求值，只有redex的参数是值了才能被求值。

求值策略对类型系统影响较小。

### Programming in the Lambda-Calculus

#### Multiple Arguments

通过柯里化，来通过单参数函数实现多参数函数

#### Church Booleans

`tru`和`fls`的定义:

$$
tru = \lambda t. \lambda f. t;\\
fls = \lambda t. \lambda f. f;
$$

#### Pairs

基于布尔值，可以实现pair。

#### Church Numerals

数字是0的后继。表示一个函数执行多次某个操作。

$scc = \lambda_n. \lambda_s.\lambda_z. s (n\ s\ z);$

$plus = \lambda_m.\lambda_n.\lambda_s.\lambda_z.m\ s(n\ s\ z);$

$times = \lambda_m.\lambda_n.m(plus\ n) c_0;$

$iszro = \lambda_m.m(\lambda_x.fls) tru;$

$$
zz = pair\ c_0\ c_0;\\
ss = \lambda_p.pair(snd\ p)(plus c_1(snd p));
prd = \lambda_m.fst(m\ ss\ zz);
$$

$nil = \lambda c.\lambda n. n$

$cons = \lambda h.\lambda t.\lambda c.\lambda n. c\ h(t\ c\ n);$

$isnil = \lambda t. t (\lambda x.\lambda y.fls) tru;$

$head = \lambda t. t (\lambda x.\lambda y.x) nil;$

#### Enriching the Calculus

$\lambda$NB加入代数和布尔表达式的lambda-calculus。

$\lambda$NB中对代数和布尔都存在两种实现，可以相互转换。

Church encoding的问题是因为`call by value strategy`,代数运算的求值会被延迟，而原始类型则没有这个问题。

#### Recursion

有的表达式不是normal形式，但是无法被求值为normal形式，而是一直递归，这是`diverge`。

`fixed-point combinator`实现递归函数$fix = \lambda f.(\lambda x.f(\lambda y. x\ x\ y))(\lambda x.f(\lambda y.x\ x\ y));$

#### Representation

Church数表示了原始数吗？Church数和真实的数没有可以被观测到的差异。

### Formalities

只关注lambda-calculus。

#### Syntax

term的三种组成，本身是变量，是函数声明，是函数应用。

#### Substitution

替换的两种定义。一种更为直观一种对特定的ML实现更为方便。

区分自由变量和绑定变量。

静态作用域。需要进行`capture-avoiding substitution`。对于重名的情况，应该进行`alpha-conversion`，对绑定变量进行重命名。

绑定变量重命名的语句是一致的。

#### Operational Semantics

计算顺序。

### Notes

ref: [Böhm, Corrado and Alessandro Berarducci. Automatic synthesis of typed Λ-programs on term algebras. Theoretical Computer Science, 39(2–3):135–154, August 1985.](https://www.sciencedirect.com/science/article/pii/0304397585901355)

## Nameless Representation of Terms

变量的表示。

- 符号表示（依赖Barendregt convention）
- 显式替换（explicit substitutions）
- combinatory logic可以完全不需要变量

这些都是基于风格和性能的可选项。

本书基于索引来定位变量。
