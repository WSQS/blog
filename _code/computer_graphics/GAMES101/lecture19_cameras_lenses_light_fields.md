---
title: "lecture 19: Cameras, Lenses and Light Fields"
date: 2025-01-09
url: https://www.bilibili.com/video/BV1X7411F744?p=19
tags:
  - computer_graphics
---

Imaging = Synthesis + Capture

计算摄影学

## Camera

小孔成像

- Shutter:快门
- Sensor:记录 Irradiance

### Pinhole Camera

针孔相机

并不会虚化和景深。

### Field of View

视场

$FOV = 2 \arctan(\frac{h}{2f})$，和传感器大小和焦距有关。以35mm胶片为基础。

## Exposure

曝光。

$Exposure = Time \times Irradiance$

时间由快门决定。运动模糊。运动模糊并不总是糟糕的，可以反走样。Rolling Shutter会扭曲旋转的螺旋桨。

Irradiance由光圈和焦距决定。

光圈：f-stop f数控制。FN或F/N，两者一致。是直径分之一。

ISO gain 增益，白平衡，对于暗的图，会放大噪声。线性增加。

景深和运动模糊不可兼得。

## Fast and Slow Photography

高速摄影，短快门时间+大光圈。

超低速摄影，延时摄影。“拉丝”

## Thin Lens Approximation

薄透镜近似。

透镜会散光。

- 过焦点变平行光
- 平行光变过焦点
- 焦距可以被任意修改

物距相距关系：$\frac{1}{f} = \frac{1}{z_i} + \frac{1}{z_o}$

景深

Circle of Confusion

物体不在焦平面上就会出现一片光。

大光圈会更模糊。和光圈成正比。

F数是焦距除以光圈的直径。

渲染薄透镜。

进行一次光线转换。

## Depth of Field

景深。

场景中的一段深度，在镜头上CoC都比较小。
