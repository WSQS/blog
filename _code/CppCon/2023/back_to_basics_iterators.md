---
title: "Back To Basics: Iterators by Nicolai Josuttis"
date: 2024-11-22
url: https://www.bilibili.com/video/BV1BC4y1R7iL?p=30
tags:
  - Cpp
---

other talk from this reporter: [markdown](../2021/back_to_basics_lambdas.md)

Loop over array.

- with index
- with pointer

Iterators: generalization of pointers that iterate

`begin`and`end`

note: end is not the element. It's a half one range. It's no need to deal with empty collections.

## Why Iterators?

Iterators can deal with multi data structure.

Used by the range-based for loop.

`const_iterator` means the element the iterator refers to is const. This is also equals to `cbegin`and`cend`

iterators have different categories.

- random access iterator: can jump to and compare with other position
- bidirectional iterator: can iterate forward and backward
- forward iterator: can iterate forward only
- input iterator: can read elements only once
- contiguous range/iterator(since c++ 20):support for std::ranges::data()

note: deque is a array of a array so it's a random access iterator but not a contiguous iterator

## Iterator and Algorithms

iterators as glue interface.

ref:std::max_element

```c++
if(result != foo.end())
```

handel the result.

ref:std::accumulate

Algorithms are generic

note:std::set sort the element automatic

pure abstraction: everything that behaves like a iterator is a iterator.

Separate data and function.

## Pitfalls of Iterators

append element maybe will change the location of the container.

std::transform()with 4 arguments. Destination need to be a output iterators, and there must be elements to overwrite.

- Need to resize the destination array.
- using `std::back_inserter`

std::remove remove the elements but doesn't resize the container, it remain the value. Iterator can't remove the elements.

Removing algorithms do note remove, instead they replace removed elements and return the new end.

ref:std::ranges::subrange and std::views::filter

view cache the begin

modification of the element a filter_view::iterator denotes is permitted, but results in undefined behavior if the resulting value does not satisfy the filter predicate.
