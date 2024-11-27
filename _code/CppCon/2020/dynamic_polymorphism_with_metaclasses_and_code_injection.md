---
title: Dynamic Polymorphism with Metaclasses and Code Injection By Brand
date: 2024-10-12
url: https://www.bilibili.com/video/BV1YA411J7Pe?p=38
tags:
  - Cpp
---

Polymorphism:The provision of a single interface to entities of different types.

ref: Runtime Polymorphism: Back to Basics[markdown](./../2017/runtime_polymorphism_back_to_basics.md) [html](./../2017/runtime_polymorphism_back_to_basics.html)

ref: Inheritance is the base class of evil

Problems with Inheritance:

1. Often requires dynamic allocation
2. Ownership and nullablity considerations
3. Intrusive: requires modifying child classes
4. No more value semantics
5. CHanges semantics for algorithms and containers

Hand-written virtual functions

- Declare vtable for the abstraction interface: declare function pointer in struct( vtable).
- Define vtable for a concrete type: template of instance vtable.
- Capture the vtable pointers on construction: use template in the construction function. Type Erasure
- Forward calls through the vtable: call vtable function in function.

Solve the problem of 2 and 3. By adding correspondent function it can solve problem 4 and 5.

Should add type check.

Reflection: The ability of a program to introspect its own structure

Static Reflection: The ability of a program to introspect its own structure at compile time.

`std::is_array<T>` `std::is_same<T, U>`

ref: Scalable Reflection in C++

Code Injection

```cpp
constrval void generate_getter(meta::info member)
{
    ->_fragment struct{
        typename(meta::type_of(member))const&
        unqualid("get_",member)()
        {
            return exprid(member)
        }
    }
}
```

Code-injected virtual functions

- Declare vtable for the abstraction interface: generate function declare
- Define vtable for a concrete type: inject to template
- Capture the vtable pointers on construction
- Forward calls through the vtable

Add StoragePolicy and CTablePolicy in template to set the storage way.

Metaclass functions let programmers write a new kind of efficient abstraction: a user-defined named subset of classes that share common characteristics, typically(but not limited to): user-defined rules, defaults, generated functions

ref: [Compiler Explorer](https://cppx.godbolt.org)
