---
title: The Early History Of Smalltalk
date: 2025-10-16
url: https://worrydream.com/EarlyHistoryOfSmalltalk/
tags:
  - smalltalk
---

## Abstract

绝大多数想法来自之前已有的想法。

Smalltalk是新思想的完整实现，计算机是个人学习、思考与表达的工具，而不是更强的计算机器。

## Introduction

Smalltalk是更大的被称为个人计算(personal computing)的追求的一部分。

编程语言可以分成两类，一类是特性拼凑`agglutination of features`，另一类是风格结晶`crystallization of style`。后者有清晰的核心思想，而前者没有。前者通常由委员会设计，而后者由一个人主导。

Smalltalk的设计是基于我们所有可以描述和呈现的事物都可以通过一种行为构建块的递归组合来表示。状态和过程被隐藏在块内，对块的交互只通过消息交换。

哲学上说，Smalltalk的对象和莱布尼兹的单子比较接近。同时，Smalltalk的类也是对象，这和柏拉图的理念论比较接近，类型本身也有类型Mateclass,这个类则是自己表示自己的。

Smalltalk的每一个对象都像是一个小型的计算机。开始先确定接口，对实现的关注可以推迟。

Smalltalk的贡献是面向对象的设计范式。

## 1960-66—Early OOP and other formative ideas of the sixties

OOP的两个核心动力：

- 寻找一个对于复杂系统更优的模块结构，允许隐藏实现细节
- 寻找一个更灵活版本的指派

新思想的接受过程，包括内部和外部。

1961年，对文件进行特殊处理，包含三个部分，第一部分是运行指令的指针，第二部分是各个运行部分，第三部分是任意尺寸和形式的数据。

分段存储系统。调用函数接口而不是直接操作指针。

### Sketchpad and Simula

ARPA组织和Utah的主要目标是解决3d图像的隐藏线问题。

计划`Sketchpad: A man-machine graphical communication system`，其中的巨大的想法，发明了现代交互式计算机图像，图像使用`master painting`绘制`instance drawing`，提供限制。

Simula语言。和Sketchpad类似，也有对象的概念，但是使用命令式的方式控制对象。

命令控制对象的想法改变了一切。

## 1967-69—The FLEX Machine, a first attempt at an OOP-based personal computer

个人电脑，FLEX machine，面向非计算机专业的用户，类似JOSS和Wirth的EULER。特点是动态模拟和动态拓展。

借鉴EULER，使用byte-code执行，简化Simula。

### Doug Engelbart and NLS

个人计算`personal computing`。Doug Engelbart提出计算机是强化人类智能的工具。FLEX机器接受了这些观点。

人机交互的概念和摩尔定律的结合产生了震撼的效果。给多数人使用的设备是颠覆性的概念。
