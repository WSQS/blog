---
title: What you can learn from being too cute By Daisy Hollman
date: 2024-10-23
url: https://www.youtube.com/watch?v=2YKj2l3PlCI
tags:
  - Cpp
---

meeting cpp

why you should write code that you should never write.

Well-written code should be unsurprising.

## Interate Backwoards Through a Parameter Pack

```cpp
// Left to right
template <typename... Ts>
void func(Ts... ts)
{
 auto func = [](auto t){};
 (func(ts), ...);
}
// Right to left
template <typename... Ts>
void func(Ts... ts)
{
 auto func = [](auto t){};
 (func(ts) = ...);
}
```

By floding over a right-associative oprator(like assignment for instance)

`std::type_identity<>()`Provides the member typedef type that names T (i.e., the identity transformation).

ref: intro.execution

comma is left to right and assignment is right to left.

flod expressions

## Excute Once Lambda

static with lambda call immediately.

ref: stmt.dcl

Execute N times Lambda: using exception

Data race

## Deductoin Guides for Aggregates

```cpp
template<class T, class U>
struct Foo
{
  T bar;
  U baz;
}
template<class T, class U>
Foo(T,U)->Foo<T,U>;
```

## Enumerating Parameter Packs

```cpp
void enumerate_pack(auto f, auto... args)
{
  [&]<size_t... Idxs>(std::index_sequence<Idx...>)
  {
    (f(Idx,args),...);
  }(std::make_index_sequence<sizeof...(args)>{});
}
```

ref: effcient parameter pack indexing by Louis Dionne

## Getting the last parameter in a pack

ref: concept in cpp20
