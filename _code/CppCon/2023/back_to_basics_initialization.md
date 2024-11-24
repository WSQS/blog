---
title: "Back to Basics: Initialization by Ben Saks"
date: 2024-11-24
url: https://www.bilibili.com/video/BV1BC4y1R7iL?p=42
---

Initialization in C++ can be quite complex

history:c, c++03, modern c++

## Inittializatiotn rules from c

Scalars are simple values.

Aggregates are object that are made up of smaller pieces. Union is Aeeregates.

Scalars can be initialize with a single value. It's copy-initialization.

aggregate-initialization. It's like `{...}`

Aggregate also can do copy-initialization.

For a object without ana explicite initializer

- object has static or thread storage duration, it has zero-initialized.
