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

因为语言是集合，所以考虑对其进行求交并非。

对语言的操作如何变换到语法上。

对上下文无关语法和正则语法求交是简单的，只需要定义一个新的启动符号并使其生成原本的两个启动符号。

上下文无关语言的交集语言不一定是上下文无关语言，但一定是第一类语言。多个上下文无关语言的交集会更加强大。

通过引入可以被擦除的符号，可以做到任何0类语言都可以由两个上下文无关语言求交得到。

上下文无关语言和正则语言的交集总是一个上下文无关语言。

### The Semantic Connection

向语法当中添加语义。通过给规则添加语义子句来简历规则两侧的联系。语义信息可以从生成树的叶子节点向根节点流动，这是综合，反之是继承。

两种常见的方式属性语法和转换语法。

#### Attribute Grammars

属性语法的语义子句假定生成树当中的每一个节点都有给一个以上属性的空间。属性语法的语义子句包含一些通过其他非终止符的属性计算非终止符属性的公式。语义也就是计算结果。

如果语义子句计算了规则左侧的属性，那么这个属性是归纳的，反之是继承的。

语义子句使用大括号包裹。

#### Transduction Grammars

转换语法用一个字符串去定义另一个字符串的语义。这个方法表达能力更弱但是更简单并且通常是足够的。假定节点的字符串在所有子节点之后输出。

#### Augmented Transition Networks

强化转换网络引入了递归转换网络，可以设置变量，构建数据结构。

### A Metaphorical Comparison of Grammar Types

如何理解语法的能力。越强大的语言可以定义正确和错误之间更复杂的边界。

用玫瑰比作语言本身的话，越高级的语法是使用越粗糙的工具进行描绘。0类语言是描绘了画面，但是并不意味着语言自身。

用Java程序来看，使用正则语法可以生成词法层面正确的程序，使用上下文无关文法可以生成句法正确的程序，使用上下文相关文法可以生成语义正确的程序，使用无限制的词汇结构语法可以生成所有基于给定输入在有限时间结束的程序。解决一个给定问题的java程序是无法生成的。

### Conclusion

## Introduction to Parsing

Parsing:基于给定字符串重建生成树。

Parsing关注于上下文无关语法。

### The Parse Tree

Parsing的两个问题：why do we need it; and how do we do it.

语法本身是对字符串集合的浓缩性描述，它只关注一个句子是否包含于语言中，而不关心生成的过程。在实践中关注Parsing是因为生成规则中可以添加语义信息，我们可以通过结构化数据获得语义信息，这正是实践中Parsing的意义。

从Parsing中恢复的生成树是Parse树。第二和第三类语法更获得关注也是因为可以更容易地附加语义。

#### The Size of a Parse Tree

n个token的字符串的Parse树包含n个终止符的节点，加上一些非终止符的节点。非终止符的数量是有限制的，所以Parse树的大小是和输入的长度线性相关的。

#### Various Kinds of Ambiguity

一个句子可以有多种生成树，这样的句子是有歧义的。可以区分出本质的和虚假的歧义，关键在于生成树上的差异是否意味着语义上的差异。本质歧义性是语法的特性，也就是语法是否会生成出本质歧义的句子。

语言本身也可以是歧义的，这是内在歧义的语言。

#### Linearization of the Parse Tree

Parse树本身不是必要的，拥有一个应用规则的列表就可以了，这是将Parse树线性化。有前序，中序和后序三种方式可以进行。

前序遍历给出的是最左推导。后序遍历给出的是逆向的最右推导。中序遍历需要定义在几个节点之后并且需要通过括号来表示前n个子节点。对n=1的情况，这是左角推导。

### Two Ways to Parse a Sentence

只有两类Parsing技术，自顶向下和自底向上。其他技术都是技术细节和修饰。

#### Top-Down Parsing

自顶向下是从启动符号开始的。自顶向下会将生成规则以前序的方式得到。

#### Bottom-Up Parsing

自底向上是从句子本身开始的。自底向上会将生成规则以后序的方式的得到。

自底向上可以看作是一种反向的生成，以起始符号作为终止符。生成和规约的双重性是形式语言的基础方法。

#### Applicability

### Non-Deterministic Automata

两个组件：进行替换并记录语法树的机器，决定机器如何移动的控制机制。主要复杂的部分在于控制机制，它设计了大量对语法的知识。

这样两个组件的结构再所有的parsing方法中都会存在。

替换机器被称作非决定性自动机( non-deterministic automaton, NDA)。非决定性意味着有多种可能的行动。其中包含三个组件，输入字符串、部分parse树和内部管理数据。

NDA的优点在于容易构建并且可以维护正确的状态，比如只可以进行正确的操作，这可以减轻控制机制的思维负担。

#### Constructing the NDA

NDA直接由语法推导得到。

#### Constructing the Control Mechanism

有的控制机制与文法有关，有的控制机制对文法无关。可以通过parser生成器来访问语法，生成一个parser，这是表格驱动的parser的范式。

通常来说是大量动态的属于基于静态的语法进行解析，反过来也是可以理解的，比如用多种语法解释给定的字符串。

### Recognition and Parsing for Type 0 to Type 4 Grammars

理论上说，通过广度优先搜索的生成加上在生成时对生成树的记录可以对任何可以被parse的字符串进行parse，无论是哪个类型的语法。

#### Time Requirements

时间复杂度。

指数复杂度，线性复杂度。实时parser可以在读入之后的常量时间内生成parse树。

幂级复杂度。

#### Type 0 and Type 1 Grammars

不存在一个通用的算法能够对任意给定的0类语法和句子在有限时间内能判断语法能够产生句子。

一类语法的情况有所不同，使用自底向上的广度优先搜索来遍历即可。

从实践的层面上说，构建一个足够高效的一类语法的parser是一个十分困难的主题。一个好的0类语法的parser是一个理论证明器的良好起点。

上下文无关语法的parser拥有更高的实践价值。

所有已知的0类，1类和无限制的2类语法的parsing算法都拥有指数时间复杂度。

#### Type 2 Grammars

上下文无关语法的Parsing算法好得多，基于说有上下文无关文法的parsing问题都已经解决了。这个区别是由上下文无关语法的本地性带来的。

##### Top-Down CF Parsing

自顶向下语法的关键是预测和匹配。Parser尝试做的就是找到最左侧的非终止符号，并由此一个适配的替换物。最左侧的非终止符被称为预测过程的目标。

尽管这种方法可以处理任意的上下文无关语法，但是在简单的实现中，会发生循环。这可以通过一些特殊技巧避免，这也就是通用自顶向下parsers。另外，算法需要指数时间。可以通过预先计算各个规则的首个非终止符来规避。

##### Bottom-Up CF Parsing

自底向上语法的关键是替换和缩减。handle是指可替换的部分和替换的规则一起。

要点在于找到handle。

问题是一样的，会发生循环和指数时间。

#### Type 3 Grammars

自顶向下对右正则语法更高效，自底向上对左正则语法更高效。

#### Type 4 Grammars

有限选择语法的关系可以通过简单的查找决定。可以用于编程语言的保留字。

### An Overview of Context-Free Parsing Methods

在所有乔姆斯基语法类型中，上下文无关语法占据了最显著的位置。原因如下：

1. 上下文无关语法的结果是树，这让语义可以简单的表达和结合。
2. 上下文无关语言覆盖了大量的希望自动处理的语言。
3. 高效的上下文无关文法是可能的。

其次重要的是有限状态语法。

#### Directionality

无方向性方法需要随机访问，需要所有输入在Parsing之前进入内存。有方向性方法按顺序一个接一个访问Token。

##### Non-Directional Methods

无方向自顶向下方法是简单和直观的。这是Unger发明的。

无方向自底向上方法也被许多人独立发现。它的简易版本实现比Unger的方法更高效。

无方法方法通常首先构建一个数据结构总结输入句子的语法结构。Parse树可以在下一个阶段被推导出来。

##### Directional Methods

有向方法都显式或隐式的基于parsing自动机。

#### Search Techniques

另一种区分Parsing技巧的方式涉及到引导非决定性parsing自动机的搜索算法。

整体上可以分为深度优先和广度优先。

深度优先的优点是需要的内存与问题的大小成正比，广度优先则可能会出现指数的复杂度。广度优先的优点是它可以最先找到最简单的方案。这两个方法都需要指数时间复杂度。可以通过限制来提升效率。

搜索技术有广泛的应用，一个常见的例子是寻找迷宫的出口。

#### General Directional Methods

有向自顶向下上下文无关Parser以生成顺序识别最左生成。

有向自底向上上下文无关Parser以反向生成顺序生成。

深度优先自顶向下技术允许一种简单的实现，递归下降。这个方法非常适合用于手写parser。

广度优先自底向上导向了Earley parser。以及Chart Parsing。

#### Linear Methods

通用搜索方法是指数时间的。这在实践中是不可用的。

为了获得一个线性时间的parser,需要牺牲通用性。实践中会先定义语法，随后再对语法进行调整来使其符合Parser。

可以通过限制非决定性Parsing自动机为决定性Parsing自动机来实现线性Parsing时间。

决定性Parsing自动机要求语法是非歧义的。

剩下的是解释如何从语法当中推导一个决定性控制机制。并不存在一个单一最优解，而是存在一些半最优解。整体上说思路是一致的，通过对语法深入分析来将可以用于判断死路的信息明确出来。

在Parsing自动化中，决定性意味着向前看k个符号，可以无歧义地确定下一步做什么。

决定性Parsing方法使用首字母缩写进行表示，X(k)表示需要提前看k个符号。所有的决定性方法都需要对语法进行处理来推导parsing自动机。

#### Deterministic Top-Down and Bottom-Up Methods

只用一种决定性自顶向下方法，LL，第一个L是从左到右，第二个L是识别最左推导。LL(1)特别流行，可以使用递归下降技术手动实现。LL(1)可以从最后一个token开始，这也就是RR(1)。

存在相当数量的决定性自底向上方法。最强大的被成为LR。从左到右，识别最右推导。这些方法只能由Parser生成器生成。一些决定性自底向上方法比LL(1)方法更加流行。

LR(1)比LL(1)更强大，但是也更难以理解和不便捷。LR(1)方法可以被反向使用也就是RL(1)。

有一类Parsing技巧需要向前看不受限制个符号。

自顶向下的选择天然的就会更少，自底向上会有更多的选择，需要更强大的方法来使其成为决定性的。

#### Non-Canonical Methods

在实践中，之前的方法并不能带来一个线性时间决定性parser。一个方案是通过修改语法来使其适配方法，但是这意味着对生成的语法树也需要进行修补。另一个方法是推迟决定并继续使用一半的力量Parsing，这是非标准Parser。其中包含了最强大，最聪明，最复杂的决定性Parsing算法。

#### Generalized Linear Methods

对于无法构建决定性控制机制的语法，可以继续使用广度优先来解决。

#### Conclusion

### The “Strength” of a Parsing Technique

一个技术的强度说明的是它能支持多少的语法。或者说是一个语法为了能够被这个技术支持会有多容易。

语言约束越强，需要的技术就越弱。

### Representations of Parse Trees

Parsing可以能得到多个parse树，但是无法知道数量。缺失或过多准备树都是不好的。存在两种模型，生产者消费者模型和数据结构模型。

#### Parse Trees in the Producer-Consumer Model

生产者和消费者模型的问题在于需要定义谁是主程序谁是子程序。

一个解决方法是使用协程。

ref: Advanced Programming Language Design R.A. Finkel

协程的问题是依赖语言实现。

更可行的是线程，但是这些的问题在于引入了并不必要的并行概念。

通常的实现是将Parser作为主程序，消费者作为子程序。

对于使用消费者作为主程序会导致Parser的数据无法在栈上存在。

还有问题在于，消费者需要比较找出差异来做进一步的决定。此外，如果语法是无限歧义的，那么Parser会生成无限的Parse树。

生产者-消费者模型并不通用。

### Parse Trees in the Data Structure Model

Parser使用一个数据结构同时表示所有parse树。这可以只有三倍的空间复杂度。

有两种表示parse森林和parse森林语法。

### Parse Forests

最简单的方式是用一个根节点连接所有Parse树。
