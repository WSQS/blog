---
title: Game Engine Architecture
date: 2025-04-04
---

## Preface

游戏引擎与游戏之间的界限是模糊的。

ref: Effective STL

ref: Effective C++

## Foundations

### Introduction

#### Structure of a Typical Game Team

- Engineers
- Artists
- Game designers
- Producers
- Support Staff

#### What is a Game?

主要关注于第一人称射击、第三人称动作和平台、竞速、格斗这些类型的游戏。*确实在这些游戏当中涉及到了想当一部分的共性，而这些共性可以被抽象成游戏引擎。因此，是先有游戏然后才有游戏引擎的，同时，这样产生的游戏引擎也就注定是对于一些更为特殊的游戏类型是较为无力的。*

##### Video Games as Soft Real-Time Simulations

soft real-time interactive agent-based computer simulations.

simulations: 游戏采用近似和简化的方法来模拟世界。

agent-based: 游戏中存在一定数量的的实体。

temporal simulation: 游戏世界的状态会动态变更

interactive: 游戏会对玩家的输入做出反应。

real-time: 实时系统需要一个刷新频率。对于游戏来说，它包含了多种不同的刷新频率。

soft real-time: 没有赶上deadline并不是一个严重的问题。

numerical: 游戏引擎是进行数值计算的，因为对于多数问题，并不存在解析解。

#### What Is a Game Engine?

Doom 区分了核心软件组件和美术资产、游戏地图、游戏规则。这使得玩家可以创作新的游戏，形成了mod社区。使用游戏引擎进行开发比独立直接开发更加的经济。

游戏引擎与游戏之间的界限是模糊的。

data-driven architecture 区分游戏引擎和游戏。

游戏引擎无法用于制作所有游戏。一个普遍的游戏引擎难以对特殊情况进行优化。A game can always be made more impressive by fine-tuning the engine to the specific requirements and constraints of a particular game and/or hardware platform.

#### Engine Differences across Genres

- FPS
- Platformers and Other Third-Person Games
- Fighting Games
- Racing Games
- Strategy Games
- MMOG
- Player-Authored Content
- Virtual, Augmented and Mixed Reality

#### Game Engine Survey

- The Quake Family of Engines
- 
