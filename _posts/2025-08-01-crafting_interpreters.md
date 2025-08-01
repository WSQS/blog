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

### Scanning

也就是lexing或lexical analysis。
