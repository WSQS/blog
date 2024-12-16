---
title: "lecture 05: Rasterization Triangles"
date: 2024-12-13
url: https://www.bilibili.com/video/BV1X7411F744?p=5
tags:
  - computer_graphics
---

## Finishing up viewing

### Viewport transformation

透视投影需要定义一个frustum，宽高比，FOV(Field of View)。长宽比和FOV可以互相转换。

MVP变换之后需要将最终生成的立方体投影到屏幕上。

屏幕是像素组成的数组，数组的形状就是分辨率。

Raster是德语当中的屏幕。

Rasterize是向屏幕上绘画的过程。

Pixel是 picture element。

屏幕空间：左下角是(0,0)，像素的中心需要加0.5。

映射矩阵：$\begin{bmatrix} \frac{width}{2} & 0 & 0 & \frac{width}{2} \\ 0 & \frac{height}{2} & 0 & \frac{height}{2} \\ 0 & 0 & 1 & 0 \\0 & 0 & 0 & 1 \end{bmatrix}$

## Rasterization

### Different raster displays

绘画机器：绘图机器、激光切割机

示波器 re:[How To Draw Mushrooms On An Oscilloscope With Sound](https://www.youtube.com/watch?v=rtR63-ecUNo)

阴极射线管(CRT)屏幕：逐行扫描、隔行扫描。

现代显示器：显存当中的Frame Buffer映射到屏幕上。

LCD：液晶显示器，涉及到光的偏振、旋光性。

LED：发光二极管

电子墨水屏

### Rasterizing a triangle

三角形是基础图元

- 是最基本的多边形
- 其他多面体可以拆成三角形
- 三个点必然组成一个平面
- 内外定义清晰
- 容易插值（重心坐标系barycentric coordinates）

判断一个像素和三角形的位置关系。

一个简单的方法：采样，利用像素中心对屏幕空间进行采样。

使用叉乘判断一个点是否在三角形内部。

边界条件：可以任意处理。

优化：只在包围盒内进行遍历。

像素：由rgb进行排布。baier排布方法，绿色点更多。

打印。

锯齿。Aliasing，Jaggies。
