---
title: "lecture 06: Rasterization Antialiasing and Z-Buffer"
date: 2024-12-16
url: https://www.bilibili.com/video/BV1X7411F744?p=6
tags:
  - computer_graphics
---

## Antialiasing

alias:走样

采样在计算机图形学当中无处不在：光栅化、拍照，视频是对时间进行采样。

Artifact：计算机图形学中的错误、不准确

- 锯齿
- 摩尔纹
- 车轮效应

本质原因：信号变化太快了而采样的速度太慢了。

### Sampling theory

想法：在采样之前进行模糊或滤波

不可以先进行采样后进行模糊或滤波

Frequency Domain：频域

Fourier Transform：傅里叶变换

把任意一个函数转变成频域

走样：对于两种不同的频率，经过采样无法区分彼此。

滤波：去除特定频率的内容

对图像进行傅里叶变换，低频信息多，集中在中间，高频信息少．

高通滤波，保留边界。

低通滤波。

ref: 数字图像处理

滤波=卷积=平均

卷积定理：时域上两个信号的卷积，频域上是两个信号的乘积。所以可以直接对图像进行卷积，也可以将图像和卷积进行傅里叶变化之后相乘，再转回图像。

Box Filter: 低通滤波器。

采样=重复频谱上的内容

采样的间隔会导致频谱上的内容以对应的距离移动。

走样也就是频谱发生了混叠。

### Antialiasing in practice

方法：

- 增加采样频率
- 在采样之前进行低通滤波

低通滤波的方法：

- 卷积：根据单个像素当中的值进行滤波

理想情况：根据像素当中被覆盖的面积混合成对应的颜色

近似：MSAA(Multi-Sample Antialiasing)(Antialiasing By Supersampling)

代价：增大了计算量

里程碑

- FXAA(Fast Approximate AA)：替换边界
- TAA(Tempotal AA)：依据时序

超分辨率和抗锯齿类似，根本问题都是采样数据不够。

DLSS(Deep Learning Super Sampling)
