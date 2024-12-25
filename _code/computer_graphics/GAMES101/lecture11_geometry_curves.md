---
title: "lecture 11: Geometry Curves"
date: 2024-12-25
url: https://www.bilibili.com/video/BV1X7411F744?p=11
tags:
  - computer_graphics
---

## Explicit Representations

- 点云，之后会用于会变成多边形面
- 多边形面：额外的数据结构(Wavefront Object File(.obj) Format 点、法线、纹理坐标、连接关系)

## Curves

相机路径

### Bezier curves

贝塞尔曲线

只经过起止点

### De Casteljau's algorithm

找t时刻的点。

递归。伯恩斯坦多项式。

n个点是n-1阶多项式。

- 必过起点和重点
- 起点方向和终点方向与第2个点和倒数第二个点相对边界点有关
- 对控制点做仿射变换与对贝塞尔曲线进行仿射变换曲线不变
- 贝塞尔曲线一定在控制点构成的凸包内

逐段的三次贝塞尔曲线，四个控制点进行控制。可以定义方向。

连续性:$C^0$、$C^1$

### B-splines, etc.

样条线：可控曲线

B-Spline:基函数样条

是b样条线的升级版本。

NURBS

ref:[清华大学-计算机图形学基础](https://www.bilibili.com/video/av66548502/)

## Surfaces

### Bezier surfaces

在两个方向上使用贝塞尔曲线

uv

### Triangles & quads

#### Subdivision, simplification, regularization

- 细分
- 简化
- 正则化