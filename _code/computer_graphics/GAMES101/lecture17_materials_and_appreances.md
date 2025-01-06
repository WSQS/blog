---
title: "lecture 17: Materials and Appearances"
date: 2025-01-03
url: https://www.bilibili.com/video/BV1X7411F744?p=17
tags:
  - computer_graphics
---

外观是材质和光线共同作用的结果。

re:业界顶尖的渲染器 Weta Digital - Manuka

图形学中的材质:BRDF

## Diffuse/Lambertian Material

漫反射材质。如果不吸收，接收多少Irradiance，就均匀发出多少Irradiance。

$$f_r=\frac{\rho}{\pi}$$

$\rho$是albedo，反射率。

## Ideal reflective/refractive material

反射角度的两种计算。

## Specular Refraction

Snell's Law:斯涅尔定律计算折射角

没有折射会发生全反射

Snell's Windows/Circle

BSDF=BRDF+BTDF

菲涅尔项:反射强度和入射光线与法线的角度有关

Schlick's approximation

## Microfacet Material

微表面模型

- 从远处看：平面&粗糙
- 从近处看：起伏&光滑

关键：微平面法线的分布。

- 微平面法线比较集中，就是glossy材质。
- 微平面法线比较分散，就是漫反射材质。

$$f(i,o)=\frac{F(i,h)G(i,o,h)D(h)}{4(n,i)(n,o)}$$

$F(i,h)$是菲涅尔项

$G(i,o,h)$几何项，微表面之间的互相遮挡，Grazing Angle:掠射角度，避免边界特别亮

$D(h)$是法线分布

可以表示金属、皮革、木材

## Isotropic/Anisotropic Materials

- 各向同性：微表面不存在方向性
- 各向异性：微表面存在方向性

结果会随方位角旋转发生变化的材质是各向异性材质。

金属、尼龙、天鹅绒

## Properties of BRDFs

- Non-negative
- Linearity:可以将结果相加
- Reciprocity principle:可逆性
- Energy conservation: 能量不会增加

## Measuring BRDFs

测量仪器:Gonioreflectometer

各向同性可以减少一个维度。

ref:MERL BRDF Database: 测量很多材质的BRDF
