---
title: "Getting Allocators out of Our Way by Pablo Halpern & Alisdair Meredith"
date: 2025-01-30
url: https://www.bilibili.com/video/BV1pJ411w7kh?p=91
tags:
  - Cpp
---

`std::prm::monotonic_buffer_resource`

allocator-aware classes incompatible with some language features.

Memory is the oxygen of computing.

Objects that are used together should reside close to each other.

Custom memory allocation

- Performance
- To place objects in special memory
- To instrument memory allocation

cpp11

Allocator can be plugged into any of the standard containers.

- value_type
- allocate
- deallocate
- operator==
- operator!=

nested containers

the scoped allocator model: `scoped_allocator_adapter`

cpp17 pmr: a simpler allocator model

- Non-template `std::pmr::memory_resource` has allocate and deallocate member functions
- Thin wrapper `std::pmr::polymorphic_allocator<T>` meets thr cpp11 allocator requirements. 

