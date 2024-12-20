---
title: lecture08: Shading Shading
date: 2024-12-20
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
