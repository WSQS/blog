---
title: "cs143 05: Introduction to Parsing"
date: 2025-07-24
url: https://www.bilibili.com/video/BV1huRUYYEcw?p=5
tags:
  - algorithm
---

## Introduction to Parsing

正则语言：最广泛的、最弱的一类形式语言。

问题在于，正则语言无法处理例如平衡括号这样的问题。

有限状态机无法计数。

Input: sequence of tokens from lexer

Output: parse tree of the program

parse tree 可能是隐式的。

## Context-Free Grammars

Context-Free Grammar(CFG)

parser需要能够区分有效和无效的token串。

需要一个描述有效token串和无效token串的语言和区分有效和无效token串的方法。

编程语言中含有递归结构。

上下文无关文法是描述递归结构的自然符号。

CFG 组成

- A set of terminals
- A set of non-terminals
- A start symbol
- A set of productions

对于终止符，一旦出现就是不可更改的。通常就是tokens。

非终止符应该使用大写。

额外的需求

- 上下文无关文法无法将输入构建为语法树。
- 优雅处理错误。
- 一种CFG的实现。

语法的格式也是重要的，工具依赖于语法格式。

## Derivations

A derivations is a sequence of productions.

A derivation can be drawn as a tree. 根节点是起始符号。叶子节点是终止符，内部节点是非终止符。

对叶子节点进行中序遍历就可以得到原始输入。

语法分析树显示了运算的结合性。

left-most derivation: 每一步都替换最左侧的非终止符，类似的还有一个 right-most derivation。两者有相同的语法分析树。

一个语法分析树通常有多种推导方式。

## Ambiguity

同一个字符串可以有多种语法分析树。

当一个文法对同一个字符串有多种语法分析树的时候，它是ambiguous的。也就是说，对这个字符串有多个 left-most derivation 或 right-most derivation。

一个直接的解决方法是将文法重写的不再有歧义。

对于 if then else，希望 else 与最近的没有被匹配的then对应。所以可以区分已匹配的if和匹配的if。

但是无法自动将有歧义语法转换为无歧义语法。

为了简便可以使用有歧义文法，但是需要一些消除歧义的机制。也就是从多个语法分析树中判断出哪个是符合的。主流的做法就是这样。

常用的消除歧义的声明形式是优先级声明和结合性声明。

bison:

```
%left +
%left *
```
