---
title: Breaking Dependencies - The SOLID Principles by Klaus Iglberger
date: 2024-10-10
url: https://www.bilibili.com/video/BV1YA411J7Pe?p=11
tags:
  - Cpp
---

blaze C++ math library

Munich C++ user group

Soft = Easy to change and extend

> Coupling is the enemy of change, because it links together things that must change in parallel.
> Dependency is the key problem in software development at all scales.

Solution: The SOLID principles

- Single-Responsibility Principle
- Open-Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

SOLID principles is not limited to OO programming but is a general set of guidelines.

## Single-Responsibility Principle(SRP)

what is responsibility?

independent, and with a single, well-defined purpose. Cohesion. Changing in isolation.

Decrease coupling and increase readability.

the design of the STL follows the SRP

std::vector follows the SRP

std::string does not follow the SRP

A function should not implement details of two orthogonal issues.

**Guideline: Prefer cohesive software entities. Everything that does not strictly belong together, should be separated.**

## Open-Closed Principle(OCP)

Open for extension, but closed for modification.

ref: CppCon2017 Free Your Functions

contradiction between srp and ocp.

这里作者比较了多种方法对OCP和SRP的支持，需要每个都研究一下。

ref: Embrace No-Paradigm Programming

modern approach is better.

ref: Dynamic Polymorphism With Code Injection and Metaclass

OCP can also apply to functions.

The copy() function works for all copyable types. Works for all types that adhere to required concepts. Doesn't hove to be modified for new types.

**GuildLine: Prefer software design that allows the addition of types or operations without the need to modify existing code.**

## Liskov Substitution Principle(LSp)

substitution property: Subtypes must be substitutable for their base types.

Behavioral subtyping aka IS-A relationship.

- Contravariance of method arguments in a subtype
- Convariance of return types in a subtype
- Preconditions cannot be strengthened in a sub type
- Post conditions cannot be weakened in a subtype
- Invariants of the super type must be preserved in a subtype.

**Guideline: Make sure that inheritance is about behavior, not about data.**

**Guideline: Make sure that the contract of base type is adhered to.**

**Guideline: Make sure to adhere to the required concept.**

## Interface Segregation Principle(ISP)

Can also apply to generic code.

**GuideLine: Make sure interfaces don't induce unnecessary dependencies.**

## Dependency Inversion Principle(DIP)

- High-level modules should not depend on low-level modules. Both should depend on abstractions
- Abstractions should note depend on details. Details should depend on abstractions.

Model-view-controller: model(high level ) should define what controller and view should give as interface.

the copy() function is in control of its own requirements(concepts), is implemented in terms of these requirements, you depend on copy(), not copy() on you.

**Guideline: Prefer to depend on abstractions(i.e. abstract classes or concepts) instead of concrete types.**

key problem: where is the abstraction belong to.

## Summary

- The SOLID principles are more than just a set of OO guidelines.
- Use the SOLID principles to reduce coupling and facilitate change.
  - Separate concerns via the SRP to isolate changes
  - Design by OCP to simplify additions/ extensions
  - Adhere to the LSP when using abstractions
  - Minimize the dependencies of interfaces via the LSP
  - Introduce abstractions to steer dependencies
