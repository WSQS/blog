---
title: "lecture 14: Ray Tracing Light Transport"
date: 2025-01-02
url: https://www.bilibili.com/video/BV1X7411F744?p=15
tags:
  - computer_graphics
---

## Basic radiometry

- Radiant flux:电磁辐射能量(J)和通量(W 功率, lm 流明)
- Intensity: 单个立体角上的功率(cd)
- Irradiance: 单位面积上的功率(lux)，要投影到平面方向上，Lambert's Cosine Law正是基于此。
- Radiance: 单位立体角并且单位面积上，是前两者的结合。入射和发射。

微分立体角

Irradiance可以解释因为距离导致的衰减。

Irradiance和Radiance相差的是方向性。

## Light transport

Bidirectional Reflectance Distribution Function, BRDF: 双向反射分布函数

某个方向进来到某个方向去的反射强度。可以理解成入射的Irradiance如何分布到各个立体角上去。

BRDF定义了不同的材质。

### The reflection equation

反射方程：对某一个点，所有入射它的光线经过立体角求积分就能得到这个点的反射光线值。

问题：反射本身也会被反射，会发生递归。

### The rendering equation

渲染方程：反射方程的基础上添加上物体本身的发光。

渲染方程是一个Integral Equation

$l(u)=e(u)+\int l(V)K(u,v)dV$

## Global illumination

可以简化为$L=E+KL$，也就是物体发出的光是自发光加上对发出的光的反射。

也就可以写成$L=(I-K)^{-1}E$，随后可以展开成$L=(I+K+K^2+K^3+...)E=E+KE+K^2+K^3+...$，也就是直接看到光源，再加上后续的反射。最终的结果就是全局光照。前两项就是光栅化。

## Probability Review

- 随机变量:X
- 分布:$X~p(x)$
- 概率
- 期望
- 概率密度函数(Probability Distribution Function, PDF)
