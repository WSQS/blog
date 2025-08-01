---
title: "cs143 06: Syntax-Directed Translation"
date: 2025-07-29
url: https://www.bilibili.com/video/BV1huRUYYEcw?p=6
tags:
  - algorithm
---

## Error Handling

编译器有两个任务：识别不正确的代码，翻译正确的代码。此外，编译器还需要未错误的程序提供良好的反馈。

编程语言有很多不同类型的错误。

- Lexical: 词法分析错误
- Syntax: 语法分析错误
- Semantic: 语义错误类型检查
- Correctness: 运行结果和预期不一样

- 编译器应该准确清楚的报告错误
- 编译器应该快速从错误中恢复
- 编译器应该不因为错误而降低编译有效代码的速度

三种模式

- Panic mode: 最简单最流行
- Error production
- Automatic local or global correction

Panic mode: 最简单最流行

编译器在找到一个明确角色的token之前丢弃所有token。并在那之后继续。特殊的token被称作synchronizing tokens.

Bison中的error关键字。

Error productions: 将已知的常见错误定义为语法中的代替产生式。这会将语法变得复杂。
