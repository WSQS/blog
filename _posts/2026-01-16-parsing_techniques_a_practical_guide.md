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
