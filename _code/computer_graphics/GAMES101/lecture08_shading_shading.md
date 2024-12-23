---
title: "lecture 08: Shading Shading"
date: 2024-12-20
url: https://www.bilibili.com/video/BV1X7411F744?p=8
tags:
  - computer_graphics
---

## Blinn-Phong reflectance model

### Specular term

高光项

接近镜面反射。也就是半程向量(h)和法线(n)接近，这是Blinn-Phong相对Phong模型的改进。

$L_s=k_s(I/r^2)\max(0,n\cdot h)^p$

### Ambient term

环境光照项

$L_a=k_aI_a$

$L=L_a+L_d+L_s$

ref:Radiometry

## Shading frequencies

着色频率：着色要应用在哪些点上。

面、顶点、每一个像素

- Flat shading：都是平面，不利于平滑
- Gouraud shading：顶点进行着色，随后插值
- Phong shading：对法线方向进行插值，随后对每个点进行着色

定义每一个顶点的法线：顶点法线是所有面的法线求平均。

更近一步，根据三角形面积进行加权平均。

定义每一个像素的法线：使用重心坐标系对顶点法向的插值

## Graphics pipeline

也可以成为Real-Time Rendering Pipeline，是以上操作的集合。

- 顶点处理
- 三角形处理
- 光栅化
- 像素处理
- 帧缓冲处理

先处理顶点投影再处理三角形是因为模型定义是先定义所有顶点，再定义哪些顶点能够组成三角形。

着色涉及到了顶点处理和像素处理，取决于着色频率。

纹理映射也涉及到顶点处理和像素处理。

Shader程序

GLSL

顶点着色器

片段着色器、像素着色器

re:Shader toy

GPUs

几何着色器

计算着色器

GPU是高度并行处理器

## Texture Mapping

纹理映射：定义物体表面任何一个点的任何属性。

物体表面是2维的。

纹理是2维图片。

ref:参数化几何学的

纹理坐标系：UV~$[0,1]^2$

纹理可以被重复使用。

平铺算法：wang tiling

已知三角形三个顶点的UV，通过重心坐标系进行插值得到其内部任何一个顶点的UV。
