---
title: Breaking Dependencies - The SOLID Principles by Klaus Iglberger
date: 2024-10-10
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

Guideline: Prefer cohesive software entities. Everything that does not strictly belong together, should be separated.

## Open-Closed Principle(OCP)

Open for extension, but closed for modification.

ref: CppCon2017 Free Your Functions

contradiction between srp and ocp.

ref: Embrace No-Paradigm Programming

modern approach is better.

ref: Dynamic Polymorphism With Code Injection and Metaclass

OCP can also apply to functions.

The copy() function works for all copyable types.
