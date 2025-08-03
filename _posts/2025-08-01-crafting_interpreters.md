---
title: Crafting Interpreters
date: 2025-08-01
url: https://craftinginterpreters.com/
tags:
  - algorithm
---

## Introduction

逻辑证明与类型系统之间存在一一对应关系。

### Why Learn This Stuff?

#### Little languages are everywhere

每一个成功的通用语言都有上千的亲戚。对应的还有DSL(domain-specific language)。因此可能会遇到对某一个特别的语言，缺少解析器或某些工具的情况，这时候就需要自己手动实现。

#### Languages are great exercise

实现一个编程语言是对程序员编程技巧真正的考验。

#### One more reason

破除对实现编译器的恐惧。

compiler-compiler: lax, yacc, bison

DESIGN NOTE: WHATʼS IN A NAME?

- It isnʼt in use.
- Itʼs easy to pronounce.
- Itʼs distinct enough to search for.
- It doesnʼt have negative connotations across a number of cultures.

## A Map of the Territory

区分语言与语言的实现。

### The Parts of a Language

编程语言的路径存在差异但是整体相似。

#### Scanning

词法分析。也就是lexing或lexical analysis。

#### Parsing

语法分析。构建语法树(AST)。同时也需要报告语法错误。

#### Static analysis

连接起引用与实现或定义。如果语言是静态类型的，那么这时会进行类型检查。

对于语义分析的内容，有时会被存在AST中，有时会被放在查找表(symbol table)中，有时会放入新的数据结构中。这是 front end ，随后还有 middle end 和 back end。

#### Intermediate representations

front end 关心源语言， back end 关心程序运行的最终架构。IR是前后两个部分的接口。

#### Optimization

优化的一个典型例子是常量折叠(constant folding)。

#### Code generation

back end 从这里开始。可以生成真实CPU的指令，也可以生成虚拟CPU的指令(bytecode)。

#### Virtual machine

对于bytecode，可以再在此基础上翻译成真实cpu的指令，或者可以基于虚拟机实现，使用虚拟机会更慢，但是更为通用。

#### Runtime

运行时需要进行GC或性能追踪等操作。

### Shortcuts and Alternate Routes

#### Single-pass compilers

不需要以上步骤，直接通过语法分析生成代码。这需要对语言进行限制。因为历史原因，c和pascal存在这样的约束。

#### Tree-walk interpreters

将代码解析成AST之后，直接开始运行。第一个编译器例子就是如此。

#### Transpilers

将代码翻译成其他的高级语言而不是机器码。

#### Just-in-time compilation

在运行时将bytecode编译为指令。

### Compilers and Interpreters

编译：将一种源语言翻译为更低级的语言

解释：接收源代码，并立即执行

对于CPython来说，编译和解释是都进行的。

## The Lox Language

### Hello, Lox

Lox的语法是类c的。

### A High-Level Language

Lox类似于JavaScript, Scheme and Lua。

- Dynamic typing
- Automatic memory management(GC)

ref: [A Unified Theory of Garbage Collection](https://courses.cs.washington.edu/courses/cse590p/05au/p50-bacon.pdf)

### Data Types

- Booleans
- Numbers: Double Only
- Strings
- Nil

### Expressions

- Arithmetic
- Comparison and equality
- Logical operators
- Precedence and grouping

### Statements

Expression主要用于产出数值，而Statement主要用于产生效果。

expression statement和block。

### Variable

`var`

### Control Flow

`if else` `while` `for`

### Functions

`fun`

- argument:调用函数时传入的值
- parameter:函数内拿到的值

#### Closures

函数也是类型。也可以定义本地函数。闭包。

ref:[The Next 700 Programming Languages](https://homepages.inf.ed.ac.uk/wadler/papers/papers-we-love/landin-next-700.pdf)

### Classes

#### Why might any language want to be object oriented?

用对象将基本数据类型组装起来。

#### Classed or prototypes

Class-based language基于实例和类型。

Prototype-based language只有对象没有类型。

#### Classes in Lox

类型实例本身也是一个类，实际上和函数是一样的。

#### Instantiation and initialization

`this` `init`

#### Inheritance

`<` 构造函数也会被继承。

### The Standard Library

`print` `clock`

DESIGN NOTE: EXPRESSIONS AND STATEMENTS

存在一些只有expression的语言。

## Scanning

### The Interpreter Framework

使用UNIX`sysexits.h`作为返回值标准。

支持给定文件，也支持交互式的命令(REPL, Read Evaluate Print Loop)。

#### Error handling

对于真正可用的编程语言来说，错误处理是关键的。错误处理要引导用户。错误处理在整个编译器的实现中都需要被考虑。

应该要区分产生错误的代码和报告错误的代码。其实也就是提供接口。

### Lexemes and Tokens

#### Token type

词法分析需要对Token分类，例如，保留字。

#### Literal value

#### Location information

将位置信息也放在Token中。可以放行号，也可以放在文件当中的偏移。

### Regular Languages and Expressions

可以使用正则表达式表示lexeme或者lexical grammar。

ref: Compilers: Principles, Techniques, and Tools(the dragon book)

`lex` `flex`

### The Scanner Class

### Recognizing Lexemes

从单个字符开始。

#### Lexical errors

对未识别的字符进行报错。

#### Operators

添加两个字符的运算符。

### Longer Lexemes

对于注释需要处理。

#### String literals

Lox支持多行字符串。因此在处理字符串字面量时也需要更新行号。我觉得应该在消费掉字符时自动的对行号进行检查。对于字符字面量，Lox并不进行转义。

#### Number literals

对数字字面量，需要再多看一个。

### Reserved Words and Identifiers

maximal munch

DESIGN NOTE: IMPLICIT SEMICOLONS

去掉分号，但是要涉及足够好的规则来判断一行结束了。

### Representing Code

Chomsky hierarchy

#### Context-Free Grammars
