---
title: C++ for Godot with GDExtension by David Snopek
date: 2025-02-23
url: https://www.bilibili.com/video/BV1gvPue1EoM/
tags:
  - Cpp
  - GodotCon
  - godot
---

Addons and GDExtension example, maintained by David Snopek:

- Godot Rollback Netcode(addon)
- SG Physics 2d(GDExtension)
- Godot OpenXR Vendors(GDExtension)

ref:[Website](https://SnopeckGames.com)

## GDExtension

GDExtension: A C interface that allows interacting with the internal of Godot, including:

- Adding nwe native classes to Godot(ie making your own nodes, resources or objects)
- Adding editor plugins
- Adding new scripting languages
- (Future)Embedding Godot in other applications(LibGodot)

## Language bindings

Language bindings adapt that C interface into something easy to use from a particular programming language of environment

- godot-cpp
- Godot Rust
- GodotSwift
- godot-go

there is difference between language bindings and scripting languages

## godot-cpp

godot-cpp: Official GDExtension binding for c++

There is a lot of way to design a language binding

godot-cpp aims to provide the same api as used within godot itself, but it not fully achieved.

So a single codebase can be compiled either as a module or GDExtension.

## Clone Project

```bash
git clone --recursive
```

```bash
git submodule update --recursive
```

`.gdextension` define library.

`entry_symbol`

`reloadable`

Add include path.

## summator example

`GDCLLASS` marco.

`static void _bind_methods()` function.

`ClassDB::bind_method(D_METHOD(...),<function_pointer>)`

`GDREGISTER_CLASS(<class>)`

`reload current project` to get auto complete.

## Traffic Light example

reusable extension.

`memnew()`

`Ref<>`

`ADD_PROPERTY(PropertyInfo(),<setter>,<getter>)`

`VARIANT_ENUM_CAST()`

`BIND_ENUM_CONSTANT()`

`void _notification(int p_what)` the `void _ready()` will be override by GDScript.

virtual in cpp and virtual in GDScript is different.

`#include <godot_cpp/core/gdvirtual.gen.inc>`

`GDVIRTUAL...`

`GDVIRTUAL_BIND()`

`GDVIRTUAL_CALL()`

`ADD_SIGNAL(MethodInfo(...))`

`emit_signal`

`godot --doctool .. --path <path> --gdextension-docs`

## Game Scripting Example

`Input::get_singleton()`

`move_and_slide()`

`GDREGISTER_RUNTIME_CLASS()`

`Engine::get_singleton()->is_editor_hint()`
