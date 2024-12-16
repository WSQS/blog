---
title: "lecture 04: Transformation Cont."
date: 2024-12-11
url: https://www.bilibili.com/video/BV1X7411F744?p=4
tags:
  - computer_graphics
---

ref:Fundamental of Computer Graphics Chapter 6 and Chapter 7

旋转矩阵的转置和旋转矩阵的逆矩阵是一样的。这就是正交矩阵。

## 3D transformations

三维空间旋转的旋转对称性。

用绕三个轴的简单旋转组合成复杂旋转。也就是欧拉角(Roll Pitch Yaw)。

Rodrigus' rotation formula 来将复杂角度转换成简单角度。

四元数：避免万向锁，用于旋转与旋转之间的插值。

## Viewing transformations

### View/ Camera transformation

MVP transformation

- model transformation
- view transformation
- projection transformation

定义相机：

- 位置
- 看的方向
- 上方向

一同变换物体和相机不会产生变化。因此可以将相机永远位于-z方向看，y轴为向上方向的状态，用于简化运算。为此需要首先将相机移动到远点，随后旋转朝向-z方向，随后旋转到y轴为向上方向。

$M_{View}=R_{View}T_{View}$

$R_{VIew}$通过逆运算得到。

Also known as ModelView Transformation.

### Projection transformation

- Orthographic projection:正交投影
- Perspective projection:透视投影

#### Orthographic projection

原本平行的直线在平面上仍然平行。

简单理解：若镜头位于-z方向，y轴为向上方向，那么去除模型z轴的分量，随后转换和归一化到$[-1,1]^2$，就得到了正交投影的结果。

将空间中的长方体映射为标准立方体，需要平移+缩放。

#### Perspective projection

平行线会相交。近大远小。

涉及齐次式的含义。

可以理解成将远平面挤压成近平面，随后再进行正交投影。

相似三角形。$\frac{n}{z}$

构造映射之后的z轴的含义为在近平面和远平面上的z坐标不变，由此推导矩阵的第三行。

$$\begin{bmatrix} n & 0 & 0 & 0 \\ 0 & n & 0 & 0\\ 0 & 0 & n+f & -nf \\0 & 0 & 1 & 0 \end{bmatrix}$$

注意，z坐标为双曲线，而非线性曲线。
