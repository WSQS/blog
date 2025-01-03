---
title: "lecture 16: Ray Tracing Monte Carlo Path Tracing"
date: 2025-01-03
url: https://www.bilibili.com/video/BV1X7411F744?p=16
tags:
  - computer_graphics
---

渲染方程

连续性随机变量、概率密度函数

## Monte Carlo Integration

蒙特卡洛积分是用来求解定积分的。并不是解析，而是数值求解。

黎曼积分：将曲线拆分成多个小长方形。

蒙特卡洛采用在积分域内随机采样来近似等于积分结果。

定积分：$\int_a^bf(x)dx$

随机变量：$X_i\sim p(x)$

蒙特卡洛近似：

$$F_N=\frac{1}{N}\sum_{i=1}^{N}\frac{f(X_i)}{p(X_i)}$$

一种特殊情况，随机变量均匀采样。

- 采样次数越多，结果越准确
- 在x上采样在x上进行积分，两者要保持一致。

## Path Tracing

路径追踪

Whitted-style ray tracing:

- 对于光滑物体总是进行反射折射
- 对于粗糙物体上停止弹射

路径追踪是为了解决Whitted-style ray tracing当中一些不准确的近似。

- Glossy的物体应该两者兼而有之。
- 漫反射的反射被忽略了。color bleeding

渲染方程是准确的。

求解渲染方程的困难：

- 对半球面进行积分
- 递归求解

使用蒙特卡洛算法对问题进行求解。

首先求解某个点的直接光照。

$$L_O(p,w_O)=\int_{\Omega +} L_i(p,w_i)f_r(p,w_i,w_o)(n\cdot w_i)dw_i$$

使用蒙特卡洛算法进行积分，可以得到：

$$L_O(p,w_O)=\frac{1}{N}\sum^N_{i=1}\frac{L_i(p,w_i)f_r(p,w_i,w_o)(n\cdot w_i)}{p(w_i)}$$

注意，这里的i有两种含义。
