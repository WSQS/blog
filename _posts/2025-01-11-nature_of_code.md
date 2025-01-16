---
title: Nature of Code
date: 2025-01-11
url: https://natureofcode.com
tags:
    - JavaScript
---

## Acknowledgments

书籍的起源：动态实体和生成式艺术系统。

ref:[Processing](https://processing.org/)

ref:Code of Music

## Introduction

### What Is This Book?

ref:《Learning Processing》

Goal for this book is simple: I want to take a look at phenomena that naturally occur in the physical world and figure out how to write code to simulate them.

If this book is anything, it’s an old-fashioned programming textbook, and particular focus on object-oriented programming.

### A Word About p5.js

ref:[openFrameworks](https://openframeworks.cc/)

ref:[Cinder](https://www.libcinder.org/)

ref:[Magic Book project](https://github.com/magicbookproject)

ref:《The Computational Beauty of Nature》

ref:[That Creative Code Page by Taru Muhonen and Raphaël de Courville](https://thatcreativecode.page/)

## Randomness

### The Random Walker Class

object and class

In javascript, constructor function of a class is the member function `constructor()`.

In javascript, using `let` or `const` to declare variables.

There is `===` and `==` in javascript.

### A Normal Distribution of Random Numbers

normal distribution (sometimes called a Gaussian distribution, after mathematician Carl Friedrich Gauss)

bell curve

`randomGaussian()`function takes care of the math and returns random numbers with a normal distribution

### A Custom Distribution of Random Numbers

Lévy flight.

根据生成的随机数再去生成一个随机数。

accept-reject algorithm

It‘s one of Monte Carlo methods.

### A Smoother Approach with Perlin Noise

`noise()`function.

ref:[Ken Perlin’s website](https://mrl.cs.nyu.edu/~perlin/doc/oscar.html)

`map()`function.

`noiseDetail()`function.

## Vectors

Vector: defined as an entity that has both magnitude and direction.

Vector rather than float is better for doing same thing in short.
