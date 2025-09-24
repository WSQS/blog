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

## Evaluating Functions

### Functions in the Language

top-level函数、非top-level函数和匿名函数。

### Extending the Representation

函数不需要默认有名字，函数名可以由`let1`赋值。

函数需要定义和使用两种表示：introduction和elimination。

### Evaluating Functions

函数本身也需要一种值表示，包括了形参和表达式。

side-effect: 在函数体之外可观测到的系统的变化

pure function: 对同一个输入，输出都是相同的，并且没有副作用的函数

### Extending Values

需要做的是：

- 求函数值
- 求变量值
- 检查函数类型
- 将实参赋值给形参
- 求值函数体

### Stepping Back

到目前为止已经实现了一个完整的编程语言。

### Extending Tests

函数中捕获的变量的作用域会在被调用时覆盖掉，因此会将语言变成动态作用域的语言。

### Return to Static Scope

Environment的实现实际上时对替换的一种优化，所以还是要回到替换上来看。

通过函数内部存储一个它创建时的环境来解决这个问题。 这样的函数也就是闭包。

closed function: 没有未绑定变量的函数。

闭包不是closed function。

ref: A Brief, Incomplete, and Mostly Wrong History of Programming Languages

函数参数和表达式不应该在闭包环境中被求值。

### A Subtle Test

## How SMoL Becomes Large

处理AST的程序可以输出各种不同的结果，解释器输出数值，编译器输出程序，类型检查器使出类型正确性，但是它们的基本结构都是一致的。

### Redundancy in Languages

for和while是重复的。

### Desugaring

区分核心语言和表层语言。表层语言增加了语法糖，各种不同的结构，但是可以被转换成同一种核心语言的结构，转换的程序是desugarer。

在报错时，为了报错的正确，所以需要对语法糖进行特殊处理。

一种常规的desugar的方法是将AST重写成子集的AST。在括号语法的语言中，parse分为两个部分，一个是粗糙的括号语法，另一个是精细的AST，前者很适合用来做语法糖的展开和重写。这通常被称为宏系统，在解析之前，将源码重写为源码。绝大多数语言都有语法糖，但是只有很少一部分语言拥有宏系统，让程序员拥有重写程序的能力。

### Macros By Example

改为使用racket`#lang racket`。

### A New Conditional

实现一个更严格版本的if函数，在进行if之间先进行类型检查，只支持布尔值。

问题在于racket是立即求值的，所以strict-if的两个分支都会被执行。

使用宏可以避免这个问题。

DrRacket的Macro Stepper支持逐步显示宏是如何展开的。

### Local Binding

`let1`无法被函数实现，因为每一个参数都会被先求值。

special forms: 在语言中新加入的语法

可以将变量展开成函数，将变量的值变为函数的参数，let1的body变为函数的body。

left-left-lambda: 立即被执行的匿名函数。在javascript中被称为IIFE(Immediately Invoked Function Expression)。

### Binding More Locals

可变参数宏。使用`...`表示可变参数。

### Multi-Armed Conditionals

`...`表示0或更多个参数，所以，可以递归的调用宏。支持模式匹配。

## More on Macros

### A Definitional Convenience

可以使用符号`_`来避免重复使用宏。

### Name Capture

宏中的变量并不只是名字，其中还记录了绑定信息。这可以避免动态作用域。这一特性是hygiene。

### A Truthy/Falsy Idiom

对于if，应该如实返回值，而不只是true。

### A Macro Definition Hazard

问题在于，对于上面直接返回值的情况，会导致值被计算了两次，这对于有副作用的表达式是有问题的。需要将对应的值，使用lat保存下来。

### Back to Hygiene

hygiene对局部变量也是起效的。

### Generalizing Macros

实现一个orN。

## A Standard Model of Objects

对象可以看作是闭包的推广。

对象可以被作为结构或者是作为语法糖。

前者需要：

- 进行额外的记录，实现比较琐碎
- 解释器会变得越来越庞大
- 难以编写实例程序和测试

使用语法糖和宏来实现对象。
