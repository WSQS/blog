---
title: "Parsing Techniques: A practical Guide"
date: 2026-01-16
url: https://github.com/WSQS/resource_archive/blob/master/26/01/16/Parsing%20Techniques.%20A%20practical%20Guide%20(Dick%20Grune%2C%20Ceriel%20J.H.%20Jacobs).pdf
tags:
  - compile
---

官网: [official website](https://dickgrune.com/Books/PTAPG_2nd_Edition/)

## Preface

### Preface to the Second Edition

一些从第一版到第二版17年间在Parse领域当中的发展。

Parsers除了用于Parse，现在用于代码生成、数据压缩和逻辑语言实现。

#### Exercises and Problems

本书不是面向学校的，不提供习题，但是会提供问题，问题分成not marked、marked Project、Marked Research Project。

#### Annotated Bibliography

不提供URL而是提供搜索关键词。

#### The Future of Parsing, aka The Crystal Ball

统一的Parse算法，几乎所有算法都是带左递归保护的自顶向下搜索。

### Preface to the First Edition

用简单的方式来介绍Parse技术。

ref: Learning to program by Howard Johnston

ref: Programming from first principles by Richard Bornat

## Introduction

Parsing: the process of structuring a linear representation in accordance with a given grammar.

Grammar.

Parse的原因：

- 通过结构可以更进一步处理对象
- 语法展现了我们对句子的认识
- 提供缺失的信息

Parse的逆向是基于大量的句子寻找产生的语法，这是grammatical inference。

### Parsing as a Craft

数学的结构上是静态的，计算科学家的结构是动态的。数学是计算科学的基础。

### The Approach Used

提供并不是直接可以运行的代码。

### Outline of the Contents

Chapter2: 介绍语句和语法

Chapter3: Parsing 背后的规则，Parsing 的种类

Chapter4: 无方向方法

Chapter5: 关于有限状态机的间奏曲

Chapter6-10: 有向方法

Chapter11: 非决定性方法

Chapter12: 最近的技术

Chapter13: 基于有限状态机的上下文无关文法

Chapter14: 并行Parsing

Chapter15: 非乔姆斯基语言的格式化

Chapter16: 错误处理

Chapter17: 实践中的Parser

### The Annotated Bibliography

Chapter18: 带标注的参考文献

## Grammars as a Generating Device

### Languages as Infinite Sets

三个术语`grammar`，`drscribe`,`language`。

#### Language

语言的三个层级，语言消息由句子组成，句子由词组成，词由符号组成。语言的差异可以在这三个层次上发生。

计算机科学当中的层级有所不同，只有句子和token两个层级。

形式语言在此也持有抽象的视角。语言是一组句子的集合，句子是符号的序列。

#### Grammars

自然语言的语法包含句-词和词-字两个层级，`syntax`和`morphology`。

形式语言的语法则非常的宽泛，只要是对语言的准确、有限、完整的描述即可。形式语言还有生成式的语法，这只描述了能够生成，但是并不描述一个给定的句子如何生成。

计算机科学中的语法和形式语言的生成式语法接近，并且希望能够推导出一个句子如何能够被生成。

#### Problems with Infinite Sets

在无限的句子和有限的规则之间，有两个问题：

- 有限的生成规则如何生成无限的句子？
- 句子只是序列，句子的意义在于它的结构，我们如何获得其意义？

##### Inﬁnite Sets from Finite Descriptions

第一个问题比较简单，而更有趣的问题在于，是否所有语言都可以用有限的规则描述，答案是否定的。

##### Descriptions can be Enumerated

描述是可以以长度加字母顺序被枚举的。

##### Languages are Inﬁnite Bit-Strings

只要语言的组成符号是可以排序的，那么语言中的句子也可以以长度加字母顺序进行排序。

对给定的字母表，可以定义全集语言,剩下所有使用该字母表的语言都是该语言的子集。那么这些语言其实可以通过一个无限长的二进制掩码来标记哪些句子属于这个语言来定义。

##### Diagonalization

所有的描述都有一个对应的无限长二进制掩码。

Cantor对角线过程来证明描述无法穷举语言。

##### Discussion

这样的证明显现了将语言处理为形式对象的威力。

我们只能处理所有可能的语言中的一个小的子集。

语言的无限比描述的无限更高价。

#### Describing a Language through a Finite Recipe

终止符与非终止符。本书中终止符小写，非终止符大写。

启动符号。

### Formal Grammars

重写系统，一种基础的形式语法。

#### The Formalism of Formal Grammars

Deﬁnition 2.1： 生成式语法是非终止符，终止符，规则，启动符号组成的四元组。

#### Generating Sentences from a Formal Grammar

短语结构语法。更精简的语法。

可以用图来描述生成过程，生成图，描述了最终句子的语法结构。

生成图是有向无环图。

#### The Expressive Power of Formal Grammars

短语结构语法是我们现有的最有力的表达方式了。

有短语结构语法描述曼哈顿乌龟的移动。

### The Chomsky Hierarchy of Grammars and Languages

只要是能被生成的集合，都可以通过短语结构语法生成，但是短语结构语法本身未必简单或能理解。这是语法短语结构在智力层面的问题。

语法短语结构还有基础和实践的问题，并不存在通用的parsing算法并且所有现有的特殊的parsing算法都十分低效或者复杂。

为了显示短语结构语法的不可管理性，同时尽可能保留生成的能力，引入了乔姆斯基语法层级，分为0到3四层，但也可以引入第五层。0类语法是不受限制的短语结构语法。后续的层级引入了越来越多的限制。
