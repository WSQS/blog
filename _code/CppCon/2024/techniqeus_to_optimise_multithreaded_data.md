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
- Stale data can be fine
- Process everything in parallel

### Assumption and Concepts

Assumption

- Built on Job System, with Async IO
- Single PC
- C++17 and C++20

Terminology

- Job: unit of work
- Task: larger process converting input to output
- SpinLock: busy wait lock
- FlatMap: key-value container using sorted array for key

## Techniques

### Keep Threads Busy

Keep threads busy doing useful work.

- Make jobs roughly the same size
  - Prevents waiting on a single long job
  - Can distributed work evenly on treads
- Split long functions into jobs
- Building Large Worlds
  - Create read-only world cache for fast queries
  - Subdivide into regions to process as independent tasks
  - Some regions will take longer to process
- Dealing with exponentially long tasks
  - task that takes hours instead of minutes
  - Could be bad data, bad algorithm, or code bug
  - Method
    - Build the tasks once
    - Upload to the cache
    - Disable local processing
    - Make everyone download instead

### 3D caching

- Traditional spatial data structure
  - KD-tree, Octree, Quadtree
  - O(log n) Lookup
  - Large volume queries require multiple traversals
- Grid Cache
  - Stores static world elements for quick queries
  - Consider it a sparse 3D array
  - Process to create
    - Partition 3D space into cube grid
    - Distribute items into grid cells
    - Store non-empty cells in a map
  - Hashmap or Flatmap
    - Hashmap good for small area
    - Flatmap good for large area queries
  - Provides Large Item grid cell
  - Owned nodes and intersection nodes
  - Grid Node Class
    - Keep small and tightly packed
  - Sort using `std::tie` or using if and can inline most of the function and hide some less used function into functions.

### Optimise Sorting

- Sorting algorithms are O(n log n)
- Expensive comparison functions hurt performance
- Optimise
  - Extract needed values into separate sorting array
  - Sort the smaller sorting array
  - Ends up touch data twice

### Avoid Blocking Threads

- Be aware of hidden locks
- Use the job system to synchronies instead
- Change from spinlock to mutex
- Create second dependency chain for saving jobs
