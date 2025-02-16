---
title: "Perlin Noise"
date: 2025-02-15
url: https://www.scratchapixel.com/lessons/procedural-generation-virtual-worlds/perlin-noise-part-2/perlin-noise.html
tags:
  - algorithm
  - computer_graphics
  - perlin_noise
---

## Perlin Noise

1985 Ken Perlin

Lattice system. Random value in corner, gradient, random n Dimensional normalized vector.

Random vector need to be uniformed.

Product Random vector and the vector corner to point to get the value.

Do Interpolation to get the value, using smoothstep function.$y(x) = 3 x ^2 - 2 x ^ 3$

## Uniform Distribution of Gradients

Using angle to generate uniformed distribution normalized vector, it's still not uniformed.

//TODO

## Why Is Perlin/Gradient Noise Better Than Value Noise

In value noise the change speed of the value will change in a large range.

> A good noise is a noise that looks random and changes smoothly locally but also generally presents a pretty homogeneous look.
> As a result, the distribution of frequencies in the Perlin noise is more regular than the value noise's frequency spectrum (in particular, it removes the low frequencies you can find in the latter).

ref: An Image Synthesizer. Ken Perlin (1985)
