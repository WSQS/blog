---
title: "Lecture 03: Transformation"
date: 2024-12-11
url: https://www.bilibili.com/video/BV1X7411F744?p=3
tags:
  - computer_graphics
---

## Why study transformation

Modelling：模型变换

Viewing：视图变换

## 2D transformations: rotation, scale, shear

### Representing transformations using matrices

缩放变换：对角矩阵，值为scale，值不同可以进行不均匀缩放。

### Rotation, scale, shear

Shear Matrix：切变。$\begin{bmatrix} 1 & \alpha \\ 0 & 1 \end{bmatrix}$

旋转变换：以原点为圆心，逆时针为正方向。$\begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$

## Homogeneous coordinates

齐次坐标是为了支持平移，而不是将平移变换作为一个特殊的变换。

2d point: $(x, y, 1)^T$

2d vector: $(x, y, 0)^T$

含义：向量具有平移不变性。

向量+向量=向量

点-点=向量

点+向量=点

因为也有$(x/w, y/w, 1)^T$，所以，点+点=中心点

逆变换即是逆矩阵。

仿射变换最下方必定是001。

## Composing transformations

因为矩阵运算不满足交换律，所以变换进行的顺序是会影响变换的结果的。

变换矩阵在向量的右侧，变换矩阵会从右向左逐个变换。反过来，利用矩阵的结合律，也可以认为是将变换矩阵合成成一个变换再对向量进行这个操作。

分解复杂变化。例如：以固定点进行旋转。

三维空间中的变换可以类比二维变换。可以添加一个维度，组成齐次式。类似的，对于$(x, y, z, w)^T$，对应的点为$(x/w, y/w, z/w, 1)^T$。

仿射变换的矩阵是先进行的线性变换后进行的平移。
