---
title: Back to Basics: Lambdas by Nicolai Josuttis
date: 2024-11-21
url: https://www.bilibili.com/video/BV1ha411k7pa?p=138
---

TODO: read some book of him.

have cpp books

without lambda, there is more functions. which all need a good name.

lambda is for helper function. Compiler can have chance to optimize.

callable

std::count_if

std::find_if

Lambda: function object defined on the fly.

Combining Lambdas with standard algorithms.

auto can used in lambdas.

lambdas without captures is equal to function pointer and can be used as sorting criterion and hash function.

Lambdas are more than functions: it's local and it can be defined at run time.

Lambdas has two parameters: capture behavior parameter and call parameter.

the type of lambdas need to be auto.

the auto in lambda make the `operator()` a function template. But lambda self is still a function object which can be pass to a function. But a function template it self can't.

lambda capture with value is stateless, lambda capture with reference and mutable is stateful.
