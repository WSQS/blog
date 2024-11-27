---
title: "Runtime Polymorphism: Back to Basics by Louis Dionne"
date: 2024-10-14
url: https://www.bilibili.com/video/BV1Vx411V7Rd?p=137
tags:
  - Cpp
---

problems:

- returning related types from a function
- storing related types in a container

variant sometimes does the trick

- but it only works for closed set of types
- using visitation is sometimes not convenient

bottom line: manipulating an open set of related types with different representations

inheritance has many problems:

- bakes in reference semantics
- heap allocations
- bakes in nullable semantics
- ownership hell
- doesn't play well with algorithms
- intrusive

ref: [Sean Parent](https://youtu.be/QGcVXgEVMJg)

Goal: independent storage and method dispatch

- Storage policy
  - Remote Storage(Just like using dyno::remote_storage)
  - The Small Buffer Optimization: Add a buffer in the type
  - Always-Local Storage: may failed
  - Non-Owning storage
  - Shared Remote Storage
- VTable policy
  - Remote
  - Inline: Pessimization
  - Partial Vtable Inlining

Remote Storage: strengths and weaknesses

- simple model, similar to classic inheritance
- Always requires an allocation

The Small Buffer Optimization: strengths and weakness

- does not always require allocating
- takes up more space
- Copy/move/swap is more complicated
- Dispatching may be more costly

Always-Local Storage: strengths and weakness

- No allocation ever
- Simple dispatching
- Takes up more space

GuideLines

- use local storage whenever you can afford it
- otherwise, use SBO with the largest reasonable size
- Use purely-remote storage only when object sizes are so scattered SBO wouldn't help
- By default, all methods are in the remote vtable
- Consider inlining some methods if
  - you have slack space
  - you know you're calling them often
  - you've measured it makes a difference

Summary

- Inheritance is only a choice of run time polymorphism
- Many ways of storing polymorphic objects
- Vtable can be inlined
- Type erasure is tedious to do manually

ref: dyno lib

ref: Zack Laine's CppCon 2014 talk
