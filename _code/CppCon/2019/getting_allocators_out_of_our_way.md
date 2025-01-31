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
- Each standard container has a pmr alias.

`std::pmr::memory_resource`: member function `allocate()` `deallocate()` is delegate to virtual functions.

`std::pmr::polymorphic_allocator`: wrapper a pointer to memory resource.

Interoperability problem disappear.

cpp20

`polymorphic_allocator<byte>`: in new code there is no need a template allocator, just using `polymorphic_allocator<byte>`.

cpp17 provides standard memory resource.

`std::pmr::new_delete_resource()`: delegate to general heap(`operator new` and `operator delete`)

`std::pmr::unsynchronized_pool_resource()`

- Good for dynamic data structures that grow and shrink
- Single threaded

`std::pmr::monotonic_buffer_resource`

- Ultra-fast, single-threaded, allocate from contiguous buffers and do nothing deallocate.
- For container that grow monotonically throughout their lifetime.
- Can allocate from stack memory.

Test

ref: test_resource: The pmr Detective in CppCon 2019

Standard resource can be constructed with an upstream resource for replenishing its interal pools.

`using allocator_type - pmr::polymorphic_allocator<>`

cost: interface and implementation

It's the limits of library approach, next is language solution for language proposal.

Simplify the interface.

Redduce implementation boilerplate.

`using`

