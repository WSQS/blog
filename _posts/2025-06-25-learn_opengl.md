---
title: Learn OpenGL
date: 2025-06-25
url: https://learnopengl.com/
---

OpenGL 只是规范而不是一个API，它并不提供实现细节。

ref：[规范文档](https://registry.khronos.org/OpenGL/specs/gl/glspec33.core.pdf)

OpenGL Core profile

OpenGL 包含状态机概念。

OpenGL 设计了c风格的 Object。

GLFW

GLAD:[glad website](https://glad.dav1d.de/)

渲染管线<-顶点数据

- 顶点着色器
- 几何着色器
- 片段着色器
- 光栅化

OpenGL 仅处理 3D 坐标上 -1.0 到 1.0 之间的特定范围内的坐标。

顶点缓冲对象VBO

顶点数组对象VAO

元素缓冲对象EBO：相比起复制多份数据，只是重用索引。不要在VAO解绑之前解绑EBO。

## GLSL

swizzling

`in` and `out`

片段着色器输出一个vec4的颜色。

OpenGL 会将相同名字的变量的着色器链接起来。

uniform: 全局变量
