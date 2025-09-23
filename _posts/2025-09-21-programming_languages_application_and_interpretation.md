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

实现一个计算器。它的输入是`Exp`，输出是一个`Number`。

递归处理AST。并用`type-case`对两种类型进行处理。

### Testing the Evaluator

使用test方法对求值器进行测试。

增加标记`(print-only-errors #true)`来让测试只输出失败的条目。

### Some Subtler Tests

浮点数的加法需要特殊处理。

ref: [浮点数加法说明](https://0.30000000000000004.com/)

需要确认主语言的语义是我们想要的，例如浮点数计算这种。

## Parsing: From Source to ASTs

### The Problem

现有的直接写AST的方式的表面语法太复杂了。需要一个更方便的表层语法。Parsing是将输入语法转换成AST。

选择使用Racket的括号语法进行表示。

### S-Expressions

这样的语法是`s-expressions`。plait提供了`s-exp`相关的函数来进行读取和判断。

### Primus Inter Parsers

Parser是将s-expressions转换成Exp。

`test/exn`进行测试之后，会对抛出的异常是否包含字串来看是否显示这个报错。

## Evaluating Conditionals

要支持语法表达式。需要：

- 拓展数据类型支持表示条件
- 拓展求值器来处理条件表达式
- 拓展解析器来生成新的表示

### Extending the AST

### Extending the Calculator

### The Design Space of Conditionals

条件表达式也有不同的设计。

- test-expression支持的类型。必须是布尔值，又或者是有一些值表示true，另一些表示false，其中的值的定义又是各不相同的，这部分应该尽可能简单，比如Scheme，Ruby和Lua，都只有少数几个值是false。
- 分支的类型。是statement还是expression。
- expression的值的类型对静态类型语言来说需要两个分支的值是一样的，对动态类型语言没有这样的限制。

### Using Truthy-Falsy Values

Rackte中只有`#false`是非。

### Implementing Conditionals

先简单实现一个if0，也就是只看test-expression的值是不是0。

解释器的一部分工作可以复用宿主语言的功能，例如if，也可以在实现中引入一些差异。

### Adding Booleans

一个成熟的语言需要多种类型。

### The Value Datatype

增加一个类型Value，用于表示求值器可以得到的结果。

### Updating the Evaluator

需要处理非数字相加的情况。增加了一个函数add来处理这种情况。

## Evaluating Local Binding

Binding: 将名字和值关联起来。

Local: 意味着只有程序的一些区域可以访问这个值，其他区域无法使用这个值。

### A syntax for Local Binding

使用BNF(Backus-Naur Form)来标记语法。

BNF区分终止符和非终止符。终止符需要被`<>`包裹。

### The Meaning of Local Binding

`let1`赋值。

### Static Scoping

SMoL的重要概念：静态作用域，变量的绑定是基于其位置的，而不是运行程序的顺序。

控制流控制绑定是动态绑定的变体。动态绑定是毋庸置疑的编程语言的错误设计。

动态语义的python论文：

ref： [Python: The Full Monty: A Tested Semantics for the Python Programming Language](https://cs.brown.edu/~sk/Publications/Papers/Published/pmmwplck-python-full-monty/)

静态作用域允许IDE重命名变量。

静态作用域比起动态作用域实现起来会更加复杂一些。

### An Evaluator for Local Binding

变量需要被替换。

### Caching Substitution

但是替换作为一种实现是低效的，每一个变量的绑定都需要和程序大小线性相关的时间去进行替换。更可行的方法是将变量存储在一个被称为环境的数据结构中，其中存储了变量名和其值，这实际上是一个键值对。

尽管我们没有使用替换，但是我们希望程序运行的结果和替换是一致的。

环境使用哈希表来实现。
