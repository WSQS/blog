---
title: "lecture 13: Ray Tracing Whitted-Style Ray Tracing"
date: 2024-12-25
url: https://www.bilibili.com/video/BV1X7411F744?p=13
tags:
  - computer_graphics
---

原因：光栅化不能很好的处理全局的效果。

- 软阴影
- 金属反射
- 间接光照

光栅化快且质量低

光线追踪准确但是十分慢，通常是离线的

## Basic Ray-Tracing Algorithm

定义光线

- 沿着直线传播
- 不会与其他光线发生碰撞
- 从光源出来到达人眼，是可逆的(reciprocity)

Ray Casting

假定折射是完美的。

eye ray与物体相遇，判断该点是否会被照亮，这样和光栅化结果近似。

Whitted-Style：光线弹射、折射多次，递归，每一个点都被计算着色，会考虑能量衰减,进行相加。

primary ray

secondary ray

shadow ray

## Ray-Surface Intersection

Ray Equation：起点+方向

$r(t)=o+td$

光线与球的交点。交点是满足两个函数的点。

推广，光线和隐式表面的交点。牛顿法。

显式表面，光线和三角形求交。首先求光线和平面求交，随后求点是否在三角形内。可以直接得到解析解。

Moller Trumbore Algorithm

光线+重心坐标系
