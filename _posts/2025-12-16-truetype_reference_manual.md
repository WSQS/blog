---
title: TrueType Reference Manual
date: 2025-12-16
url: https://developer.apple.com/fonts/TrueType-Reference-Manual/
tags:
  - computer_graphics
---

## Digitizing Letterform Designs

二阶贝塞尔曲线。

轮廓的方向决定了哪些部分是填充的，哪些部分不是。规则是`non-zero winding number rule`。

轮廓允许相交。

em square：画布。

y=0为字体基线。x=0为字体的美学中心。

一个弧线通常需要3-4个点描述。

## Font Engine

Font Engine:用于将TTF转换成栅格图像。

### How the font engine works

- 缩放字形的master outline
- grid-fitted
- 扫描为位图

#### Scaling the master outline

单位转换从em转换到26.6 fixed point numbers。

pointSize * resolution / (72 points per inch * units_per_em)
