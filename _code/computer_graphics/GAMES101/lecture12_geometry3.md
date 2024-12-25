---
title: "lecture 12: Geometry3"
date: 2024-12-25
url: https://www.bilibili.com/video/BV1X7411F744?p=12
tags:
  - computer_graphics
---

## Mesh Operations

- Mesh Subdivision：上采样
- Mesh Simplification：下采样
- Mesh Regularization

### Subdivision

位移贴图

引入更多三角形，同时优化他们的位置。

Loop Subdivision

区分新的顶点和旧的顶点，新的顶点调整到周围点的加权平均，旧的顶点是自己和周围顶点的加权平均。

Catmull-Clark Subdivision

对一般网格生效

对线与面取中点，连接。非四边形面都消失了，变成奇异点。

面上的点、边上的点加权平均，旧的点也进行平均。

### Simplification

边坍缩

Quadric Error Metrics：二次误差度量。

从二次度量误差最小的边开始，取最小同时动态更新。优先队列和堆。

## Shadow mapping

光栅化解决阴影问题。

是图像空间算法

存在走样

关键思想：点如果不在阴影当中，那么这个点必须同时被相机和光源看到。

点光源：硬阴影。

- Render from Light，记录深度
- Project to light

非常广泛使用

硬阴影：锐利的边缘

软阴影：模糊

Penumbra
