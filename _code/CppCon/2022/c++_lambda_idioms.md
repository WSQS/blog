---
title: C++ Lambda Idioms
date: 2024-10-21
url: https://www.bilibili.com/video/BV1FB4y1H7VS?p=28
---

Jetbrain developer.

Lambda was included in C++11.

ref: [standard document for lambda](https://eel.is/c++draft/expr.prim.lambda)

some other site: [https://timsong-cpp.github.io/cppwp/](https://timsong-cpp.github.io/cppwp/) [https://eel.is/c++draft/](https://eel.is/c++draft/) [https://github.com/timsong-cpp/cppwp](https://github.com/timsong-cpp/cppwp)
when there is a lambda expression, compiler will generate a closure type for a lambda-expression has a public inline function call operator.

- Lambda is const by default and can changed by using key word mutable.
- the return type is deduced by compiler and can spercified.
- no noexcept by default.
- Compiler also delete constructor and assignable function.
- Lambda with no state can implicit convert to function poiner.

## Unary plus trick

Explicit conversion to function poiner.

- using `static_cast<>()`
- or just add + in the front of lambda-expression. Cause unary plus can work for pointer.

Lambda captures

Add to non-static menbers to capture variable, and initialize it with captured variable.

static variable and gloable variable can't be captured.

odr-use of a variable also don't need to be captured.

ref: odr-use

## Immediately Invoked Function expression(IIFE)

Call a lambda function right after it definition.

Use case: initialize a complex object. Need doing some logic. Can move the code into lambda function.

Since C++17 std::invoke() can do the same thing.

## Call-once Lambda

red: what you can learn from being too cute - Daisy Hollman.[markdown](../../cpp/what_you_can_learn_from_being_too_cute_part_1.md) [html](../../cpp/what_you_can_learn_from_being_too_cute_part_1.html)

Immediately invoke a lambda expression with a return value and assign it to a static variable.

it's more efficient than std::call_one.

C++14 include generic lambdas. The call operator of lambda is a template. But the Unary plus trick cann't work.

Generic lambda support perfect forwardding`auto &&`. Generic lambda also support`auto&&...args`.This also support to pass a lambda function into a lambda function.

## Variable Template Lambda

ref: Bjorn Fahller

Make lambda itself a template, add access the template parameter in it.

```cpp
templdate<typename T>
constexpr auto c_cast = [](auto x){return (T)x;}
```

## Init capture optimisation

ref: Filipec: *C++ Lambda Story*

Init capture: Init a new variable inside the capture.

Init just do once.

C++17 can be constexpr, and can pass into template.

## Lambda overload set

Class template argument deduction(CTAD)

We can inherent from lambda.

```cpp
template<typename... Ts>
struct overload: TS...{
  using TS::operator()...;
};
```

C++20 include Templated lambdas

## Unique types generator

ref: Kris Jusiak

```cpp
template<auto=[]{}>
struct foo{};
```

## Recursive lambdas

C++23 include deducing this: template on the type of self.

Call the lambda function in it self.
