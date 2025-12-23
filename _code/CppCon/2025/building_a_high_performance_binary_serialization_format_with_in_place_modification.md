---
title: "Building a High-Performance Binary Serialization Format with In-Place Modification by Hamish Morrison"
date: 2025-12-23
url: https://www.bilibili.com/video/BV1jQBNBqEey/
tags:
  - Cpp
---

## The Basics - What is Serialization

Serialization: data structure to bytes.

Memory copy is not enough.

- Endianness
- Size of types
- Padding
- Alignment

Better version

- Defined size type
- Network order
- Consistent padding

Two broad approaches:

- Schema-based
- Schemaless

## Schema-Based Formats

User define a schema in a DSL.

Protobuf.

Generated code based on schema.

Schema is allowed to evolve in some ways.

Tag - Value pairs.

## Schemaless Formats

Dictionary-style API

Json. MsgPack.

Tag - Value pairs.

Optimize foe small values.

Cost: need to decode and encode for read and modification.

Target: Schemaless serialization format supports fast traversal and modification in place.

## Baseline Serialization Format

Tagged serialization format.

A sequence of tag, value pairs.

Benchmark.

## Faster Searches

Make search faster.

Most file is spent checking the size of fields.

Put keys in sorted order.

The value size is different so it's still not possible to do binary search.

Idea 1: Store a table of offsets at the start of the map.

Idea 2: Store hashes of keys at the start if the map.

Mispredicted Branches in Binary Search. Branchless programming.

Idea 3: Use branchless binary search.

Doing only one assignment in the if statement.

ref: Array Layouts for Comparison-Based Searching

ref: [Performance comparison: linear search vs binary search](https://dirtyhandscoding.github.io/posts/performance-comparison-linear-search-vs-binary-search.html)

## Faster Modification

Moving element is a problem.

Idea 1: Move items "out-of-line" of their containing object.

Offsets can point anywhere else in th buffer. Nesting is expressed by maps pointing to other maps.

Idea 2: Implement a bump allocator.

Idea 3: Implement a free-list allocator.

Idea 4: Prefetch free-list entries while iterating.

## Final Benchmarks

## Limitations

Fragmentation is a problem with first-fit.

## Conclusions

Improve performance:

- Create highly parameterized benchmarks
- Profile
- Make algorithmic/data structure improvements
- Explore vectorization, branchless code, prefetching

## Futrure Work

- Compact
- Offset-free serialization

ref: Algorithms for Mordern Hardware by Sergey Slotin

ref: The Garbage Collection Handbook

ref: Going Nowhere Faster in CppCon 2017

ref: Performance and Efficiency in C++ by Fedor Pikus
