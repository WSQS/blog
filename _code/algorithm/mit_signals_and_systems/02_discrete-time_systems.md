---
title: "Lecture 02: Discrete-time Systems"
date: 2025-02-15
url: https://www.bilibili.com/video/BV1Vx411D7sN?p=2
tags:
  - algorithm
---

DT is easier than CT.

Multiple representations of DT

- verbal description
- difference equation
- block diagram

## Difference Equation

mathematically precise and concise

example: $y[n] = x[n] - x[n-1]$

input: unit sample

$$\delta[n]=\left\{ \begin{array}{}
    1, &if\ n= 0;\\
    0, &otherwise.
\end{array} \right.$$

## Block Diagram

Useful in hardware. And shows how to do the thing in arrow.

At rest means the output of delay is zero.

Difference: Difference Equation is declarative and Block Diagram is imperative

## From Samples to Signals

Lumping is an abstraction.

Delay is right shift operation to signal.

$Y=X-RX=(1-R)X$, where R is right shift operation.

It's concise and declarative.

## Explicit and Implicit Rules

- Recipes
- Constraint: try step by step

Accumulator; $(1-R)Y = X$ => $Y=(1+R+R^2+R^3+...)X$

## Feedback

- acyclic
- cyclic

Feedback means there is cycle in Block Diagram.
