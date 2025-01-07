---
title: "lecture 18: Advanced Topics in Rendering"
date: 2025-01-06
url: https://www.bilibili.com/video/BV1X7411F744?p=18
tags:
  - computer_graphics
---

## Advanced Light Transport

Unbiased & Biased: 无偏的与有偏的，期望的值与准确值是否一致。

consistent： 一致的，有偏，但是在极限情况下是有偏的。

### Unbiased light transport methods

#### Bidirectional path tracing(BDPT)

双向路径追踪

- 光源和相机都会发出一些sub-path
- 连接两个sub-path的终点

- 适合在光的方向光路比较复杂的情况
- 难以实现并且速度较慢

#### Metropolis light transport(MLT)

利用马尔科夫链进行采样，可以用任意的PDF函数。

善于找到局部路径。

- 适合复杂的光线
- 无偏的

- 难以估计收敛时间
- 通常会得到比较脏的结果
- 通常不会用来渲染动画

### Biased light transport methods

#### Photon Mapping

光子映射，有偏

从光源发出光，知道光达到漫反射的地方，收集光所在的地方。计算局部密度估计。光子数量太多会变得模糊，也就是有偏的，足够多光子时会足够准确，因此是consistent的。

- 适合渲染 Caustics：聚焦(聚散)
- 适合渲染 SDS(Specular-Diffuse-Specular)

#### Vertex connection and merging(VCM)

结合BDPT和Photon Mapping。

关键想法

- 不要浪费BDPT中两个相近的点

### Instant radiosity(VPL/ many light methods)

实时辐射度算法

已经被照亮的面被认为是新的光源

- 高效并且效果不错
- 缝隙中容易发光，和距离平方项有关
- 不能处理glossy材质

## Advanced Appearance Modeling

### Non-surface models

#### Participating media

#### Hair/ fur/ fiber(BCSDF)

#### Granular material

### Surface models

#### Translucent material(BSSRDF)

#### Cloth

#### Detailed material(non-statistical BRDF)

### Procedural appearance
