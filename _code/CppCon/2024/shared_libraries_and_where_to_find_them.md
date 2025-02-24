---
title: "Shared Libraries and Where To Find Them By Luis Caro Campos"
date: 2025-02-18
url: https://www.bilibili.com/video/BV14YyfYhE3C/?p=48
tags:
  - Cpp
---

## When shared libraries are needed

- When configuring the build
- When creating other shared libraries and executables
- When running executables
  - Launching them
  - Loading loadable plugins
- When packaging application for distribution

## Which programs needs to locate shared libraries

- Static Linker
- Dynamic Linker/Loader

### Static

`-l<library>`

The linker:`ld`, other implementation: ld.gold, lld, mold, gcc invoke ld via collect2

- Each distro/toolchain may be configured differently
- ld defaults may be overridden by the invocation by gcc
  - check the collect2 invocation with -v
- GNU Linker is typically the default, there is others:
  - gold, lld, mold
  - They may have slightly different behaviors

`-Xlinker`: dump interal linker script

`ld.so`

### Dynamic

`ld-linux.so`

`file`

`readelf -l`

`readelf -d`

`objdump -p`

`LD_DEBUG=libs`

`ldd`

`-L<path>` to define where to look libraries when compile, this only define the direct dependency.

`LD_LIBRARY_PATH` and `-Wl,rpath,/<path>` (when compiling) to define where to look when running.

transitive dependencies

RPARH and RUNPATH

## Tools to query, troubleshoot

## Where to find shared libraries
