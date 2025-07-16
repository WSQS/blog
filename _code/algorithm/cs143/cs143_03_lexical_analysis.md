---
title: "cs143 03: Lexical Analysis"
date: 2025-07-16
url: https://www.bilibili.com/video/BV1huRUYYEcw?p=3
tags:
  - algorithm
---

## Lexical Analysis

将字符串分割成词法单元。

划分token类型: Identifier, Keywords, `(`, `)`, Number

Token类型是字符串的集合。

- Identifier: 标识符
- Integer:
- Keyword: `if` `else` `begin`
- Whitespace: a non-empty sequence of blanks, newlines, and tabs

基于字串类型区分程序。

将token传递到parser中，token是`<class, string>`。

Token Classes: whitespace, keyword, identifier, number, operator

lexeme: 词位

token:`<token class, lexeme>`

## Lexical Analysis Examples

FORTRAN rule: Whitespace is insignificant.

Goal: Partition the string. 需要额外向前多看一些，最好多向前看的数量是固定的。

PL/1 rule: keywords are not reserved
