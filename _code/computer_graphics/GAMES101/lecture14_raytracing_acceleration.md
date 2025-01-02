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

Oct-Tree:八叉树、依赖维度

KD-Tree:只砍一刀

BSP-Tree:不是横平竖直的砍

KD-Tree：会形成树，只需要在叶子节点存储对象。

问题：

- 难以判断三角形是否和包围盒存在交集。
- 一个物体可能在多个叶子节点当中。

### Object Partitions & Bounding Volume Hierarchy

划分物体而非空间。

减少重叠。

- 选择一个维度去进行划分
- 总是选择节点的最长轴
- 取中间的那个节点来进行划分($O(n)$复杂度，快速选择算法)

## Basic radiometry

辐射度量学

- 精准的光学物理量。准确测量光在空间中的属性
- Radiant flux:电磁辐射能量(J)和通量(W,lm 流明)
- Intensity:单个立体角上的功率(cd)
- Irradiance:接收到的强度
- Radiance:传播中的强度

- Why
- What
- How

ps:led标注的功率是相当于白炽灯的功率，实际的功率会低得多。
