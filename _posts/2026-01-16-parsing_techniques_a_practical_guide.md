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

#### Type 1 Grammars

第一类语法限制了变换规则左右两侧的符号数量。

##### Two Types of Type 1 Grammars

第一类语法monotonic：没有规则左侧的符号比右侧的符号更多。

第一类语法context-sensitive：所有规则的左侧只有一个非终止符由其他符号替换，其余符号不做变换，作为上下文。

monotonic语法需要注意避免产生多于最终需要的符号。

monotonic和context-sensitive是同样有力的。

语言本身也有级别，也就是最高级别的可能的语法的级别。

##### Constructing a Type 1 Grammar

Type 1 语法一般被称作上下文相关语法，CS语法。

#### Type 2 Grammars

Type 2 语法被称为上下文无关语法，CF语法。也就是说上下文的左右都是空的，也就是说左侧只有一个非终止符。

##### Production Independence

上下文无关意味着，每一个非终止符的生成都是和上下文无关的。这使得上下文无关文法的生成图是一个树，也就是生成树。

上下文无关文法以两种过程构建字符串，拼接和选择。此外还有识别机制，将非终止符链接到它的规则上。

上下文无关文法当中的每一个非终止符都生成一个集合，一个语言，和其他非终止符无关。符号的拼接和选择有对应的集合操作。

递归，意味着非终止符最终生成出包含自己的内容。还可以区分直接递归和间接递归，这两者在Parse中没有什么区别。更重要的是区分左递归和右递归。右递归意味着非终止符自身重新生成在右侧。

要是两侧都有东西生成，那么就是自嵌入的，自嵌入是嵌套的。

对于无递归的文法，每一个生成步骤消耗一个非终止符，这样的生成过程不能无线进行，因此是一个有限语言结果。递归式语法的本质。

##### Some Examples

在现实世界中，很多事物是被其他事物定义的，上下文无关文法是一个描述这样的相互关系的精确方法。

这可以保证结果的正确结构，文档准备和文本标记系统，SGML、HTML和XML使用这种方法去表述和控制文档的基本结构。

乔姆斯基和一些Parsing算法依赖上下文无关语法是monotonic的，上下文无关语法是非monotonic的意味着它有$\epsilon$-rule，也就是规则右侧是空的。无$\epsilon$-rule的语法是$\epsilon$-free的。但不是特别重要，因为多数上下文无关语法可以通过替换实现$\epsilon$-free，除非开始符号也可以生成$\epsilon$。不过这样的替换可能会摧毁语法的结构。

##### Notation Styles

有多种方式标记上下文无关语法。两种主要的是BNF(Backus-Naur Form)和CF van Wijngaarden grammars。

##### Extended CF Grammars

通过引入缩写来让上下文无关语法更加简洁和可读。

`+`: one or more Somethings

`*`: zero or more Something

`?`: zero or one Something

这是EBNF(Extended BNF)。EBNF的右侧是一个正则表达式。

对正则表达式的结构存在两种理解，一种是递归的，一种是迭代的。在实践中为了便捷，多数会使用递归的方式。

#### Type 3 Grammars

上下文无关文法的基本特征是描述嵌套的事物。

Type 2.5: 规则右侧只允许存在一个非终止符，但是不限制位置。这是线性语法。

Type 3： 规则右侧只允许存在一个非终止符，并且必须在右侧末尾。也被称为正则(RE)语法。一般正则语法默认为右正则语法，左正则语法需要显式说明。

正则语法是无嵌套语法。

一些正则语法常用于描述字符级的文本结构。正则语法的生成树变成了生产链。

`[]`: one out of a set of characters

正则语法parser生成器lex还支持宏。比起形式语言，计算机科学更注重表达的简单，并愿意付出额外处理的成本。

使用正则语法生成句子时，其中一只只会存在一个非终止符。

正则语法可以通过缩写有效的化简。

#### Type 4 Grammars

Type 4： 规则右侧不允许存在非终止符。

这样便只允许选择替代的。这被称为有限选择(FC, finite-choice)语法。

编程语言中的保留字可以用这种方式描述。

#### Conclusion

### Actually Generating Sentences from a Grammar

#### The Phrase-Structure Case

语法的目的是生成所有的句子。有一种系统性的方法来实现，BFS。

必须要逐个替换非终止符，因为替换可能会破环上下文。对上下文无关文法，这样做是可行的。

无法通过程序判断是否一个PS语法是空集，也就是说不存在算法来判断每一个PS语法是否语法能够产生至少一个句子。

PS语法生成句子的长度顺序是难以预料的。

#### The CS Case

上下文相关语法的变化在于生成句子的长度是会单调增加的。因此可以通过生成直到长于句子长度来判断。上下文相关语言也被称为递归集。

#### The CF Case

上下文无关语法的生成会更加简单。并且可以判断语法是否能够输出一个句子，通过反向搜索来判断一个非终止符是否能产出句子来递归，直到开始符号。

上下文无关文法可以通过不断替换最左和最右侧非终止符来生成，但是在两种情况下的序列并不是直接的镜像，而是对构建树的中左右和中右左两种不同顺序的遍历。

句子的最左推导是不断替换最左非终止符的规则序列。对应的最右推导。

使用箭头下方的小写字母l和r标记是最左和最右推导，使用箭头上面的星号来表示多步替换。

Parsing的任务是基于给定的输出字符串，重新构建推断树或推断图。一些Parsing技术可以视为尝试将输入字符串重建为一个最左或最右推导的过程，随后生成推断树。

### To Shrink or Not To Shrink

应该避免$/epsilon$规则，但是这个规则对语法来说十分便捷。`*`缩写也隐含了$/epsilon$规则。

不允许$/epsilon$规则的语法会十分不方便，这是一种严重的约束。从理论的角度看这并不是问题，因为可以通过机械的变化来将任何语法转变成无$/epsilon$规则的语法，但是代价在于语法的结构会发生变化。

对上下文相关语法，如果保持$/epsilon$规则，则和短语结构语法一致。要包含空字符串，对上下文相关语法，上下文无关语法和正则语法来说，需要增加特殊属性。

许多Parsing方法在原则上只对$/epsilon$-free语法生效。

### Grammars that Produce the Empty Language

对于一个空语言，它的语法应该如何定义。空语言和只有空字符串的语言是不同的。

一个方法是通过循环不让生成过程结束。这是丑陋的。

另一个方法是不定义生成规则。但是在这仍然不让人满意。

一个更优雅的办法是不允许生成过程启动，也就是不设定启动符号。这样的四元组是({},{},{},{})。

可以通过考虑设定生成规则左侧为空来描述噪声。

对空的关注是有意义的，一个系统的简洁和鲁邦可以经由系统处理空情况的难易程度来评估。

### The Limitations of CF and FS Grammars

可以通过uvwxy定理来看到上下文无关语法的局限。

#### The uvwxy Theorem

原始符号：生成谱系中的规则-位置对没有重复的情况。

如果一个句子中所有的符号都是原始的，那么这个句子是原始的。

原始句子中不同位置的相同符号意味着这个符号有两个不同的原始生成谱系。因此最长的原始句子是有限的，原始句子的数量也是有限的。

因此，任何上下文无关语法都会生成一个有限大小的原始句子的核心和可能是无限的非原始句子。

uvwxy定理意味着对于任何被上下文无关语法生成的长于最长原始句子的句子可以被分成五个部分$uvwxy$,$uv^nwx^ny$也会是语法的句子。

这也被称为上下文无关语言的泵引理。

对于产生越来越长的句子但是却不衰减为嵌套句子的语言，是不存在上下文无关语法的。

最长原创句子是语法的属性而不是语言的属性。

#### The uvw Theorem

正则语法有更简单的uvw定理。

### CF and FS Grammars as Transition Graphs

状态转移图。

上下文无关语法的递归状态转移网络，需要一个栈来存储非终止符。

正则语法是非递归状态转移网络，不需要栈来存储非终止符。将出口连到对应的非终止符上作为入口并去掉非终止符，就可以得到状态转移图。

### Hygiene in Context-Free Grammars

语法中可能存在无用的规则。

对0类和1类语法，不存在算法来进行判断。

对上下文无关语法，情况仍然是困难的，有三种原因会导致无用的规则，未定义的非终止符号，不能从启动符号访问，无法产生句子。

#### Undeﬁned Non-Terminals

移除生成没有生成规则的生成符的规则。

#### Unreachable Non-Terminals

#### Non-Productive Rules and Non-Terminals

规则自身不是一个非空的子语言的不是生成性的，如果一个非终止符的所有规则都是非生成性的，那么它也是非生成性的。

#### Loops

非终止符只产生自己的规则也是无用的。

一个无无用非终止符和循环的语法被称作规范文法。

#### Cleaning up a Context-Free Grammar

清理上下文无关文法分成两步，移除非生成性规则和移除不可达非终止符。

##### Removing Non-Productive Rules

通过判断一个规则是生成性的来移除非生成性的规则，一个规则是生成性的，当它右侧所有符号都是生成性的。

未定义非终止符只是一个非生成性终止符的特殊例子。

闭包算法：初始化+推导规则。

##### Removing Unreachable Non-Terminals

通过判断可达来区分不可达的非终止符。

移除不可达非终止符之后不需要再移除非生产性非终止符，不过反过来是不行的。

移除非生成规则是一个自底向上的过程，移除不可达非终止符是一个自顶向下的过程。

### Set Properties of Context-Free and Regular Languages

因为语言是集合，所以考虑对其进行求交并补。
