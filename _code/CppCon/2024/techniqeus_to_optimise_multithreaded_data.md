---
title: Techniques to Optimise Multithreaded Data Building During Game Dev By Dominik Grabiec
date: 2025-03-31
url: https://www.bilibili.com/video/BV14YyfYhE3C/?p=25
tags:
  - Cpp
  - CppCon
  - multi_thread
---

## Background

### Data building

Compiling Converting Generating Cooking Baking

- Pre-computes data that is loaded by the game
- Creates additional data from existing assets
- Optimises and compresses data to make loading faster
- Includes arranging the data within files

Data Building Systems

### Difference from Game Code

Data Building

- Batch execution
- Minimise wall lock time
- System run in isolation
- Read/Write andd compress
- Developer iteration time

Optimisation Goal: Minimise the time taken to process all the game data.

- Only build things that have changed
- Cache data locally and globally

### Assumption and Concepts

## Techniques

### Keep Threads Busy

### 3D caching

### Optimise Sorting

### Avoid Blocking Threads
