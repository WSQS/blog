---
title: Harness engineering for coding agent users
date: 2026-04-16
url: https://martinfowler.com/articles/harness-engineering.html
tags:
  - AI
---

目的: 让 Coding Agent 在较少的监督下工作。

Harness 是 AI agent 中除了模型之外的东西。

在 Coding Agent的情况下，还可以区分出内置Harness和用户Harness。

用户 Harness 有两个目的，增加agent首次执行正确的机率和在用户看到之前尽可能自我修复尽可能多的错误。

## Feedforward and Feedback

对于提高首次执行的正确率，需要进行引导，预测模型的行为并在其行动前进行引导。

对自我修复，需要在模型行动之后进行观察。

这两个方面需要结合，因为它们各自又有自己能解决和无法解决的部分。

## Computational vs Inferential

存在两种执行类型，计算和推导。

## The steering loop

用户通过在 harness 中迭代来控制 agent。一个多次发生的 issue 应该通过 feedforward 和 feedback 两个部分来避免。

用户 Harness 工程是上下文工程的一个特殊形式。

## Timing: Keep quality left

对CI/CD的情况， Harness 有不同的作用。

### Feedforward and feedback in the change lifecycle

在修改的生命周期中，也可以区分前馈和反馈机制。

### Continuous drift and health sensors

在运行时也区分前馈和反馈机制。

## Regulation categories

Harness 可以被理解为是一个控制装置，通过前馈和反馈机制来调整代码库状态到理想的状态。这里的状态拥有各种不同的维度，这些维度中的可调节性和复杂度都不相同，通过区分可以进行更精确的描述。

### Maintainability harness

维护代码质量和可维护性是目前最容易处理的方面。

### Architecture fitness harness

这涉及到了适应度函数，适应度函数是用来衡量给定架构设计方案和目标之间距离的函数。这样的观念借鉴自进化计算。具体可以参见 Building Evolutionary Architectures。

ref: [Building Evolutionary Architectures](http://www.thoughtworks.com/books/building-evolutionary-architectures)

### Behaviour harness

对 Agent 行为的约束也可以从前馈和反馈两个方面进行。

但是 Agent 行为也并不理想。

## Harnessability

可操纵性也受到代码库本身的依赖，强类型语言，模块边界定义，细节隐藏这些特性可以提升 Agent 的成功机率。新项目和旧项目也存在差异。这可以被称作环境适宜性。

## Harness templates

大部分的代码都是模板化的架构，这也可以发展出 Harness 对应版本。

定义拓扑结构来减少多样性。

## The role of the human

辅助工具尝试外化和显式化人类开发人员中的要素。但是完整的系统是昂贵的，所以优秀的 Harness 并不是完全取代人类的参与，而是将人类的介入引导到最重要的地方。

## A starting point - and open questions

一些 Harness 的例子：

- [openai: harness-engineering](https://openai.com/index/harness-engineering/)
- [stripe: minions-stripes-one-shot-end-to-end-coding-agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents): 将反馈尽早纳入开发流程。
- 突变和结构化测试
- 在 Coding Agent 中整合 LSP 和 代码智能。
