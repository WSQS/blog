---
title: "C++ atomics: from basic to advanced. What do they really do? by Fedor Pikus"
date: 2025-03-19
url: https://www.bilibili.com/video/BV1Vx411V7Rd?p=31
tags:
  - Cpp
  - CppCon
  - multi_thread
---

Atomic: the tool of lock-free programming

Lock-free means "fast".

## Is lock-free faster?

- Algorithm rules supreme
- Wait free has nothing to do with time.
- Atomic operations do not guarantee good performance.

What is an atomic operation?

Atomic operation is an operation that is guaranteed to execute as a single transaction

ref: C++ Atomics in cppcon 2015

Type for atomic:Any trivially copyable type can be made atomic

## Operations

Operations: Assignment, special atomic operations, other operations depend on the type T.

`x *= 2;` will not compile

`x = x + 1;` and `x = x * 2;` is not atomic. It's atomic read followed by atomic write.

`std::atomic<T>` provides operator overloads only for atomic operations.

Increment and decrement for raw pointers.

`std::atomic<bool>` is valid, no special operations

`std::atomic<double>` is valid, no special operations

### Member functions

`load` `store`

`exchange` is like `std::swap`

`compare_exchange_strong` for conditional exchange

Compare and swap(CAS) is used in most lock free algorithms.

`fetch_add`... add and return old value.

`std::atomic` provides operator overloads only for atomic operations.

## Speed

Always measured performance

Comparing atomic operation with another thread-safe alternative is valid and useful.

ref: spinlock

`std::atomic` isn't always lock free.

`std::atomic::is_always_lock_free()` to check is the type lock free. It's runtime and platform dependent， based on alignment and padding.

Two thread access 2 variable with in 64 bytes will wait as if it was the same variable.

Atomic operations do wait on each other, write do, read only can scale near perfectly.

Atomic operations have to wait for cache line access.

Avoid false sharing by aligning per-thread data to separate cache lines.

## Strong and Weak compare-and-swap

c++ provides two versions of CAS

`compare_exchange_strong` and `compare_exchange_weak`

problem: if weak CAS correctly returns x == old+x, why would it fail?

Lock is not a real mutex but some form of exclusive access implemented in hardware.

Double-checked locking pattern is back.

## Usage

Atomic variable is an index or pointer to non-atomic memory.

Atomic variables as gateways to memory access.

Atomic are used to exclusive access to memory or to reveal memory to other threads.

## Memory Barriers

Memory barriers control how changes to memory made by one cpu become visible to other CPUs.

Memory barriers are closely related to memory order.

`std::memory_order_relaxed`: no barriers

`std::memory_order_acquire`: nothing after load can move in front of it, anything before can move after.

`std::memory_order_release`: is reverse.

acquire release order often used together. One thread prepare date then releases and the other acquires atomic variable.

`std::memory_order_acq_rel`: combines acquire and release

`std::memory_order_seq_cst`: no need for same atomic variable.

CAS have two memory orders.

Default memory order is `std::memory_order_seq_cst`, the strongest order. But it is expensive.

Lock free code is hard to write and hard to read. clarity matters.

Sequential consistency makes your program easier to understand and often has no performance penalty.

Lock-based program can only memory_order_acquire and memory_order_release.

## When to use std::atomic in your c++ code

Data structures that are difficult or expensive to implement with lock.

When drawbacks of locks are important.(deadlocks, priority conflicts, latency problems)

When concurrent synchronization can be achieved by the cheapest atomic operations.

ref: talks on RCU
