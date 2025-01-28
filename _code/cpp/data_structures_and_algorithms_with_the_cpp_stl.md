---
title: "Data Structures and Algorithms with the C++ STL"
date: 2025-01-24
url: https://annas-archive.org/slow_download/22ea7908884f846947793ac0fbbba2b4/0/0
tags:
  - Cpp
---

## Preface

source code: [Github](https://github.com/PacktPublishing/Data-Structures-and-Algorithms-with-the-CPP-STL)

## Mastering std::vector

### The Basics of std::vector

std::vector as a dynamic array. Arrays are static in size, set at declaration time, and cannot be altered afterward.

Memory management.

Member functions.

#### Declaring and initializing std::vector

Specify initial size.

Value-Initialized.

Initializer lists.

`std::generate`

copy initialization.

#### Accessing elements

`operator[]`

`at()`

`size_t size()`

`front()` `back()`

#### Add and removing elements

`push_back()`

`insert()`

`emplace()` `emplace_back()`

`pop_back()`

`erase()`

erase-remove idiom:

- `std::remove` `std::remove_if` move elements to the end.
- erase the end of container.

In c++20, `std::erase()` and `std::erase_if()` allow handle two step in one function.

`capacity()`

`empty()`

`clear()` doesn't alter the capacity of vector.

`reserve()`

### Mastering Iterators with std::vector

#### Types of iterators in the STL

In STL, iterators connect algorithms and containers.

- input iterators: impossible to move forward and modify present value.
- output iterators: `std::back_inserter`
- forward iterators: combine input and output iterators. `std::forward_list`
- reverse iterators: `rbegin()` `rend()` `std::reverse_iterator`
- bidirectional iterators: `std::list`
- random access iterators

`std::generatr_n()`

#### Basic iteration techniques with std::vector

`begin()` `end()`

`cbegin()` `cend()`

- process data
- search operations
- algorithm application

#### Using std::begin and std::end

`std::begin()` `std::end` works for different containers.

Using non-menber function is key to crafting container-independent, reusable code.

#### Creating a custom iterator

- enhanced abstrction
- data transformation
- filtered views

requirements:

- type aliases
  - value_type
  - difference_type
  - pointer and refrence
  - iterator_category
- operators
  - operator*
  - operator++
  - operator== and operator!=

### Mastering Memory and Allocators with std::vector

#### Resizing and reserving memory

`resize()`

shrink a vector's size doesn't reduce its capacity.

`shrink_to_fit()`

#### Custom allocator basics

Allocator servers as an interface, abstrction the memory source for the container. It handle allocating and deallocating, construct and destruct.

abstrction interface:

- `allocate()`
- `deallocate()`
- `construct()`
- `destroy()`

`std::allocator`

#### Creating a custom allocator

Memory pool:

- Faster allocations and deallocation
- Reduce fragmantation
- Predictable behavior

