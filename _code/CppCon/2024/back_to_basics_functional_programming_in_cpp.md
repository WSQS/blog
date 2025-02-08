---
title: "Back to Basics: Functional Programming in C++ by Jonathan Muller"
date: 2025-02-06
url: https://www.bilibili.com/video/BV14YyfYhE3C?p=51
tags:
  - Cpp
---

Imperative Programming: Specify instructions that manipulate state in order to achieve a goal

Declarative Programming: Specify the desired outcome(only), have the system figure out how to achieve it.

Functional Programming: Declarative programming by composing functions.

- No state: easier to reason about, easier to parallelize

Functional Programming is all about composition

- Write building blocks using efficient, optimized, and tested C++ code.
- Compose building blocks using functional paradigms.

## Composing algorithms

`std::ranges`

Create intermediate containers

`std::views`

- Composing views does nothing yet.
- Only Iteration will trigger computation
- Functional pipeline style; no manual state wrangling

### Range -> Range

`std::views::transform`

`std::views::filter`

`std::views::take_while` `std::views::drop_while` keep only the first/last elements

`std::view::reverse`

### Rage -> Deri med Value

`std::range::max` `std::range::min`

`std::range::count*`

`std::range::all_of` `std::range::any_of` `std::range::none_of`

`std::range::find*`

`std::range::search*`

example

```cpp
int fib(int n){
    return n <= 1 ? n : fib(n - 1) + fib(n - 2);
}

int smallest_fib_above(int x){
    auto all_fibonacci_numbers = std::views::iota(0) | std::views::transform(fib);
    return *std::range::find_if(all_fibonacci_number,[x](int f){return f > x;});
}

```

speed up

```cpp
std::generator<int> all_fibonacci_numbers(){
    int a = 0, b = 1;
    while(true){
        co_yield a;
        auto c = a + b;
        a = b;
        b = c;
    }
}
```

### Nothing -> Range

`std::view::iota`

`std::view::repeat`

`std::generator` `co_yield`

### Multiple Ranges -> Single Range

`std::views::cartesian_product`

`std::view::zip`

`std::view::concat`

### Range -> range of ranges

`std::view::chunk_by`

`std::view::split`

`std::view::adjacent` `std::view::slide`

### Range of ranges -> Single range

`std::view::join`

`std::view::join_with` insert separator

### Geneal takeaways

- Try to identify small building blocks for solving a problem
- Know your algorithms
- Composing algorithms minimizes use of for

## Composing functions

what if the intermediate functions can fail.

`std::optional`

`std::optional<T>::transform`

`std::monostate`

`std::optional<T>::and_then`

`std::expected`

`std::expected<T,E>::transform`

`std::expected<T,E>::transform_error`

`std::expected<T,E>::join`

`std::expected<T,E>::and_then`

Composing std::expected requires the same E

Composing using .transform/ .and_then minimizes use of if.

## Composing I/O

Principle: All functions are pure

- No side-effects during computation
- Always result in the same value when called with the same input.

Action

Separate I/O from computation.

`std::execution::schedule`

`std::execution::then`

`std::execution::when_all`

- Declarative build plans, execute them later
- Separate I/O from computation

## Monad

A monad is a type that implements the operations

- .transform
- .and_then
- .join

Monads enable composition
