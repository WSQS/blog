---
title: "lecture 22: Animation Continue"
date: 2025-01-14
url: https://www.bilibili.com/video/BV1X7411F744?p=22
tags:
  - computer_graphics
---
## Single particle simulation

粒子在速度场当中运动。$\frac{dx}{dt}=v(x,t)$

Ordinary Differential Equation(ODE)常微分方程

### Explicit Euler method

前向欧拉和显示欧拉。

$x^{t+\Delta t}=x^t +\Delta t \dot{x}^t$

$\dot{x}^{t+\Delta t} = \dot{x}^t + \Delta t \ddot{x}^t$

误差且不稳定(diverge)。

### Instability and improvements

解决方法：

- 中点法
- 自适应方法
- 隐式方法
- 非物理方法

中点法：使用中点的速度重新计算，多了一个二次的项。

$x^{t+\Delta t}=x^t +\Delta t \dot{x}^t + \frac{(\Delta t)^2}{2}\ddot{x}^t$

自适应方法，逐步减少步长，根据距离判断是否需要将当前点划分成两个点。

隐式欧拉方法，使用下一个时间的梯度。

$x^{t+\Delta t}=x^t +\Delta t \dot{x}^{t+\Delta t}$

$\dot{x}^{t+\Delta t} = \dot{x}^t + \Delta t \ddot{x}^{t+\Delta t}$

更稳定。

稳定性的定量，局部误差和累计误差。关键在于误差和$\Delta t$的误差。

Runge-Kutta Families 龙格库塔方法

RK4 是最广泛使用的。

ref:数值分析

非物理方法。简化模型。能量不守恒。

## Rigid body simulation

刚体模拟，粒子运动+约束。存在角度和角速度。

## Fluid simulation

Position-Based 方法

- 水体是不可压缩的小球
- 密度不一样的都需要通过移动小球被修正，梯度下降。

Lagrangian: 拉格朗日方法，视为质点，关注质点。

Eulerian: 欧拉方法，视为网格，关注空间。

混合型方法。Material Point Method(MPM)

粒子->格子->粒子

ref:《Real-Time Rendering》

GAMES: 图形学在线交流平台

ref: Chinagraph

ref: ChinaVR

ref: GAMES 201

ref: Real-Time High Quality Rendering

ref: Advanced Image Synthesis

Rendering + Appearance Modeling + Future Display Equipment + Emerging Technology = Ultimate Realism
