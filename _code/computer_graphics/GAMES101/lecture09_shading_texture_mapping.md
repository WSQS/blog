---
title: "lecture 09: Shading Texture Mapping Cont."
date: 2024-12-23
url: https://www.bilibili.com/video/BV1X7411F744?p=9
tags:
  - computer_graphics
---

## Barycentric coordinates

为了插值。

$\alpha + \beta + \gamma =1$

非负则在三角形内。

可以通过组成的面积求值。

重心值为$(\frac{1}{3},\frac{1}{3},\frac{1}{3})$

可以直接用重心坐标进行插值。

注意：重心坐标并不能投影后不变。应该现在三维空间中进行重心坐标计算，随后再进行插值。

## Applications of textures


纹理放大：最近邻算法、双线性插值、双三次插值（取周围16个）

texture:纹理元素

纹理缩小：发生走样，有锯齿和摩尔纹

mipmap：点查询->范围查询

不同的像素对应的是不同大小的尺寸。

Mipmap允许快速、近似、方向范围查询。

多了三分之一的存储量。

像素查询区域近似成正方形，得到对应的MipMap层级。也可以由此进行三线性插值。

局限性，远处的Overblur。一种解决方法：各向异性过滤，可以转变为矩形区域，开销是原本的三倍。

但是对与倾斜的区域，仍然会有问题，解决方法：EWA过滤，使用圆形。
