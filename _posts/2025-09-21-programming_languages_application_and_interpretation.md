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

### What is an Object?

对象的特点

- 一个值
- 将名字映射为
- 其他值或者方法

方法可以被看做只是函数。

member: 对象的条目，不管是变量还是方法。

使用lambda来表示对象，并使用case来进行分派。

lambda是一个只有一个entry point的对象。

racket语法中使用`.`来表示绑定后续所有参数到一个值中。`apply`将这些参数拼接到调用函数中。

这允许我们通过计算来获得成员名。

有时会遇到一个目标语言没有对应部分的情况。

### The “Object” Pattern

### Constructors

向函数添加参数就相当于实现了构造了参数。

### The “Class” Pattern

引入了构造函数实际上就转变为了一个类型。

### State

有人认为对象最开始时用于封装状态的。

Smalltalk的创建者Alan Key认为OOP的理想是找到一个比赋值更为灵活的方案，甚至更进一步直接把赋值给消除掉。

ref: [The Early History Of Smalltalk](http://worrydream.com/EarlyHistoryOfSmalltalk/)

使用`set!`来对变量进行操作。

### Private Members

同一个类型的不同的实例可以互相访问private成员。

增加一个函数内部的变量就可以作为私有成员了。

### A Refined “Class” Pattern

可以在类中引入私有成员。

### Static Members

静态变量是在构造函数之前的标识符。

### A Re-Refined “Class” Pattern

### Objects with Self Reference

实现self或this。

#### Self-Reference Using Mutation

设定一个名称用于递归的自调用。

使用一个dummy值声明变量再将其改变为递归调用的值，是递归let的核心。

#### Self-Reference Without Mutation

另一种方法是将函数的第一个参数设置为this。通过这种方式可以区分函数和方法。

### Dynamic Dispatch

动态分配将条件分支从用户程序迁移到了语言实现中。

关键是一个可拓展的条件语句。其实就是实现了同名函数。

这样的特点是一种黑盒可拓展性，系统的一部分进行拓展并不需要修改对应的其他部分。这通常被认为是面向对象的一个关键优点。对应的，函数式编程可以方便的拓展方法，面向对象可以通过访问器设计模式将来实现这类似函数式编程的特点。

ref:[Synthesizing Object-Oriented and Functional Design to Promote Re-Use](https://cs.brown.edu/~sk/Publications/Papers/Published/kff-synth-fp-oo/)

## What Else do Objects Have?

### Member Name Design Space

有两个关于对象的问题:

- 对象的成员名是静态的还是动态的
- 访问对象的成员名是静态的还是动态的

对于两者都是动态的语言，通常会使用哈希表实现。

这一章关注的是都是静态的语言。

### What (Goes In) Else?

对于静态类型变量，可以使用条件表达式而不是哈希表来处理变量。同时，else可以用于进行继承。

不应该随便修改基类，参见，脆弱基类问题。

### A Java Excursion

java需要在子类构造函数中显式调用父类构造函数。因为子类也是父类的实例。

### Extending Classes

子类中需要构造和存储一个父类的变量。这是拓展类。

Java中，对象继承的字段会保留，并可以通过cast访问，方法会被移除。

使用self-application方法的定义对于递归调用来说更为方便。

### Extending Prototypes

Prototype与此不同，将父类看作一个对象本身，而不是一个类。所有继承自同一对象的类会访问同一个对象，修改也是都同步的。

可以参考Self语言。

ref： [Self 官网](http://selflanguage.org/)

一些语言设计者认为Prototype相比起类是更加原始的。

### Multiple Inheritance

一个对象可以继承自多个实例，问题是，查找的顺序。还有菱形继承问题。

需要算法来决定查找的顺序。

多继承是一个十分复杂的问题，只有在还没认真考虑之前才显得迷人。

### Class Extensions: Mixins and Traits

在java中，类体中定义的是类型拓展

mixins: 函数拓展可以独立定义，并随后附加到各种类型上。

这可以利用多继承的优点，同时避免复杂了查找算法。

mixin其实只是一个对类的方法。

mixin需要接口描述期望的输入和输出，也就是两个接口。

这符合设计模式的要求: Program to an interface, not an implementation.

ref: [Classes and Mixins](https://cs.brown.edu/~sk/Publications/Papers/Published/fkf-classes-mixins/)

trait是mixin的推广，一个类同时拓展一组mixin。

## Introduction to Types

对类型语言，写代码就是在写证明。

使用类型进行静态检查。

### A Standard Model of Types

类型检查输入的是语法树，输出的是布尔值。

不止需要知道子表达式是否类型正确，还需要知道当前表达式的类型是否正确，因此需要知道两个子表达式的类型。将类型检查返回的类型改为是Type。

类型检查器的实现架构和解释器是一致的，一个表示AST的代数数据类型，和一个递归处理的结构。这也就是SImPl。

类型检查器对弱值进行运算，即不管什么值，只管类型。传统类型检查器的优点和缺点都是来自于这个忽略。

### A Concise Notation

对类型进行表示:`|- e : T`表示e的类型是T。

axioms: 类型检查的基础情况。

antecedent: 前件，生成的前提

consequent：后件，结论

## Growing Types: Division, Conditionals

### Handling Division

除法是部分函数，对于除数是0的情况需要特殊处理。处理方式：

- 返回一个`(Optionof Number)`，但是这意味着所有的除法都需要检查。
- 依赖类型检查，这需要将0设定为一个特殊的类型，并且需要调用者证明传入的参数并不是0，这对用户会有心智负担，基于莱斯定理，这是无法自动判断的。
- 返回一个普通的值，但是对于除数为0的情况，会抛出一个异常。这会给用户带来心智负担。

ref: 莱斯定理

对于更通用的处理部分函数的方法，可以参见：

ref: [Partial Domains](https://dcic-world.org/2025-02-09/partial-domains.html)

已有的语言大多选择了第三种方法，但是正不断有语言尝试前两种方法。

### Another Perspective on Types

另一种看待类型的视角是将类型看作一个静态声明。parse就是这样一个过程。类型是对这个的拓展。

从可计算性理论来看，parse是上下文无关的，类型检查时上下文相关的。需要将这两个检查划分到两个阶段中，先进行parse检查再进行类型检查可以减少类型检查的复杂度。

### From Axioms and Rules to Judgments

需要将AST的每一个检点都用axiom进行规定。这样的树叫做judgment。使用模式匹配来处理不同情况。

### Judgments and Errors

类型错误是无法创建一个judgment。

### Typing Conditionals

对于if表达式，因为有两个分支，所以需要考虑两个分支返回的类型，其中有不确定性。解决方案如下：

- 提供一个union类型来表示这个类型或那个类型。
- 约束所有分支都应该有相同的类型。

ref: [Inferring Type Rules for Syntactic Sugar](https://cs.brown.edu/~sk/Publications/Papers/Published/pk-resuarging-types/)

### Where Types Diverge from Evaluation

类型检查和测试是互为补充。Concolic测试，尝试结合两者的优点。

## Growing Types: Typing Functions

### Typing Function Applications

对函数的类型检查需要对整个表达式进行检查。

函数自身就是一个类型，但是函数类型需要确认输入与输出的类型。需要检查函数的形参类型和实参类型是否一致，如果一致，那么函数的类型就是函数返回值的类型。

类型检查的顺序不是固定的，可以是从前到后也可以是从后到前。

### Typing Function Definitions

对匿名函数的类型进行定义。匿名函数的类型由函数体决定。但是函数的返回类型会受到参数传入类型的影响，所以并不能直接通过函数体直接确认函数的类型。

### Typing Variables

和解释器类似的，类型检查器也需要一个Environment来对函数进行类型检查。对类型的证明，需要基于Environment给出。

### Back to Typing Function Definitions

因此函数的形参类型需要由Environment给出。并基于此来对函数体进行类型推导。需要拓展的是静态作用域，也就是函数声明时所处的作用域。因为声明时不知道函数的参数的类型，所以需要增加类型注解来让类型解释器将该变量名拓展为该类型。

### More Divergence Between Types and Evaluation

对类型检查器，函数只有在声明时，才会被访问，而对求值器，函数会在运行时执行任意多次。

### Assume-Guarantee Reasoning

函数的声明和调用在类型检查中有对应关系。

### Recursion and Infinite Loops

递归调用。Simply Typed Lambda Calculus(STLC)通过类型检查来避免无限循环的表达式。

Standard ML使用STLC来避免模块之间的循环依赖。

尽管一些函数是长期运行的，但是其实是在不断周期调用必须要结束的程序，如果那个程序无法正常结束，那么就会进入异常状态。

增加类型系统可以改变语言的表达能力。类型是语义。

### Typing Recursion

增加递归函数构造器。需要声明函数的参数和返回值类型。在处理函数体时，会先将函数的类型传递给函数名。也就是说，函数的返回值的声明是为了避免递归调用的类型检查错误而设计的。

## Safety and Soundness

SMoL的一个核心概念是安全。一些运算是部分函数，SMoL语言通过报告违规来确保这一点。

ref: [JavaScript 只有很少的违规](https://www.destroyallsoftware.com/talks/wat)

这样的确保可以是静态的或者是动态的。

安全意味着数据完整性。

### Revisiting the Basic Calculator

### Making Memory Explicit (Unsafely)

对值的内存申请进行显式操作。

申请一个向量，数字直接赋值到向量，返回下标。字符串将其作为数字的数组进行赋值，首位赋值字符串长度。

将运算变更为都是对向量中元素的操作，我们持有的是元素的下标。

此时，同一个向量地址，既可以被解释为是数字，又可以被解释为是字符串。

### Recovering Safety

所以关键在于记录每一个值的类型，并且在使用时进行约束。这是tag，用于表示后续的p的元数据。

随后在存储变量时，将第一位存储为tag。随后在访问时会对tag进行检查，如果类型不对会抛出异常。

### What Price Safety?

对安全进行检查是有时间和空间的代价的。通过类型就可以避免这些代价来达到安全。

### Soundness

类型检查器的工作是对求值器的镜像。只需要考虑通过类型检查的程序，也就是说，只要类型检查器求出了程序的类型，那么程序的结果就是这个类型。这就是type soundness。

soundness 是需要证明的。

### Generic Printing

拥有了tag之后，可以实现泛型的操作，比如打印。

### The Representation of Numbers

32位机器的值会占用4个字节。这也就意味着最后两位永远是0，所以可以利用最后两位来表征值的类型。对于数字，可以直接用剩下的三十字节来表示，这样数值就不需要占用堆区了，在栈区就够了。

## Type Inference

### Unannotated Programs and Types

plait会根据函数的表达式推导函数的类型。

这是Type Inference，类型推导。

类型推导由两部分组成：

- 递归的遍历所有子表达式，生成一组约束条件
- 求解这组约束条件，类似于求多元一次方程组

### Imagining a Solution

基于变量被使用的情况来推导变量的类型。

### Unique Variable Names

对静态作用域语言来说，确认变量名是容易的。

### More Informal Examples

对于类型错误，需要更多的报错。

### Algorithmic Details

这样的算法是Hindley-Milner inference。具体内容可以参见前两个版本的书。

## Algebraic Datatypes

`define-type`进行类型定义进行了三个步骤

- 基于新类型一个名字
- 允许类型使用多种情况或变体进行定义
- 允许递归的定义

这就是代数数据类型。变体之间用or连接，成员之间用and连接。这也可以被称作tagged union。

### Generated Bindings

对于代数数据类型，如何进行确定类型。plait会自动生成检测代数数据类型和获取成员的方法。

### Static Type Safety

那些获取类型的方法是不安全的，对错误的类型进行调用也可以通过类型检查。

### Pattern-Matching and Type-Checking

可以使用模式匹配来进行处理。`type-case`。同时，模式匹配也将子表达式的类型进行了限制。

模式匹配对静态处理代数数据类型，并且保持静态安全很重要。

### Algebraic Datatypes and Space

对于同一个代数数据类型，需要tag来区分它是哪个变体。

## Union Types and Retrofitted Types

向已有的语言添加类型系统是retrofitted type system。可以将一些运行时的错误转变为静态的错误。

为了避免重写大量代码，类型系统必须兼容常见的类型安全的程序。

### You Get a Type! And You Get a Type! And You Get a Type!

之前的实现是不安全的是因为类型信息在构建之后丢失了。

Typed Racket支持结构体。

### Union Types

利用predicates去进行类型检查。类型检查器会利用predicates来具体对应的类型。

这其实和模式匹配挺像的。

### If-Splitting

对于else的情况也可以推导出类型，并进行缩窄。这种方式被称作`if-splitting`，因为对应的if语句可以区分union。

### Introducing Union Types

Union 类型对于处理部分函数很有用。

ref: [Partial Domains](https://dcic-world.org/2025-02-09/partial-domains.html)

如今因为可以安全的处理Union，所以可以引入Union类型。

### How Many Unions?

代数数据类型中，一个类只能是某一个类的变体，而不能是多个类的变体。但是Union可以让一个类属于多个Union。这带来了灵活性和复杂性。

### Union Types and Space

Union类型需要type-tag来记录类型。代数数据类型的tag只需要区分所有的变体即可，而Union的tag则需要标记所有类型的所有的程序。因此会占用更多的空间。

### If-Splitting with Control Flow

对于JavaScript。类型检查是十分复杂的。

### If-Splitting with Control Flow and State

类型系统的设计者需要面对的问题是，它们要么拒绝常见的程序或者增加类型系统的复杂程度来处理那些常见的程序。

ref: [Typing Local Control and State Using Flow Analysis](https://cs.brown.edu/people/sk/Publications/Papers/Published/gsk-flow-typing-theory/)

### The Price of Retrofitting

在无类型语言中添加类型是沉重的负担，需要一些启发式的结构，而越复杂的启发式的结构在程序不能处理的情况下会变得越奇怪。

### Types and Tags

Type和Tag是有区别的。类型是可以嵌套的，但是Tag是给定的。

## Nominal Types, Structural Types, and Subtyping

用对象来表示代数数据类型。

### Algebraic Datatypes Encoded With Nominal Types

Java中的if-splitting是通过动态分派来完成的。和模式匹配与if-splitting接近的是，都通过某种语法模式来使程序能够静态的处理类型。

一个特点是，模式匹配可以很方便的添加新的方法，而动态分配可以很方便的添加新的类型。

ref： [Synthesizing Object-Oriented and Functional Design to Promote Re-Use](https://cs.brown.edu/~sk/Publications/Papers/Published/kff-synth-fp-oo/)

ref: [Toward a Formal Theory of Extensible Software](https://cs.brown.edu/~sk/Publications/Papers/Published/kf-ext-sw-def/)

### Nominal Types

java的类是`nominal types`，类的名称是决定性的，名字不同的类无法相互替换，即使它们实现一样，有同样的接口。

### Structural Types

另一种不同的类型系统中，类的类型不是名字，而是它的结构和接口。这就是`structural typing`，结构化类型。

ref: A Theory of Objects(Martín Abadi, Luca Cardelli)

ref: [Semantics and Types for Objects with First-Class Member Names](https://cs.brown.edu/~sk/Publications/Papers/Published/pgk-sem-type-fc-member-name/)

### Nominal Subtyping

在java中的三元表达式的类型是两个返回值的最小上界。

### Subtyping

X是Y的子类，`X <: Y`，X可以被安全的替换为Y。

参见PAPL。

ref： [Subtyping](https://papl.cs.brown.edu/2020/objects.html#%28part._subtyping%29)

## Gradual Typing

### From Scripts to Programs

编程语言的潮流是在动态语言中增加静态对应内容。

对于已经基于动态类型的程序，无法立刻将其转换为静态类型的，因为:

- 程序体量很大并且程序员的工作时间有限
- 程序的某些部分甚至不能被静态类型处理

尽管如此，现实世界的一些动态类型语言也被添加了类型系统，使用一种称作`gradual typing`的方法。

### Micro Versus Macro

在gradual typing中，增加类型标注，并随后进行类型检查。

只对一部分确认的类型进行标注会导致代码变得复杂，变成动态和静态的混合，这使得类型检查器更加难以进行，也就是说难以得到有效的结果。

另一种方法是`macro gradual typing`，静态语言和动态语言是两种相似但是不同的语言，它们共享运行时，但是类型检查只会对静态语言进行。这个的例子是Typed Racket

### Typed Racket at Work

通过关注报错来关注两个语言之间的传递。在将Typed Racket的函数暴露给Racket时，会额外进行封装，对参数和返回值进行类型检查。

对Racket的合同系统，可以参见。

ref: [Contracts](https://docs.racket-lang.org/guide/contracts.html)

## Relations

### A Language Genealogy

Prolog程序。

ref [Prolog](https://swish.swi-prolog.org/)

Prolog可以通过已有的关系来推断关系。

Simula开创了OOP，Smalltalk实现了一个纯面向对象语言。

### Encoding Type Rules

对类型规则进行编码，使用Prolog的语法。这样可以将Prolog用作类型检查器和类型计算器，以及程序合成器。

环境在这种情况下是绑定关系的列表。

### Visualizing Prolog Execution

ref: [Prolog 可视化](https://www.youtube.com/watch?v=pLcfMEQjMqM)

## Generators

### A Canonical Example

Generator和函数是有差异的。运行会在yield处暂停，并在下一次调用时从暂停处继续。这类似于一个闭包，其中的变量都存储于闭包中。
