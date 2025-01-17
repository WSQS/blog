---
title: Vulkan Tutorial
date: 2025-01-16
url: https://vulkan-tutorial.com
tags:
  - computer_graphics
---

## Introduction

ref:[Learning Modern 3D Graphics Programming](https://paroj.github.io/gltut/)

ref:[Ray Tracing in One Weekend Book Series](https://github.com/RayTracing/raytracing.github.io)

ref:[Physically Based Rendering book](https://www.pbr-book.org)

## Overview

### Origin of Vulkan

Vulkan适应现代的GPU，提供更多的抽象，支持多线程。

### What it takes to draw a triangle

- Instance and physical device selection: VkInstance VkPhysicalDevice
- Logical device and queue families: VkDevice(logical device) VkQueue
- Window surface and swap chain: GLFW SDL VkSurfaceKHR VkSwapchainKHR
- Image views and framebuffers: VkImageView VkFramebuffer
- Render passed: VkFramebuffer
- Graphics pipeline: VkPipeline VkShaderModule
- Command pools and command buffers: VkCommandBuffer VkCommandPool
- Main loop: vkAcquireNextImageKHR vkQueueSummit vkQueuePresentKHR

## API concepts

### Coding convention

All of the Vulkan functions, enumerations and structs are defined in the vulkan.h header.

Functions have a lower case vk prefix, types like enumerations and structs have a Vk prefix and enumeration values have a VK_ prefix.

### Validation layers

Vulkan allows you to enable extensive checks through a feature known as validation layers.

## Development environment

- [Vulkan SDK](https://vulkan.lunarg.com/)
- [GLFW](https://www.glfw.org/download.html)
- [GLM](https://github.com/g-truc/glm/releases)

## Drawing a triangle

### Setup

#### Base code

##### General structure

- Init Vulkan
- Main Loop
- Clean Up

##### Resource Management

Vulkan's niche is to be explicit about every operation to avoid mistakes.

Vulkan objects are either created directly with functions like vkCreateXXX, or allocated through another object with functions like vkAllocateXXX.
