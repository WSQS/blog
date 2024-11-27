---
title: Thinking Functionally in C++ by Brian Ruth
date: 2024-10-29
url: https://www.bilibili.com/video/BV1BC4y1R7iL?p=19
tags:
  - Cpp
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

- Filter: take a list of item of one and eliminate to create a list of the same number or fewer items of the same type. `std::copy_if`
- Map: Take a list of items of one type and create a list of the same size with all items converted to a new type. `std::transform`
- Reduce: Take a list of items and create a single value.`std::accumulate` `std::reduce`

std::ranges

## Lazy Evaluation

Delay actions or calculations until they are needed

Allocation

Fetch data lazily

Efficient Iteration

## Your Mileage may vary

`std::remove_if`

Calculations need unchanging data:

- If the contained type is cheap to copy, copy it
- Guarantee that the data won't change, which requires some type of synchronization
- Create data structure that can create copies lazily or log changes: bitmapped vector trie

## Thinking Functionally

- Leverage that C++ is a multiparadigm language.
- Separate code into Actions, Calculations and Data
- Isolate Actions
- Reuse Calculations
- Treat functions as Data
- Functions can work together
- Be lazy
- Don't be too smart

> Debugging is twice as hard as writing the code in the first place. Therefore if you write code as cleverly as possible, you are, by definition, not smart enough to debug it.

ref: Grokking Simplicity by Eric Normand(book)

ref: Functional Programming in C++(book)

ref: Ranges for the Standard Library by Eric Niebler

ref: C++ Weekly - EP 126 - Lambdas with Destructors
