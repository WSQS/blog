---
title: Back to Basics: Object-Oriented Programming in C++ by Amir Kirsh
date: 2024-10-27
url: https://www.youtube.com/watch?v=_go74QpFPAw
---

Goals:

- Disscuss the basics of object oriented Programming in C++
- Understand the alternatices and tradeoffs

data+operation

Single Responsibility: Every class takes care of its own business

- public
- protected
- private

data members: should be private and need to initialized for primitive types.

member functions is not part of the object size

a function defined in class is inline.

Constructor Delegation and Constructor Inheritance

Casting and explicit

mutable members

Rule of Zero: It is the best if your class doesn't need any resource management: try to using std::unique_ptr and std::shared_ptr, Isolate the resource to it's own class.

Rule of There: if you need a dectrctor, first thing block the copy Constructor and assignment operator.

Rule of Five: If you implement or block any one of the five, you lose the defaults for the move operations.

Inheritance-Polymorphism

Command Pattern

> C++ is not Just an Object Oriented Language

Array of Structs vs Structs of Arrays

Efficient

ref: Inheritance is the base class of Evil by Sean Parent
