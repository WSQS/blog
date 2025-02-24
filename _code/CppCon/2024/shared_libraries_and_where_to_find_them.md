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

LD_LIBRARY_PATH

Call to function in  indirect transitive library.

### AppleOS

- static linker: ld ld64 ld-prime
- dynamic linker/loader: dyld
- filed extension: dylib so framework
- file inspection: otool vtool
- post-build modifications: install_name_tool

`-L`

`otool` `-L` display shared library dependency

Each dynamic library has an install name.

//TODO: skip the appleos part.

### Windows

- .lib: Import Library
- .dll: Loadable Library

- cl: MSVC compiler
- link: Linker
- dumpbin: binary file dumper

link can be invoked by compiler or directly

link search path can be defined by `LIB` environment variable or `/LIBPATH` argument.

Pass `/VERBOSE:LIB` to print search procedure.

DLL search path:

- Neth to the .exe
- System directory
- Entries in PATH environment variable

`dumpbin /dependents` to display dependency.

`echo %errorlevel%`

DLL troubleshooting:

- Dependency walker
- Windows debugger

## Build Systems

Why locate libraries?

- Error out early: Save time
- Additional checks: version architecture
- portability/cross platform for abstraction
- correct compiler and liner flags

Package descriptor files to derive compiler/ linker flags

package descriptor files

- pkg-config .pc files
- cmake config.cmake
- Common Package Specification

ref: cppcon 2023

### CMake

- build tree
- install tree

CMake in windows runtime, can't get right dll.

ref: professional CMake: A Practical Guide

using package managers to rescue

- Conan CMake integration
- vcpkg

### Creating relocatable bundles

All dependency in bundles

Linux: package managers

Windows: place dll next to executable on windows.

linuxdeployqt

docker
