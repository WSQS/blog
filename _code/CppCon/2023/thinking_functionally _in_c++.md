---
title: Thinking Functionally in C++ by Brian Ruth
date: 2024-10-29
url: https://www.bilibili.com/video/BV1BC4y1R7iL?p=19
---

A different ways of thinking about a problem

ref: The forgotten functional pattern by Ben Deane for deeply functional topic

Paradigms:

- Imperative or Procedual: roots with c
- Object Oriented: roots with simula
- Functional: STL, Lambdas, Ranges

## Identifying code functionally

Functional Code Categories:

- Actions: Depend on when or how many times they are called. Observable changes occur.
- Calculation: Depend only on their inputs and not when or how they are called. Calling them with the same inputs always results in the same outputs. No observable changes occur.
- Data: Unchanging records od events. Used as input to calculations and actions. Records the results of calculations adn actions.

- Actions
  - Allow input to programs that is unknown when the program was written
  - Performing an action has consequences
  - Affect how a program executes
- Calculation
  - Reliable
  - Encapsulated, has no effect outside of itself
  - Thread safe, since it is entirely salf contained, no ordering or locking is necessary
- Data
  - Fundamental building block
  - Immutable, data doesn't change
  - Transparent, you can look at data and see what it is
  - Open to interpretation, data can mean different things to different components without changing value
  - Used by calculations and actions to communicate with other calculations and actions

Data is all about context

Breaking down a problem to actions, calculations and data.

std::copy_if

## Functions as Data

Passing functions to functions

Return functions from functions

currying: transform a function of several arguments to a function of a single argument.

RAII

Call C API through the lambda

std::forward

```cpp
auto Oven = [](auto handle)
{
    return [h=handle](auto func, auto&&... args) mutable
{
      return func(h,std::forward<decltype(args)>(args)...);
    }
}
```

Creating an object wrapper using a lambda.

## Composable Functions


