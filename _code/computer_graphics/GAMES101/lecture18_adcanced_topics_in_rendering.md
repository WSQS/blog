---
title: "lecture 18: Advanced Topics in Rendering"
date: 2025-01-06
url: https://www.bilibili.com/video/BV1X7411F744?p=18
tags:
  - computer_graphics
  - perlin_noise
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

非表面模型

#### Participating media

散射介质。特点在于散射光线是如何分布的。

随机选择方向弹射，随机选择方向前进。

手指其实也是散射介质。

#### Hair/ fur/ fiber(BCSDF)

头发。

高光:无色的高光和有色的高光。

Kajiya-Kay Model

Marschner Model:R,TT,TRT，将头发建模为类似玻璃的圆柱。

多次散射。

毛发

- Cuticle
- Medulla
- Cortex(动物拥有的更多)

闫令琪发明

Double Cylinder Model

R、TT、TRT、TTs、TRTs

#### Granular material

颗粒状材质

简化

### Surface models

#### Translucent material(BSSRDF)

半透明材质

玉石、水母

次表面散射，要考虑从各个方向进到其他点的光。

Dipole近似

#### Cloth

布料：一系列缠绕的纤维，两个层次。

近似于体积来运算。

直接渲染每一根纤维。

视为表面模型。

#### Detailed material(non-statistical BRDF)

有细节的材质。

模型过于完美。划痕。

计算量要求很大。

法线分布近似。

这种尺度时需要考虑波动光学，存在不连续的效果。

### Procedural appearance

程序化生成的外观。

三维空间噪声函数。

re:[柏林噪声](../perlin_noise.md)

木头，铁锈等材质。
