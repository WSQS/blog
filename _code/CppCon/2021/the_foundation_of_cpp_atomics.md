---
title: "The Foundation of C++ Atomics: The Knowledge You Need to Correctly Use C++ Atomics by Filipe Mulonde"
date: 2025-03-12
url: https://www.bilibili.com/video/BV1ha411k7pa?p=98
tags:
  - Cpp
  - CppCon
  - multi_thread
---

- Atomic as a class in C++
- C++ Memory MOdel
- Compiler
- Hardware

ref: Onur Mutlu Lectures

- Computing System
  - Computation
  - Communication
  - Storage/memory

Different Platform, Different goals

Parallel Computers

- Improve performance
- Reduce power consumption
- Improve const efficiency and scalability, reduce complexity
- Improve dependability

Multiprocessor types

- Loosely coupled multiprocessors
- Tightly coupled multiprocessors: Operations on shared date require synchronization

C++ standard doesn't support programming for loosely coupled multiprocessors

Main Issues: Memory consistency ordering of all memory operations

Atomic operation

- Atomicity
- synchronization/ visibility

## Memory Consistency vs. Cache Coherence

Consistency ordering all memory operations form different processors

Coherence is ordering of operations form different processors to the same memory location.

## Memory Ordering in a MIMD processor

What is the ordering of operations across different processors.

Protecting Shared Data: Threads are not allowed to update shared data concurrently.

Problem: The two processors did not see the same order of operations to memory.

## Sequential consistency

Idea: Sequential consistency, but still had multi sequential order.

Issues: Total order requirement too strong

ref:Two Techniques to Enhance the Performance of Memory Consistency Models

ref:SC-Preserving optimizations in LLVM MArino et al. 2011

Weak consistency model

`std::memory_order_acquire`

`std::memory_order_release`

`std::memory_order_relaxed`

ref:Mathematizing C++ Concurrency

Buffer influence Memory Model.

## How ROB/SQ within x86 cores influenced the x86 TSO memory model

SC(Sequential Consistency) is a subset of TSO execution.

TSO do not support ordering between a store and a subsequent load.

ref:A Primer on Memory Consistency and Cache Coherence

// TODO:Further is about hardware skip
