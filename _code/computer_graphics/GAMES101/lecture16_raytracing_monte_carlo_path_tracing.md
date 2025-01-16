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

引入间接光照，对于非光源的情况，再求一次该点的直接光照。

问题：

- 光线数量指数级递增:N=1时就不会爆炸，这时就是路径追踪。可以通过对足够多的路径进行平均来解决噪声的问题。
- 递归的求解，算法无法停止: 俄罗斯轮盘赌(Russian Roulette, RR)，一定概率停止向下追踪，并将得到的值除以概率P，这样的平均的期望值还是原本的值。

并不高效，优化：让蒙特卡洛算法尽量在光源上进行采样，需要把渲染方程写成在光源上的积分，也就是将$dA$映射到$dw$。

$$L_O(p,w_O)=\int_{A} L_i(p,w_i)f_r(p,w_i,w_o)(n\cdot w_i)\frac{\cos\theta\cos\theta'}{\left| \left| x'-x \right| \right|^2}$$

可以将一个点受到的光分成直接光照和间接光照，前者不需要用俄罗斯轮盘赌进行求解。

问题：光源可能被遮挡解决：需要进行遮挡检查。

路径追踪几乎与现实一模一样。照片级真实感。

光线追踪如今是一个十分宽泛的概念。

ref:[Physically Based Rendering book](https://www.pbr-book.org)

一些遗留的问题：

- 如何对一个半球面进行均匀采样，以及如何对任意函数进行采样
- PDF的最佳选择：重要性采样理论
- 随机数的选择：low discrepancy sequences
- 对半球采样和光源采样进行结合: multiple imp. sampling
- 像素加权算法:pixel reconstruction filter
- 计算得到的radiance并不是颜色，还需要进行gamma矫正，曲线，颜色空间。

> Fear the science, my friends.
