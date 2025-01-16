---
title: "lecture 21: Animation"
date: 2025-01-13
url: https://www.bilibili.com/video/BV1X7411F744?p=21
tags:
  - computer_graphics
---

动画，美学方面更加关键。

动画是对几何的拓展。

视觉暂留。

## History

手绘剧场版动画:《白雪公主》

《侏罗纪公园》

CG剧场版动画：《玩具总动员》

## Keyframe animation

关键帧动画。

flash。

插值的技术。

## Physical simulation

牛顿定律

布料模拟。

流体模拟。

Mass Spring System: 质点弹簧系统。

一系列相互连接的质点和弹簧。

增加阻尼，会导致所有运动都减速，增加内部损耗，取决于相对径向速度。

弹簧的结构。

结构无法抵抗切向的力。无法抵抗外在于平面的力。

增加对角线的弹簧。增加skip connection。

有限元方法。力的扩散过程。

Particle Systems

用粒子描述物体。

需要很多粒子，需要一个加速结构找到最近邻粒子。

re:[Teaching myself C so I can build a particle simulation](https://www.youtube.com/watch?v=NorXFOobehY)

- 吸引力、排斥力
- 阻力
- 碰撞

万有引力

先模拟后渲染。

粒子模拟流体。

鸟群。

分子系统。

## Kinematics

运动学，正运动学与逆运动学。

三种关节：1维旋转，2维旋转，拉长。

正向运动学存在解析解。

逆运动学，自动根据尖端位置调整关节位置。难以求解。只能用梯度下降求解析解。

## Rigging

对于形状的控制，骨骼绑定。

对形状进行插值，控制点插值。

运动捕捉。控制点。

复杂，并且设置很复杂。

捕获的动作还需要进行修改。

- 光学
- 磁场
- 机械

恐怖谷效应。

制片流水线。
