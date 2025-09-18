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

正则表达式难以处理多层嵌套的情况。上下文无关文法(CFG, context-free grammar)。

#### Rules for grammars

生成式。基于规则生成。terminal与nonterminal。描述规则的格式:BNF(Backus-Naur form)。

#### Enhancing our notation

支持`|`、`()`、`*`、`+`、`?`

#### A Grammar for Lox expression

目前只考虑这些表达式：

- Literals
- Unary expressions
- Binary expressions
- Parentheses

#### Implementing Syntax Tree

AST。

在java中使用继承进行表示。

#### Disoriented objects

AST只负责存放数据，并没有处理的方法。它是语法分析和解释器之间通信的桥梁。

#### Metaprogramming the trees

代码生成。

### Working with Trees

不同类型的表达式会执行不同的操作。

ref: Design Patterns: Elements of Reusable Object-Oriented Software

#### The expression problem

表达式的复杂度在哪里展开？

面向对象、函数式。对于添加类型和添加方法，总是一个容易一个困难，这就是`expression problem`。

#### The Visitor pattern

Visitor模式是在面向对象中实现函数式。

要添加新的方法就不需要更改原本的类型了。

#### Visitors for expressions

### A(Not Very) Pretty Printer

## Parsing Expressions

你不需要学完所有传统理论，也能写出非常高质量的解析器。

### Ambiguity and the Parsing Game

语法可能存在歧义。

- Precedence
- Associativity: left-associative right-associative

区分不同的优先级类型。低优先级类型的可以转换为高优先级类型的。

left-recursive对一些解析会存在问题。通过调整表达式，去除left-recursive的结构。

### Recursive Descent Parsing

使用的算法：recursive descent。

recursive descent是最简洁的办法，同时高效、鲁棒并且支持复杂的报错。例如gcc使用的就是这种方法。

recursive descent 被认为是一个top-down parser。它可以直接将表达式翻译成函数。

#### The parser class

每一条语法都成为parser类的一个方法。我理解就是通过栈来模拟嵌套关系。

### Syntax Errors

编译器有两项工作：编译和报告错误。

- Hard requirements
  - Detect and report the error
  - Avoid crashing or hanging
- More requirements
  - Be fast
  - Report as many distinct error as there are
  - Minimize cascaded errors

error recovery

#### Panic mode error recovery

从报错开始丢弃synchronization之前的所有token。

#### Entering panic mode

#### Synchronizing a recursive descent parser

使用分号来判断是否能够进行synchronization。

### Wiring up the Parser

DESIGN NOTE: LOGIC VERSUS HISTORY

位操作符的优先级。好的设计可以加速用户的学习，但是适应传统也可以吸引用户。

## Evaluating Expressions

对于jlox，通过执行语法树来运行。

两个问题：我们产生的值是多少，以及，我们如何识别这部分代码。

### Representing Values

使用java.lang.Object封装多种类型。

### Evaluating Expression

继续使用visitor模式。

#### Evaluating literals

直接返回字面量。值和字面量是不同的。

#### Evaluating parentheses

直接计算其内部的值。

#### Evaluating unary expressions

一元运算符有取负和逻辑非。

#### Truthiness and falsiness

需要考虑哪些类型可以转换成布尔值。Lox将0和nil视为空。

#### Evaluating binary operators

需要注意二元运算符的取值顺序。

### Runtime Errors

应该向用户隐藏java细节，让用户知道的是lox的报错。

#### Detecting runtime errors

### Hooking Up the Interpreter

需要对interpreter进行封装。并提供一个统一的接口。

DESIGN NOTE: STATIC AND DYNAMIC TYPING

动态类型和静态类型并不是非黑即白的。静态类型语言也会在运行时进行类型检查。例如java会进行cast检查。推迟一些类型检查到运行时可以增加代码的灵活性，但是类型检查的意义就是为了避免处理一些运行时的问题。

## Statements and State

存储变量的值需要编译器支持内部状态。

### Statements

- expression statement: 以`;`结尾
- print statement

#### Statement syntax trees

添加`Stmt`语法。

#### Parsing statements

#### Executing statements

解析完成之后需要同时更新Interpreter。

### Global Variables

#### Variable syntax

声明变量也是一个statements。但是声明语句的范围有限制。所以要区分declaration和statement。

#### Parsing variables

### Environments

使用`Map`来存放值。对于变量和作用域，可以借鉴scheme的设计，允许变量重复定义。Lox在访问未定义的变量时，会进行运行时报错。

#### Interpreting global variable

### Assignment

#### Assignment syntax

等号左侧应该是左值，所以要把表达式转变成变量。因为等号是右结合律，所以逻辑有一些不同。

#### Assignment semantics

### Scope

考虑到作用域，同样的名字可以指向不同的对象。

Lexical Scope是变量基于其位置而处于对应的作用域。

Lox中变量是Lexical Scope的，而对象中的方法和成员则是Dynamic Scope的。

#### Nesting and shadowing

作用域内的变量会隐藏作用域外的同名变量。因此需要将environment以链的形式连接起来。其实就是类似于责任链模式了。

#### Block syntax and semantics

Block是一个statement。

DESIGN NOTE: IMPLICIT VARIABLE DECLARATION

一些语言支持隐式变量声明，但是这就意味着需要处理shadowing等问题。

隐式变量声明的问题：

- 对于错误的拼写变量名难以察觉。
- 外层作用域的变化会影响内部代码的语义。
- 难以给外部作用域的变量赋值。

为了解决这些问题

- JavaScript增加了`Strict Mode`来限制隐式声明全局变量
- Python增加了`global`说明符
- Ruby增加了显式声明的逻辑

## Control Flow

### Turing Machines(Briefly)

computable functions. Turing machine and lambda calculus.

图灵完备。

### Conditional Execution

- Conditional control flow or branching control flow
- Looping control flow

if statement执行statement。`?:`执行expression。

else应该和最近的if匹配。

### Logical Operators

还需要`and`和`or`。这个的特点是存在逻辑短路short-circuit，可以不计算一部分数据。

### While Loops

区分expression和statement可以在while中十分清楚的看出来。

### For Loops

#### Desugaring

for和while是一致的，其实相当于是语法糖。这可以让代码更加高效，但是需要后端支持。但是除此之外还可以desugaring，前端将语法糖转换为更原始的，后端已有的表示，这会在parsing阶段实现，这样就不需要添加新的语法节点类型了。

DESIGN NOTE: SPOONFULS OF SYNTACTIC SUGAR

Lisp，Forth，Smalltalk都没有语法糖。C，Lua，Go追求的是清晰。更复杂的是Java，C++，Ruby，Perl和D。

语言会随着时间，不断增加语法糖。

## Functions

### Function Calls

可以通过括号调用一个expression。这拥有最高优先级。

#### Interpreting function calls

#### Call type errors

在调用前增加类型检查。

#### Checking arity

需要匹配调用的参数数量和函数声明的参数数量。

### Native Functions

添加native方法来供用户调用。native function是在宿主语言（对jlox来说是java）实现的方法。Native方法决定了用户能做的事情。FFI(foreign function interface)允许用户自己定义native functions。

#### Telling time

benchmark需要时间。

### Function Declarations

### Function Objects

需要将语法对象function封装成LoxCallable来被调用。

函数调用时需要基于global创建一个新的environment。

### Return Statement

#### Returning from calls

return需要从堆栈深处返回到调用call的地方。考虑使用exception实现。

### Local Functions and CLosures

函数运行的environment的父节点应该是什么？local function。闭包。将函数定义时的environment保存下来。

## Resolving and Binding

目前实现的闭包留下了漏洞。

### Static Scope

lexical scoping: A variable usage refers to the preceding declaration with the same name in
the innermost scope that encloses the expression where the variable is used.

函数所处的作用域会在函数定义之后被修改，因此会导致闭包被修改。导致不一致的行为。

#### Scopes and mutable environments

变量声明会修改environment，或者说，将一个environment拆分成了两个。

#### Persistent environments

persistent data structures对于修改，只产生新的修改之后的副本，而不会变化原始值。

但是Lox使用记录变量的作用域位置来解决这个问题。

### Semantic Analysis

分析用户的程序，找到所有使用的变量，只进行一次变量解析。这是一个语义分析的例子。

其实需要记录的是每一个变量是经过几个跳数之后找到的。

在parser之后增加一个resolver来做这件事情。

#### A variable resolution pass

对于静态类型语言，类型检查也可以在这里进行，以及其他优化。但是这不是真的运行。

- There are no side effects
- There is no control flow

需要考虑复杂度。

### A Resolver Class

Resolver只关心block、函数声明、变量声明、对变量的解析。

#### Resolving blocks

#### Resolving variable declarations

增加一个编译报错。对于在初始化中使用变量自身。将变量绑定区分成声明和定义。声明时将变量标记为false来说明还没有完成初始化。

#### Resolving variable expressions

#### Resolving assignment expressions

#### Resolving function declarations

函数声明和定义是一起进行的，因为函数支持自己调用自己。

#### Resolving the other syntax tree nodes

对于if语句，静态分析会处理两个分支。

### Interpreting Resolved Variables

对于处理得到的数据可以将其放在AST中，也可以额外放在一个map中。放在map中让这部分数据可以很容易的被丢弃。只需要一个map就可以存储。

#### Accessing a resolved variable

resolver和interpreter之间存在着耦合。

#### Assigning to a resolved variable

#### Running the resolver

### Resolution Errors

增加重复声明的编译时检查。

#### Invalid return errors

增加对return调用的检查。

## Classes

### OOP and Classes

OOP的三种方式: classes, prototypes, multimethods。

classes的关键: `constructor` `instance` `field` `method`

### Class Declarations

类型中只定义函数，不定义成员。

### Creating Instances

Lox中类作为工厂函数返回实例。

### Properties on Instance

#### Get expressions

#### Set expressions

### Method on Classes

对Lox来说，方法只是一个函数成员。可以被取值和赋值。对于取值，方法会捕获实例。

### This

通过this来在方法中获取类实例。类似于closure。在get时增加闭包。

#### Invalid uses of this

记录当前是否处于类型当中，并对this进行检查。

### Constructors and Initializes

构建对象包含两个步骤

- 申请内存
- 初始化对象

c++ placement new 允许在给定的内存中进行初始化。

#### Invoking init() directly

显式调用`init`返回`this`指针。

#### Returning from init()

增加对`init()`中静态检查的方法。

DESIGN NOTE: PROTOTYPES AND POWER

Prototype:方法是直接施加在实例上的，没有类的概念了。

`power = breadth * ease / complexity`

Breadth: 语言允许你表达的内容

Ease: 让语言表达用户所想要表达的所需要花费的精力

Complexity: 思维负担。

## Inheritance

### Superclasses and Subclasses

Lox使用`<`表示继承。对父类进行解析。对继承自己的情况进行检查。

### Inheriting Methods

尝试对父类调用方法。

### Calling Superclass Methods

子类调用父类方法。`super`关键字。

#### Syntax

#### Semantics

`super`应该从包含`super`表达式的父类开始查找。通过在函数闭包当中捕获`super`来实现这部分功能。但是区别是，`this`在函数被访问时绑定，`super`在函数声明时绑定。

#### Invalid uses of super

在resolver中添加对`super`的检查。

### Conclusion

## Chunks of Bytecode

遍历AST进行运行的方式性能比较羸弱。

### Bytecode?

#### Why not walk the AST?

已有的解释器的优点：

- 不需要将AST转换成运行时的数据结构
- 可移植性

已有的解释器的缺点：

- 内存低效，AST需要大量指针来表示
- 对象在内存中分配不紧凑

ref: game programming patterns

#### Why not compile to native code?

机器码是复杂且难以移植的。

#### What is bytecode

bytecode是一种中间状态。基于一种简单的指令集，并实现一个对该指令集的模拟层。

### Getting Started

### Chunks of Instructions

使用一字节枚举值作为operation code(opcode)

定义`OP_RETURN`

#### A dynamic array of instructions

基于opcode实现动态数组。优点：

- 缓存友好，紧密存储
- 常量时间index查找
- 常量时间尾部数据增加

增加count和capacity。

对于数组大小，从8开始，每次翻一倍。

使用宏来处理数组元素大小。

只使用一个函数来完成内存的申请、释放和变化大小。

实现内存管理的方法。

### Disassembling Chunks

实现disassembler来可视化chunk。

### Constants

字面量需要存储在机器码中。

#### Representing values

immediate instructions：立即数指令，数值直接存在opcode之后。

字符串则存储在constant data区域。clox中将所有常量都放在constant data区域中。

#### Value arrays

将value array作为chunk的成员。

#### Constant instructions

`OP_CONSTANT`加载参数。它有一个operands作为参数。每个opcode都有自己的instruction format。

### Line Information

需要在机器码中保留对应的源码行数。clox选择将命令对应的行号存储在同样大小的另一个数组当中。

#### Disassembling line information

DESIGN NOTE: TEST YOUR LANGUAGE

增加test suite。

## A Virtual Machine

### An Instruction Execution Machine

虚拟机的实现是一个单独的模块。

#### Executing instructions

使用ip(instruction pointer, pc, program counter)记录运行的位置。ip永远指向下一个指令。

获得指令之后需要对指令进行解码。clox中使用一个switch来实现。

#### Execution tracing

增加对虚拟机执行的log。

### A Value Stack Manipulator

使用栈来缓存运行结果。

#### The VM's Stack

现代的解释器使用了复杂的JIT来更快的生成native code。

#### Stack tracing

### An Arithmetic Calculator

实现取负操作。

#### Binary operators

将符号作为参数传入宏中。在宏中使用do while结构来支持在一个block中插入多个statement并且允许在结尾存在一个分号。

DESIGN NOTE: REGISTER-BASED BYTECODE

寄存器可以直接读写。

寄存器带来性能提示。

ref:[The Implementation of Lua 5.0](https://www.lua.org/doc/jucs05.pdf)

## Scanning on Demand

### Spinning Up the Interpreter

`fseek` `fteel`来获取文件长度。

增加错误判断。

#### Opening the compilation pipeline

#### The scanner scans

实现一个scanner单例。

### A Token at a Time

实际上编译器并不需要一直记录所有token，parse阶段也需要提前看一个token。因此一个简化方案是在需要时才scan一个token。

`printf`中使用`%.*s`来讲长度也作为参数传入。

scanner给出一个Error类型的token来表示scan到了异常。token并不持有lexeme，而是直接指向源码中的子串。

#### Scanning tokens

### A Lexical Grammar for Lox

#### Whitespace

#### Comments

处理空格换行和注释。

#### Literal tokens

在编译器中再将字面量转换成运行时值。

### Identifiers and Keywords

需要对保留字进行处理。一个简单的方法是使用hash表。

#### Tries and state machines

Trie:前缀树

前缀树是DFA(deterministic finite automaton,确定性有限状态机)的一个特殊例子。正则表达式匹配也是使用DFA实现。龙书介绍了这部分。

Lex可以根据词法自动生成对应的c代码。

## Compiling Expressions

使用的算法：Vaughan Pratt’s “top-down operator precedence parsing”

ref:[Pratt Parsers: Expression Parsing Made Easy](http://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/)

### Single-Pass Compilation

clox在一次遍历中同时进行解析和代码生成。

### Parsing Tokens

#### Handling syntax errors

对parser增加标记是否有error和是否处于panic mode。

### Emitting Bytecode

抽象接口实现向chunk添加指令。

### Parsing Prefix Expressions

#### Parsers for tokens

每种token对应一种表达式，一个表达式对应一个函数指针来生成对应的bytecode。

对于字面量，将其添加到`ValueArray`中。

#### Parentheses for grouping

括号递归的调用`expression()`，并且不需要发送bytecode。

#### Unary negation

一元运算符在操作数计算之后尽心计算。与jlox不同，clox的`unary`还是调用`expression`，而不是调用更低优先级的方法。增加一个方法基于优先级来进行parse，其中只允许更高优先级的方法。

### Parsing Infix Expressions

对prefix和infix，需要存在两列函数里面。

### A Pratt Parser

实现函数表

#### Parsing with precedence

parsePrecedence中会对优先级进行检查，只允许更高优先级的运算。

### Dumping Chunks

对于parser不报错的情况，打印输出chunk。

DESIGN NOTE: ITʼS JUST PARSING

parser generators。Parser是很容易实现的。

## Types of Values

问题：如何动态表示不同类型。

### Tagged Unions

需要解决两个问题：我们如何表示一个值的类型和我们如何保存值本身。需要关注效率。

clox通过union加上enum实现，也就是tagged union。

### Lox Values and C Values

使用宏对类型进行检查。

### Dynamically Types Numbers

#### Unary negation and runtime errors

对于运行时的类型错误需要进行检查。

推荐c语言教程：[The C Programming Language](https://www.cs.princeton.edu/~bwk/cbook.html)

#### Binary arithmetic operators

对二元运算符进行类型检查。

### Two New Types

对于布尔值和`nil`的字面量，相比起放在常量表中，更高效的方式是直接添加对应的指令。

#### Logical not and falseness

#### Equality and comparison operators

只用三个操作符来处理大于等于和小于的五个符号。

## Strings

### Values and Objects

增加类型Obj。

### Struct Inheritance

通过在首位放置父类来实现继承。这是c语言有意的设计，参见:[C ISO标准](https://c0x.shape-of-code.com/6.7.2.1.html)

对于宏中的值需要使用两次的情况，需要避免同一个值被调用两次，改为使用函数封装。

### Strings

实现String对象的创建

### Operations on Strings

使用`memcmp`对字符串进行比较。

#### Concatenation

对字符串拼接增加支持。

### Freeing Objects

需要避免内存泄漏，及时释放对象。用链表来存储所有对象。通过栈中是否持有引用来决定对象是否需要被回收。

对于需要GC的语言，越早考虑GC，越合适。

使用`reallocate`来统计申请的内存。

DESIGN NOTE: STRING ENCODING

- ASCII
- Unicode

## Hash Tables

通过变量名获取变量的值需要依赖哈希表。

哈希表的特点是，平均查询是常量时间的，无论有多少键。

### An Array of Buckets

直观的想法是使用一个数组，每一个元素对应一个字母。

#### Load factor and wrapped keys

对于更长的情况，可以将数组取模。

可以通过load factor评估哈希冲突的概率。达到一定冲突率之后可以对数组进行扩容。

### Collision Resolution

还是需要解决哈希冲突。

#### Separate chaining

冲突时放在链表中。

#### Open addressing

用另一个空entry去放置冲突的元素。需要确定探测序列(probe sequence)。

clox使用线性探测(linear probing)

### Hash Functions

对哈希函数的要求：

- 必须是决定性的
- 必须是均匀分布的
- 必须要高效

clox使用FNV-1a作为哈希函数。

### Building a Hash Table

#### Hasing strings

对字符串的哈希值进行缓冲。

#### Inserting entries

#### Allocating and resizing

当大小变化的时候，所有数据都需要重新取模进行计算。

#### Retrieving values

#### Deleting entries

从哈希表中删除也需要一些设计。移除并不设置为空，而是放置一个墓碑。但是，当表中全部都是墓碑时，程序会陷入到无限循环当中。

#### Counting tombstones

变为墓碑不减少计数。

### String Interning

将字符串对象本身保留为只有一个，使用时只传递引用。

clox intern所有字符串，使用哈希表。

clox中的字符串只需要比较地址。

## Global Variables

全局变量和局部变量实现不同。局部变量可以进一步优化。

全局变量可以在定义前被访问，局部变量则必须在访问前被定义。

### Statements

#### Print statements

一个statement应该总计对栈不产生影响。

#### Expression statements

对于expression，需要最终进行pop。

#### Error synchronization

在clox中实现错误同步。

### Variable Declarations

对于变量，需要支持三部分操作：

- 变量声明
- 变量访问
- 变量调用

将变量名作为常量。

### Reading Variables

### Assignment

对于赋值来说，差异来自于最后那个符号。对赋值的优先级需要特殊处理。也就是说，对变量的赋值和取值的优先级是不同的。

## Local Variables

全局变量在clox中是运行时绑定的，这是低效的。对于局部变量和函数变量，需要基于lexical scoping修复这个部分。

### Representing Local Variables

c和java在栈中实现局部变量。clox可以在虚拟机栈中实现局部变量。

因为表达式不会残留内容在栈中，所以栈区的变量永远都在最内部。

> As programmers, our intuition of what’s “normal” in a language is informed even today by the hardware limitations of yesteryear.

使用栈内的偏移来定位变量。

### Block Statements

### Declaring Local Variables

声明局部变量不需要做什么，只需要将栈区的内容保留下来就可以了，随后通过栈底的偏移来访问变量。

因此当局部变量数量超过256时，会溢出缓冲区。

clox不允许局部变量重复定义。

在退出作用域时将locals数组中记录的当前作用域的数据进行清楚。

### Using Locals

#### Interpreting local variables

在get局部变量是会将栈上的变量再一次添加到栈上。

#### Another scope edge case

还需要处理`var a = a;`的特殊情况。使用深度为-1来表示定义但是还未初始化的情况。

## Jumping Back and Forth

### If Statements

需要知道跳转距离。使用技巧`backpatching`，留下占位符号，在之后来填补。

#### Else clauses

对于else的情况，else分支需要被then分支跳过。

需要去除if在栈中残留的值。

### Logical Operators

逻辑运算符因为短路的存在，也需要基于jump来实现。实际上这和if-else非常像。

对于and，不短路的话，需要将残留的值去除，否则的话就不去除。

#### Logical or operator

可以基于已有的接口来实现逻辑或，代价是性能会受到影响。

### While Statements

### For Statements

#### Initializer clause

#### Condition clause

只有有Condition clause的时候才会涉及到退出。

#### Increment clause

DESIGN NOTE: CONSIDERING GOTO HARMFUL

ref: Go To Statement Considered Harmful Edsger Dijkstra

Dijkstra询问如何找到精确的运行位置。引入goto将会使这难以做到。goto无疑会写出坏的代码，但是它对于从深循环当中直接退出非常有帮助。

## Calls and Functions

### Function Objects

每个函数有自己的chunk。

### Compiling to Function Objects

因为函数是编译进自己的chunk中，所以需要记录当前的chunk。可以将整个全局作用域抽象成一个最大的函数。

#### Compiling functions at compile time

函数式对象是编译时创建的，在运行时被调用。

在local中创建一个编译器使用的变量，用来将全局函数对象存下来。。

编译器最终返回的就是一个函数对象。

### Call Frames

#### Allocating local variables

不同函数的变量存放在哪里？

可以每个函数都独立存储局部变量，但是这样函数就不能被递归调用了。

可以将局部变量放在栈上，但是需要一个方法来在编译期确认局部变量的位置。这就需要记录函数被调用时的栈顶，这被称为`call frame`。

#### Return addresses

还需要记录函数调用的地址来在返回时知道返回到哪里。

#### The call stack

### Function Declarations

#### A stack of compilers

在编译时也需要处理函数的嵌套。可以通过每一个函数对应一个编译器来解决这个问题。通过一个编译器栈来追踪函数的嵌套关系，也就是链表。

#### Function parameters

将函数参数作为变量解析。

### Function Calls

对于函数调用将`(`视作infix运算符。

#### Binding arguments to parameters

基于栈的函数调用不需要将函数参数再进行拷贝，函数参数本身就已经在栈上排列好了。

#### Runtime error checking

对函数参数进行运行时检查。

对函数调用的堆栈深度进行检查。

#### Printing stack traces

基于函数的调用堆栈可以实现运行时异常可以打印出函数堆栈。

#### Returning from functions

在函数结束时，返回一个`nil`。

### Return Statements

### Native Functions

Native函数没有vm的call frame。

## Closures

闭包需要局部变量在函数结束之后依然存在。

因此对于被捕获的变量，会将其的生命周期移动到堆上，否则，变量的生命周期还是在栈上。

一些技法: closure conversion和lambda lifting

### Closure Objects

clox的函数是在编译时创建的，在运行时只是加载，并不会在运行时创建一个函数对象。

但是对于闭包对象则不是如此，这需要运行时的对象创建，因为实际上每次闭包函数创建的对象是不同的对象。因此需要对闭包对象进行一些运行时表示。clox的设计是在ObjFunction外部再封装一层ObjClosure，对对应的ObjFunction进行引用。因此对于ObjClosure来说，析构时并不会对其中的ObjFunction进行析构。

ObjClosure是对用户来说隐藏的。

#### Compiling to closure objects

增加一个`OP_CLOSURE`操作符，用于创建一个ObjClosure。

#### Interpreting function declarations

### Upvalues

因为clox是single-pass编译器，所以在后面的函数中访问变量时才能知道对应的变量会被捕获，因此需要一种方法允许将一个栈上的变量转变为闭包变量并且允许变量仍然被作为栈上的变量被处理。

对应的技术在lua中被成为upvalue。

#### Compiling upvalues

#### Flattening upvalues

对于双层嵌套的情况，会发现要捕获的变量在函数声明时已经不存在栈上了。

解决方法是使用upvalue以链表的方式追踪超出了一层的变量。

### Upvalue Objects

对于upvalue，也有运行时的表示ObjUpvalue，用于对捕获的变量进行引用，但是ObjUpvalue的数值并不会随其析构。

#### Upvalues in closures

### Closed Upvalues

需要将捕获之后的变量从栈上移除。

#### Values and variables

需要考虑闭包捕获的到底是值还是引用。

#### Closing upvalues

open upvalue还在栈上，closed upvalue在堆上。

将变量移动到堆上的时间应该尽可能推迟。

#### Tracking open upvalues

应该让函数调用更快一些，而声明可以稍微慢一些。存储所有upvalue并在其中查找是否存在重复的捕获。

#### Closing upvalues at runtime

在捕获变量时要将对应的upvalue中的指针也更新，将location指向自己的closed。*为什么不在Local中记录upvalue呢？*

对于函数的最外层，是由call frame来回收的，因此也需要捕获变量。

DESIGN NOTE: CLOSING OVER THE LOOP VARIABLE

闭包捕获循环中的变量，在一些更高阶的函数的情况下实际上会捕获到不同的值。

## Garbage Collection

Managed language: 基于用户的行为进行内存的申请和释放

### Reachability

被gc的是不会再被使用的变量，而这就需要vm近似估计哪些变量不会再被使用。`conservative GC`:将内存中的所有部分都视为指针。`precise GC`:区分内存中哪些是指针，哪些是字符串和数字。

在lox这样的内存安全的语言中，是可以做到判断的，因为一个可以被访问的值是一个用户可以引用到的值。

对于可达性，可以认为，所有根都是可达的，所有被根引用的对象也都是可达的。

大致上gc的结构是递归地找到所有被引用的对象，随后释放其余的所有对象。

ref: The Garbage Collection Handbook Jones

### Mark-Sweep Garbage Collection

最早使用gc的语言是lisp。使用了Mark-Sweep算法。

ref: History of Lisp McCarthy

Mark-Sweep算法包含两个阶段：

- Marking: 从根节点开始遍历所有引用的节点，每次引用都将其坐上标记
- Sweeping: 释放所有未被引用的对象

#### Collecting garbage

增加一个对gc进行压力测试的方案：尽可能频繁的触发一次gc。当申请更大的内存时，会触发gc。

在申请内存之前进行gc是触发gc的典型方法，因为在这之后程序会需要更多的内存。

#### Debug logging

gc的步骤对程序员来说是不可见的。需要通过日志来进行分析。

首先添加gc开始和结束的日志。

### Marking the Roots

局部变量、临时变量和全局变量是根。

#### Less obvious roots

对于每一个frame的closure都可需要进行标记。同样的还没有闭合的upvalue list也需要被标记。

编译时也会触发gc，所以也许要被标记。

### Tracing Object References

需要遍历变量。

#### The tricolor abstraction

需要避免略过对象或者陷入环形循环。

tricolor abstraction: 用于减缓gc的心智负担。

- 白色: 未到达的对象
- 灰色: 已经到达但是未处理其中的引用的对象
- 黑色: 引用的对象也都已经被处理的对象

tricolor invariant: 不会有一个黑色节点引用一个白色节点。

#### A worklist for gray objects

使用独立的worklist来追踪所有的灰色对象。worklist是一个栈。worklist的内存申请不会再由`reallocate`管理。

#### Processing gray objects

### Sweeping Unused Objects

#### Weak reference and the string pool

对于string pool中的不再被引用的字符串，它也应该从string pool中被移除。

### When to Collect

需要确定一个进行gc的时间。

#### Latency and throughput

两项指标: throughput和latency。

- Throughput: 在全部时间中，运行用户代码的时间。
- Latency: 最长的一块进行gc的持续时间。

两方面是需要平衡的。

#### Self-adjusting heap

gc频率根据堆的大小自动调整。堆中存活的数据越多，gc的频率越低。

### Garbage Collection Bugs

因为gc会在所有申请内存的情况下发生，所以需要尽快将变量增加到栈上。

Boehm collector: 会将c语言栈上的变量也纳入处理。

#### Adding to the constant table

#### Interning strings

#### Concatenating strings

DESIGN NOTE: GENERATIONAL COLLECTORS

generational hypothesis: 一个对象活得越久，一个对象越有可能活下去。

## Classes and Instances

### Class Objects

### Class Declarations

### Instances of Classes

对于类的成员，使用一个哈希表来实现。对象析构时，哈希表会析构，但是其中的元素不会，这依赖于gc去回收。

对于类的实例化，将类作为函数调用。

### Get and Set Expressions

#### Interpreting getter and setter expressions

## Methods and Initializer

### Method Declarations

#### Representing methods

#### Compiling method declarations

### Method Reference

方法可以作为变量被引用，同时需要持有this指针。也就是ObjBoundMethod。

#### Calling methods

将第一个槽用来存放this指针。在调用函数时，将this插入第一个槽。

#### Misusing this

需要处理编译器当前是否位于某一个类的声明内。使用链表来声明当前位于哪一个类的声明内。

### Instance Initializers

#### Invoking initializers

#### Initializer return values

对于构造函数的返回值需要做隐式处理，来保证会返回this。

#### Incorrect returns in initializers

在构造函数中不能返回其他数值。

### Optimized Invocations

对于函数直接调用的情况，还是会有对象创建和回收，这是额外的不必要的性能开销。

#### Invoking fields

DESIGN NOTE: NOVELTY BUDGET

一个好的编程语言应该支持用户拥有更多的语言能力和更少的学习成本。

语言应该简单。和其他语言拥有相同的特性，会使学习成本更低，这是近似。但是一个编程语言需要有自己的特点。

idiosyncrasy credit: 一些部分做的好让你能够在其他方面表现得怪异。

需要衡量一个编程特性带来的好处，和它带来的学习上的困难。在语法上保守，在语义上激进。

## Supperclasses

### Inheriting Methods

#### Executing inheritance

子类不再持有父类的指针，而是直接复制父类的方法。

这是copy-down inheritance，这依赖于类本身不可以被修改。

#### Invalid superclasses

对父类进行类型检查。

### Storing Superclasses

#### A superclass local variable

增加一个接口将c的字面量常量转化为token。

### Super Calls

super后面必须接`.`和方法名。

#### Executing super accesses

#### Faster super calls

对父类的调用也进行优化。

### A Complete Virtual Machine

## Optimization

### Measuring Performance

优化在今天是一个经验性的工作。

#### Benchmarks

需要确认两件事：

- 优化确实提升了性能
- 其他无关的修改没有降低性能

这两个问题要通过benchmarks来解决。

benchmarks也会随着语言的进步不断地进步。

#### Profiling

需要一个profiler来进行性能测试。

### Faster Hash Table Probing

#### Slow key wrapping

模运算比较缓慢。因为模的大小是2的n次方，所以可以使用位掩码来完成这一操作。

### NaN Boxing

也有些性能优化是通过对底层机器架构的理解和思考来达到的。

动态数组因为需要标记变量的类型，所以需要一些额外的空间。

#### What is (and is not) a number?

IEEE 754, IEEE Standard for Floating-Point Arithmetic.

只要指数位都是0，那就是NaN，又分为signalling NaN和quiet NaN。signalling NaN意味着cpu计算异常，可能会完全退出程序。quiet NaN是安全的，可以更安全的使用。再减去一位未定义的值。有2的51次方个quiet NaN可以使用。

类似地，指针其实也只需要48位就可以了，因此也可以放到浮点数剩余的位中。

这样的方式的优点是不需要做位偏移。

#### Conditional support

因为这些实现是依赖于平台的，所以对于两种方式，都需要支持。

#### Numbers

使用memcpy来避免类型转换，编译器优化会实际上去除这个memcpy。

#### Nil, true, and false

#### Objects

其实使用pointer tagging也可以利用指针的末几位存放别的数据。

#### Value functions

#### Evaluating performance

应该基于release版本去做性能测试。

### Where to Next

更近一步

- 实现编译期优化: Engineering a Compiler和Modern Compiler Implementation
- 对编程语言学术进行了解，论文
- 改造lox为一门自己想要的语言

> If you can handle compilers and interpreters, you can do anything you put your mind to.
