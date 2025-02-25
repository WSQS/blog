---
title: Procedural Generation in Godot4 By Milan Gruner
date: 2025-02-24
url: https://www.bilibili.com/video/BV1q8PsePE2L/
tags:
  - Cpp
  - GodotCon
  - godot
  - perlin_noise
---

[slides](https://talks.godotengine.org/media/godotcon-24/submissions/W7BQ7N/resources/Procedural_Generation_-_GodotCon_2024_K1h3kFp.pdf)

Procedural Generation is not same as Generative AI.

## Procedural Generation Basics

Procedural Generation needs Randomness

Equal distribute probability.

Blue Noise: Poisson Disk Sampling, Relative equidistant points of a given

Simplex/ Perlin Noise

ref:RedBlobGames

Lindenmayer-System: Data Transform in Each Iteration

Wave Function Collapse

10000 bowls of oatmeal problem: Perceptual uniqueness

Find balance of Authored content and generated content

Prebuilt room layout and stitch them at runtime.

## Procedural Generation

General Approach for build a generator:

- Create hand-authored example output
- Find a pattern or repeated structure in it
- Write code to generate this structure
- Adjust things randomly or using noise to hide the structure and make it more interesting
- Add rules that enable complexity, human intent and guiding the player
- Mix in pre_authored scenes spawned using rules for more artistic control

Procedural spawning

- Build a set of rules to create objects in the world
- Perhaps start top-down
- using code or ProtonScatter

ref:ProtonScatter

Greebling

- Spawn large objects first
- Small objects decorate large objects.

ref:[ProcJam](https://procjam.com/tutorials)

ref:[Inigo Quilez's article](https://iquilezles.org/articles/palettes/)

## Example Game: Sunken Shadows

- Level Editor
- [Drunkard walk algorithm](http://pcg.wikidot.com/pcg-algorithm:drunkard-walk)
- Group solid blocks together.

## Workshop Projects

- 2d
  - Wave function collapse based generator for top-down games
- 3d
  - Using ProtonScatter to define rules for spawning meshes in worlds
  - Generating meshes with SurfaceTool, MeshDataTool, ArrayMesh
  - Generating meshes and worlds using compute shaders

[github repository](https://github.com/lemilonkh/godot-procgen)
