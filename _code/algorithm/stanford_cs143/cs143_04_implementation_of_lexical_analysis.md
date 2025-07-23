---
title: "cs143 -4: Implementation of Lexical Analysis"
date: 2025-07-16
url: https://www.bilibili.com/video/BV1huRUYYEcw?p=3
tags:
  - algorithm
---

## Lexical Specifications

希望做到的：将输入的字符串划分为符合正则表达式的字串。因此需要对正则表达式进行拓展。

- 为每一类lexemes编写正则表达式
- 实现一个更大的正则表达式，匹配所有的lexemes
- 对前i个字符，判断是否符合正则表达式子。如果符合，则去除，并重复。

对于前i个和前j个字符都符合的情况，总是应该选择更长的那个。这是最大匹配原则(Maximal Match)。

对于前i个字符符合两钟正则表达式的情况，这个需要根据优先级排序，并选择优先级更高的。

对于规则不适配的情况，需要设计合适的错误反馈。可是设计一个错误规范，将不符合的字符串都放入其中，并将其优先级调整到最低。

最大匹配原则和最高优先级原则会有冲突。

已有的算法可以只遍历一次输入，并只是简单的查表来完成词法分析。

*对于NFA和DFA，最大匹配原则应该关注最后一个匹配然后就不匹配的字符串。*

## Finite Automata

有限状态机是正则表达式的一个很好的实现模型。

有限状态机的组成

- 输入字母表
- 有限状态集合
- 开始状态
- 接收状态
- 状态转移

如果输入在输入状态结束，那么说明输入是合法的。否则就是拒绝。

$\epsilon$-moves: 不需要输入就可以进行状态切换。

确定有限状态机(Deterministic Finite Automate, DFA): 无$\epsilon$-moves并且每个状态的每个输入，状态机只有一个转换。

对DFA，同一输入的状态转移路径是确定的。

对NFA，只需要找到一条接受的路径就可以了。在同一时刻，NFA可以进入多种状态。

NFA和DFA有同等的处理正则语言的能力。

DFA执行更快，NFA更小。

## Regular Expressions to NFAs

流程

- 词法规范
- 正则表达式
- NFA
- DFA
- Table-dirven Implementation of DFA

将正则表达式转换成NFA，可以实现拼接、并集、*。

## NFA to DFA

$\epsilon$-closure: 将$\epsilon$变化到达的状态组合起来。

将NFA状态切换到DFA。NFA的状态组合本身可以被看成值DFA的一个状态。

DFA states: subsets of S, except the empty set.

DFA start state: $\epsilon$-closure of start state

DFA final state: $\{X|X\cup F\neq\empty\}$

DFA transition function: $Y=\epsilon-clos(a(X))$

## Implementing Finite Automata

并不一定通过DFA实现，也可以直接通过NFA实现。

DFA可以通过二维表实现。分别是起始状态和输入字符，表格中的内容是下一个状态。其实也可以通过2维来表征有向图来表征。可以复用数据来减少内存占用。

NFA实现的表格会小得多，但是执行速度会慢得多。
