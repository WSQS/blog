---
title: Game Engine Architecture
date: 2025-04-04
---

## Preface

游戏引擎与游戏之间的界限是模糊的。

ref: Effective STL

ref: Effective C++

## Foundations

### Introduction

#### Structure of a Typical Game Team

- Engineers
- Artists
- Game designers
- Producers
- Support Staff

#### What is a Game?

主要关注于第一人称射击、第三人称动作和平台、竞速、格斗这些类型的游戏。*确实在这些游戏当中涉及到了想当一部分的共性，而这些共性可以被抽象成游戏引擎。因此，是先有游戏然后才有游戏引擎的，同时，这样产生的游戏引擎也就注定是对于一些更为特殊的游戏类型是较为无力的。*

##### Video Games as Soft Real-Time Simulations

soft real-time interactive agent-based computer simulations.

simulations: 游戏采用近似和简化的方法来模拟世界。

agent-based: 游戏中存在一定数量的的实体。

temporal simulation: 游戏世界的状态会动态变更

interactive: 游戏会对玩家的输入做出反应。

real-time: 实时系统需要一个刷新频率。对于游戏来说，它包含了多种不同的刷新频率。

soft real-time: 没有赶上deadline并不是一个严重的问题。

numerical: 游戏引擎是进行数值计算的，因为对于多数问题，并不存在解析解。

#### What Is a Game Engine?

Doom 区分了核心软件组件和美术资产、游戏地图、游戏规则。这使得玩家可以创作新的游戏，形成了mod社区。使用游戏引擎进行开发比独立直接开发更加的经济。

游戏引擎与游戏之间的界限是模糊的。

data-driven architecture 区分游戏引擎和游戏。

游戏引擎无法用于制作所有游戏。一个普遍的游戏引擎难以对特殊情况进行优化。A game can always be made more impressive by fine-tuning the engine to the specific requirements and constraints of a particular game and/or hardware platform.

#### Engine Differences across Genres

- FPS
- Platformers and Other Third-Person Games
- Fighting Games
- Racing Games
- Strategy Games
- MMOG
- Player-Authored Content
- Virtual, Augmented and Mixed Reality

#### Game Engine Survey

- The Quake Family of Engines
- Unreal Engine
- The Half-Life Source Engine
- DICE’s Frostbite
- Rockstar Advanced Game Engine (RAGE)
- CRYENGINE
- Sony’s PhyreEngine
- Microsoft’s XNA Game Studio
- Unity
- Proprietary In-House Engines
- Open Source Engines(OGRE, Panda3D, Yake, Crystal Space, Torque, Irrlicht, Lumberyard)
- 2D Game Engines for Non-programmers(Multimedia Fusion 2, Game Salad Creator, Scratch)

#### Runtime Engine Architecture

游戏引擎是一个大型软件系统。

游戏引擎是层级结构，上层依赖于下层。

- Target Hardware
- Device Driver
- Operating System
- Third-Party SDKs and Middleware
  - Data Structures and Algorithms
    - Boost
    - Folly
    - Loki
    - stl
  - Graphics
    - Glide
    - OpenGL
    - DirectX
    - libgcm
    - Edge
    - Vulkan
  - Collision and Physics
    - Havok
    - PhysX
    - Open Dynamics Engine
  - Character Animation
    - Hranny
    - Havok Aniamtion
    - OrbisAnim
  - Biomechanical Character Models: Endorphin and Euphoria
  - Platform Independence Layer
- Platform Independence Layer
- Core Systems
- Resource Manager
- Rendering Engine
  - Low-Leven Renderer
    - Graphics Device Interface
    - Other Renderer Components
  - Scene Graph/Culling Optimizations
  - Visual Effects
  - Front End
- Profiling and Debugging Tools
- Collision and Physics
  - Havok
  - PhysX
- Animation
- Human Interface Devices (HID)
- Audio
- Online Multiplayer/Networking
  - Single-screen multiplayer
  - Split-screen multiplayer
  - Networked multiplayer
  - Massively multiplayer online games (MMOG)
- Gameplay Foundation Systems：用于弥补游戏代码和底层引擎系统之间的差异的中间胶水层
  - Game Worlds and Object Models
  - Event System
  - Scripting System
  - Artificial Intelligence Foundations
  - Game-Specific Sub Systems

### Tools and the Asset Pipeline

- Digital Content Creation Tools
- The Asset Conditioning Pipeline
- The World Editor
- The Resource Database
- Some Approaches to Tool Architecture

### Tools of the Trade

#### Version Control

- SCCS & RCS
- CVS
- Subversion
- Git
- Perforce
- NxN Alienbrain
- ClearCase
- Microsoft Visual SourceSafe

#### Compilers, Liners and IDEs

- Visual Studio
- LLVM/Clang
- gcc/gdb

Project and Solutions in Visual Studio

##### Build Configuration

###### Common Build Options

- Preprocessor Settings: define macros in command line, conditional compilation
- Compiler Settings: Debugging information, inline functions expand
- Linker Settings： Type of output

###### Local and Global Optimizations

- Local Optimization: Work for code without branch, from compiler
- Global Optimization: common sub-expression elimination, from linker

ref: [nut shell](https://www.nutshell.com/)

#### Profiling Tools

ref: Pareto principle

- Statistical profilers
- Instrumenting profilers

#### Memory Leak and Corruption Detection

Rational Purify: in Purify Plus toolkit

#### Other Tools

### Fundamentals of Software Engineering for Games

#### C++ Review and Best Practices

##### Brief Review of Object-Oriented Programming

- class
  - Encapsulation
  - Inheritance: is-a
  - Multiple Inheritance: mix-in class
- Polymorphism
- Composition & Aggregation
- Design Pattern
  - Singleton
  - Iterator
  - Abstract factory
  - Janitors & RAII
  - C++ Language Standardization: 98 03 11 14 17 20 23 26
- Coding Standards
  - Interfaces are king
  - Good names encourage understanding and avoid confusion
  - Don’t clutter the global namespace
  - Follow C++ best practices
  - Be consistent
  - Make errors stick out： ref: [Wrong](http://www.joelonsoftware.com/articles/Wrong.html)

#### Catching and Handling Errors

- User errors
- Programmer errors

- Error Return Codes
- Exception handling
- Assertions: Macro
  - MSVC: `__debugbreak()`
  - GCC: `__builtin_trap()`
  - Clang: `__builtin_debugtrap()`
- Compile Time Assertions: `static_assert`

ref: Writing Solid Code Steve Maguire

ref: [static_assert](https://www.pixelbeat.org/programmaing/gcc/static_assert.html)

#### Data, Code and Memory Layout

##### Numeric Representations

- Subnormal Values
- Machine Epsilon
- Units in the Last Place (ULP)
- Impact of Floating-Point Precision on Software

##### Primitive Data Types

- char
- int, short, long
- float
- double
- bool
- `<cstdint>`
- OGRE
- Endianness
  - Little-endian
  - Big-endian
  - Integer Endian-Swapping: gcc `__builtin_bswapXX()`
  - Floating-Point Endian-Swapping: swap as of it is integer `reinterpret_cast`

kili -> kibi

mega -> mebi

giga -> gibi

tera -> tebi

peta -> pebi

exa -> exbi

zatta -> zebi

yotta -> yobi

##### Declarations, Definitions and Linkage

- Declarations
- Definitions
- inline for function in header file
- Templates and Header Files

The static keyword is used to change a definition’s linkage to internal.

##### Memory Layout of a C/C++ Program

- Text segment
- Data segment
- BSS segment
- Read-only data segment
- Stack
  - Return Address
  - CPU register
  - Local variables
- Dynamic Allocation Heap: `new` `delete`

##### Member Variables

类的静态成员必须要在cpp中初始化是因为需要在对应的.obj文件给静态成员留下空间。

- Alignment and Packing
- Inheritance
- virtual functions: Virtual table pointer

#### Computer Hardware Fundamentals

##### Learning from the Simpler Computers of Yesteryear

ref: [Inside the App IIe](http://www.apple2scans.net/files/InsidetheIIe.pdf)

ref: [x86 instruction](http://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html)

ref: Graphics Programming Black Book Michael Abrash

##### Anatomy of a Computer

- CPU
  - ALU
  - FPU
  - VPU
  - MC
  - registers
  - CU
  - Clock: MIPS & FLOPS
- Memory
  - ROM
  - RAM
- Buses

##### Machine and Assembly Language

- Instruction Set Architecture (ISA)
  - Move
  - Arithmetic operations
  - Bitwise operators
  - Shift/rotate operators
  - Comparison
  - Jump and branch
  - Push and pop
  - Function call and return
  - Interrupt
- Machine Language
  - opcode
  - operands
  - options field

ref: [MachineLanguage](http://aturing.umcs.maine.edu/~meadow/courses/cos335/Asm07-MachineLanguage.pdf)

- Assembly Language:`assembler`
  - addressing modes

ref: [x86 assemble](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

ref: [paper](https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html)

#### Memory Architectures

- Memory Mapping
  - Memory-Mapped I/O
  - VRAM
- Virtual Memory
  - Pages
  - Core dump
  - translation lookaside buffer
- Memory Architectures for Latency Reduction
  - The Memory Gap: cpu的发展速度远高于内存的发展速度
    - Cache
    - arranging instructions
    - arranging program's data
- Memory Cache Hierarchies
  - L1, L2, L3
  - cache hit & cache miss
  - Cache Lines
    - Spatial locality
    - Temporal locality
  - Cache Lines Mapping
    - direct-mapped cache
  - Multilevel Caches
  - Instruction Cache and Data Cache: Distinct in L1 cache
  - cache coherency
    - MESI
    - MOESI
    - MESIF
  - Organize your data in contiguous blocks
  - Avoid calling functions in body loop
- Nonuniform Memory Access(NUMA)
  - UMA
  - NUMA

ref: [virtual](https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Memory/virtual.html)

ref: [virtual-memory-paging-and-swapping](https://gabrieletolomei.wordpress.com/miscellanea/operating-systems/virtual-memory-paging-and-swapping/)

ref: [paper](https://www.akkadia.org/drepper/cpumemory.pdf)

### Concurrent Programming

Parallelism is a factor for computer speed up.

#### Defining Concurrency and Parallelism

A concurrent piece of software utilizes multiple flows of control to solve a problem.

- Thread
- Fibers
- Coroutines

并发的一个要点是要多个线程对共享数据进行操作。关键问题在于`数据竞争`。

- parallelism
- serial

- implicit parallelism:instruction level parallelism
  - pipelining
  - superscalar architecture
  - very long instruction word
- explicit parallelism:  running more than one instruction stream simultaneously
  - hyperthreaded CPUs
  - multicore CPUs
  - multiprocessor computers
  - computer clusters
  - grid computing
  - cloud computing

- Task parallelism
- Data parallelism

- Flynn’s Taxonomy
  - Single instruction, single data (SISD)
  - Multiple instruction, multiple data (MIMD)
  - Single instruction, multiple data (SIMD)
  - Multiple instruction, single data (MISD)
  - Single instruction, multiple thread (SIMT)

#### Implicit Parallelism

##### Pipelining

Execute command:

- Fetch
- Decode
- Execute
- Memory access
- Register write-back

CPU can execute each stage at the same time. `pipelining` makes this happened.

- latency
- throughput

pipeline depth

stalls: Bubble in instructions

dependencies cause stalls:

- data dependencies: `instructions reordering` and `out-of-order execution`(by cpu)
- control dependencies: `speculative execution`
  - `branch penalty`
  - `branch prediction` hardware
  - `predication`
- structural dependencies

#####  Superscalar CPUs

`superscalar`: multi instruction in one clock time.

`resource dependency`

`reduced instruction set` RISC

##### Very Long Instruction Word (VLIW)

eaves the task of dispatching instructions to those compute elements entirely to the programmer and/or compiler.

#### Explicit Parallelism

- hyperthreaded: CPU select from two separate instruction stream at once.
- multicore: symmetry or asymmetry
- destributed computing: Multiple stand-alone computers
  - computer clusters
  - grid computing
  - cloud computing

#### Operating System Fundamentals

##### The Kernel

- kernel mode: Has access to all of the machine language instructions in CPU, include privileged instructions.
- user mode

##### Interrupts

interrupt service routine (ISR)

- hardware interrupts
- software interrupts

##### Kernel Calls

system call: user software perform a privileged operations.

software interrupt

context switching

system call warped in to  kernel API function.

##### Preemptive Multitasking

multiprogramming

time-slicing

preemptive multitasking: operating system controlled time-slicing

##### Processes

A running instance of a program contained in an executable file.

Process anatomy:

- pid
- permissions
- parent process
- virtual memory space
- environment variables
- file handles
- working directory
- resources for synchronization and communication between process
- threads: A instance of a single stream of machine language instructions.

Every process has its own virtual page table.

- text, data and bss sections
- view of shared library
- call stack
- heap
- pages sheared with other processes
- kernel space

shared libraries can be shared between process in memory. For changed libraries no need for relinked.

##### Threads

- tid: may or may not be unique
- call stack
- registers
- thread local storage

thread libraries:

- IEEE POSIX 1003.1c standard thread library (pthread)
- c11 & c++11 thread library

- create: `pthread_create()` `CreateThread()` `std::thread`
- terminate: return `pthread_exit()`
- request to exit
- block: sleep
- yield: `pthread_join()`
- join: `pthread_join()`
- spin-wait or busy-wait or polling
- yield while polling: `pthread_yield()` `Sleep(0)`

Context Switch

- Running
- Runnable
- Blocked

Thread Priorities and Affinity

Thread Local Storage

##### Fibers

Fiber never scheduled directly by the kernel.

- create: `ConvertTHreadToFiber()` `CreateFiber()`
- terminate: `DeleteFiber()`
- yield: `SwitchToFiber()`

##### User-Level Threads

user-level threads: no need to make kernel calls.

##### Coroutines

A coroutine is a generalization of the concept of a subroutine.

The next time the coroutine is called it continues from where it left off.

ref:[Handmade Coroutines for Windows](https://probablydance.com/2013/02/20/handmade-coroutines-for-windows/)

ref:[thread introduction](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/4_Threads.html)

ref:pthread document

ref:Nikita Ishkov’s "A Complete Guide to Linux Process Scheduling" online

ref:[goroutines](https://www.youtube.com/watch?v=f6kdp27TYZs)

### Introduction to Concurrent Programming

concurrency: the composition of independently executing computations.

Using concurrent to solve match problems or just use multi core.

- Communicate
  - Message passing
  - Shared memory

distributed shared memory

#### Race Conditions

race condition: the behavior of a program is dependent on timing.

critical races: a race condition that has the potential to cause incorrect program behavior.

Data Races:  critical race condition in which two or more flows of control interfere with one another while reading and/or writing a block of shared data, resulting in data corruption.

read-modify-write operation

#### Critical Operations and Atomicity

atomic operation

invocation and response

- Preamble section
- Critical section
- Postamble section

A critical operation can be said to have executed atomically if its invocation and response are not interrupted by another critical operation on that same object.

mutex:make sure all operation executed in sequence but not specific order.

thread synchronization primitives

data-centric consistency models

ref:[data-centric consistency models](https://www.cs.cmu.edu/~srini/15-446/S09/lectures/10-consistency.pdf)

### Thread Synchronization Primitives

- atomic
- synchronize

The synchronization primitives require kernel call, and can cost upwards of 1000 clock cycles.

lock-free programming

#### Mutexes

mutex: mutually exclusive

- create() `pthread_mutex_t` `std::mutex`
- destroy()
- lock() `pthread_mutex_lock()` `std::mutex::lock()`
- try_lock()
- unlock() `pthread_mutex_unlock()` `std::mutex::unlock()`

#### Critical Section

Windows alternative for mutex

`InitializeCriticalSection()`

`DeleteCriticalSection()`

`EnterCriticalSection()`

`TryEnterCriticalSection()`

`LeaveCriticalSection()`

ref:[futex](https://www.akkadia.org/drepper/futex.pdf)

#### Condition Variables

A queue of waiting sleeping threads

#### Semaphores

semaphore: a atomic counter.

- `init()`
- `destroy()`
- `take()` `wait()`
- `give()` `signal()`

binary semaphore: can be unlocked by another thread that not locked it. Used to send a signal from one thread to another.

### Problems with Lock-Based Concurrency

Deadlock: circular dependency

- mutual exclusion
- hold and wait: reducing the number of locks
- no lock preemption
- circular wait: imposing a global order to all lock-taking in the system

Livelock: unlock all mutex if thread been blocked

Starvation: one or more threads fail to receive any execution time on the CPU.

Priority Inversion

The Dining Philosophers

### Some Rules of Thumb for Concurrency

- Global Ordering Rules
- Transaction-Based Algorithms
- Minimizing Contention
- Thread Safety

monitor: A class whose functions are all thread safe

### Lock-Free Concurrency

lock-free: Never allow a thread to block.

- Blocking
- Obstruction freedom
- Lock freedom
