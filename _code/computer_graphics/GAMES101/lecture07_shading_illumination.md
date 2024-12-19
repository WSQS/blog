---
title: "lecture 07: Shading Illumination"
date: 2024-12-17
url: https://www.bilibili.com/video/BV1X7411F744?p=7
tags:
  - computer_graphics
---

## Visibility/ occlusion

直观思路：画家的算法

从后向前进行绘制，覆盖framebuffer。

问题：存在互相遮盖的情况。

### Z-buffering

解决：引入深度缓存，记录每个像素的最小深度值。

需要对深度值添加一个额外的缓存。

假定Z总是为正，小就是近，大就是远。

绘制顺序无关。

最重要的可见性算法。

## Shading

Shading：着色。引入明暗与颜色。

对不同物体应用不同材质。

### Illumination & Shading

A Simple Shading Model: Blinn-Phong Reflectance Model

- 高光
- 漫反射
- 环境光（间接光）

shading point

三个方向：观察方向、法向、光源方向

表面参数：颜色、反光度（光泽度）

shading is local: no shadows will be generated.没有阴影

Diffuse Reflection：漫反射 Lambert强度$\cos{\theta}$

光强是平方反比衰减。

综上，漫反射强度可以定义为$L_d = k_d(I/r^2)\max(0,n \cdot l)$
