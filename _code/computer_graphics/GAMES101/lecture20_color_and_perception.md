---
title: "lecture 20: Color and Perception"
date: 2025-01-10
url: https://www.bilibili.com/video/BV1X7411F744?p=20
tags:
  - computer_graphics
---

Linux: SimpleScreenRecorder

## Light field/ Lumigraph

ref:SIGGRAPH 2012

The Plenopic Function: parameterize everything that he can see.

$P(\theta,\phi,\lambda,t,V_X,V_Y,V_Z)$

光场是全光函数的部分。是在任何一个位置往任何一个方向去的光的强度，二维的位置，二维的方向。可以用两个平面来定义任何一个光场。u,v,s,t。

光场相机，微透镜，支持后期重新聚焦。可以虚拟的移动摄像机的位置。

问题：

- 分辨率不足
- 成本高
- 计算机图形学需要权衡

## Physical Basis of Color

### What is color

色散。颜色的合成。

光谱。谱功率密度(SPD)支持线性组合。

### Color Perception

颜色是基于人的感知的。

视网膜。棒状细胞和锥形细胞。三种锥形细胞。人眼的锥形细胞的分布差异非常大。人看到的不是光谱，而是SML

### Color reproduction/ matching

Metamers: 同色异谱现象

用颜色的混合去表示另一种颜色。

加色系统。

CIE RGB 颜色匹配。

### Color space

颜色空间。

sRGB

CIE XYZ，绿色可以表示亮度。

Gamut:色域，一个颜色空间所有的颜色。

### Perceptually Organized Color Spaces

HSV，颜色拾取器。色调(Hue)、饱和度(Saturation)、亮度(Value)。

CIELAB空间，互补色，可以通过视觉暂留实现。

颜色都是相对的。

减色系统。CMYK，带上黑色是因为黑色墨水比较便宜。
