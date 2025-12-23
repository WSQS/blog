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
