---
title: "Better Code: Runtime Polymorphism - Sean Parent"
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

`make_shared<>` is better than new, but the shared structure break ability to reason locally about the code(A shared pointer is as good as global variable).

- problem: Changed semantics of copy, assignment, and equality
  - leads to incidental data-structures
  - thread safety concerns

we define an operation in terms of the operation's semantics, but the syntax for copy and assignment no longer have their regular semantics. The shared structure also break our ability to reason locally about the code.

Using the same operator names to provide the same semantics on our user types enables code reuse.

value semantics(cpp) is different from reference semantics(java)

- problem: Inefficient
  - always heap allocated
  - access to call must be synchronized
- problem: Polymorphism is intrusive

The requirement of a polymorphic type comes from it's use. There are no polymorphic types, only a polymorphic use of similar types.

> Inheritance is the base class of Evil.

guidelines: let the compiler do the work where appropriate

guidelines: write classes that behave like regular object to increase reuse.

guidelines: Do your own memory management - don't create garbage for your client to clean-up.

sink argument

guidelines: Polymorphism is an implementation detail.

ref:http://sean-parent.stlab.cc/papers-adn-presentations

ref: Elements of Programming

