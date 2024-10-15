---
title: Better Code: Runtime Polymorphism - Sean Parent
date: 2024-10-15
url: https://www.youtube.com/watch?v=QGcVXgEVMJg
---

- Better Code
  - Regular Types
  - Algorithms
  - Data Structures
  - Runtime Polymorphism
    - Goal: No Inheritance
  - Concurrency

Inheritance is a mechanism to implement runtime-polymorphism where one class is derived from another class, but overriding all or part of the implementation.\

- guideliens
  - Write all code as a library
  - Reuse increases your productivity
  - Writing unit tests is simplified

make_shared<> is better than new, but the shared structure break ability to reason locally about the code(A shared pointer is as good as global variable).

Using the same operator names to provide the same semantics on our user types enables code reuse.

value semantics(cpp) is different from reference semantics(java)
