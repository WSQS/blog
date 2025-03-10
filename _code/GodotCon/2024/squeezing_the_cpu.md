---
title: "Squeezing the CPU: Multi-THreading in Godot by Pedro J. Estébanez"
date: 2025-03-06
url: https://www.bilibili.com/video/BV14ZRAYAE9H/
tags:
  - GodotCon
  - godot
---

ref: [github account](https://github.com/RandomShaper)

ref: W4 consoles

## Gentle Intro to Threading

- RAM
- CPU: Able to run multi instructions at the same time.

Hyper Thread let cpu do 30% more work.

- Hardware Thread
- Software Thread

## Godot Threading Overview

- Building Blocks
  - Basic sync primitives:
    - Mutex, BinaryMutex, Semaphore
    - RWLock
    - ConditionVariable: let thread wait for event
  - Atomics:
    - SafeRefCount
    - SafeNumeric
    - SafeFlag:bool
  - Thread

ref:`std::atomic`

ref:`SafeBinaryMutex`

LANDSCAPE

- Main
- Main and Godot Main
- RemoteDebuggerPeerTCP
- WorkerThreadPool
- IP(resolver)
- ThorVG
- Audio driver
- Arbitrary threads
- Many non-Godot others(input, rendering)

## WorkerThreadPool

N threads(N = Logical CPU(Hardware Thread) count by default)

MAX(1, N * low-prio-ratio(default is 0.3)) eligible for low-prio tasks

```pseudocode
while !exit
  IF task = queue.POP()
    RUN(task)
  ELSE
    self.cond_var.WAIT()
  END-IF
```

Add task

Waiting in thread pool.

fibers

### Use cases

- Particles' collisions
- 2D physics
- Shader Variants compilation
- Navigation: avoidance
- Threaded node processing
- Resource loading

ref:Godot Sprint

ref:[Multi-threaded Scene Processing in Godot 4.1+](https://www.youtube.com/watch?v=WuH3TiVnuaw)

ref:[godot events](https://godotengine.org/events/)

### Deadlock prevention

Add task id and compare to avoid dead lock, return ERR_BUSY.

## Servers

Thread models

- Single unsafe
- Single safe: ServerWrapMT + CommandQueueMT::flush_all
- Separate thread: ServerWrapMT + CommandQueueMT::sync

## A few tips

- Read document
- Inter-node comm: no signals, no node group calls, use deferred calls
- custom resource loader: connect/ disconnect. emit_change()
- short-lived tasks: WorkerThreadPool
- long-lived tasks: custom thread, stick to the basic
- main scene tree is unsafe: load and instantiate, defer insertion
- if safe, prevent thread guards: `thread.set_thread_safety_checks_enable(true)`
- Servers are safe, just be sure not to cause syncs
