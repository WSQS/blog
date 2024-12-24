---
title: "lecture 19: Geometry Introduction"
date: 2024-12-23
url: https://www.bilibili.com/video/BV1X7411F744?p=10
tags:
  - computer_graphics
---

## Applications if textures

纹理=内存+范围查询(过滤)

环境光照 Environment Map，假定光源无限远。

顶部底部扭曲。

凹凸贴图，法线贴图。定义表面存在根据纹理的上下起伏。

Perturb the normal

求出切线，随后求法线。

更近一步，位移贴图，给顶点真的做移动。要求三角形顶点足够细腻。对此的动态适配，DX存在支持。

纹理可以定义为三维的。一个三维空间中的噪声。

ref:柏林噪声

记录已经计算好的信息。

## Introduction of geometry

### Various representations of geometry

隐式几何：满足特定关系的点$f(x,y,z)=0$

难以采样

但是可以判定一个点是否在物体内和外

显式几何：可以通过参数映射得到所有点，但是难以判定一个点是在平面内还是平面外。

两者各有优劣，根据需要选择。

隐式几何：

- 数学公式
- CSG(Constructive Solid Geometry):基本元素的加减
- Distance Functions 距离函数：空间中任意一个点到物体表面的最短距离,水平集类似于等高线
- 分型

隐式函数表示很容易，容易判断内与外

易于与光线求交

容易处理拓扑关系。
