---
title: "lecture 14: Ray Tracing Acceleration"
date: 2024-12-26
url: https://www.bilibili.com/video/BV1X7411F744?p=14
tags:
  - computer_graphics
---

ref:GTC

DLSS 2.0

RTXGI：实时全局光照技术

## Using AABBs to accelerate ray tracing

1. 找到包围盒
2. 创建格子
3. 存储包含物体的格子

对格子进行判断。找到相遇的格子，类似于光栅化一条直线的逻辑。

大概划分到27个格子就行。

### Uniform grids

场景中物体分布不均匀不适合使用格子。

### Spatial partitions

空间划分。

Oct-Tree:八叉树

KD-Tree:只砍一刀

BSP-Tree
