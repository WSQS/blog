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

Vulkan allows you to enable extensive checks through a feature known as validation layers.

## Development environment

- [Vulkan SDK](https://vulkan.lunarg.com/)
- [GLFW](https://www.glfw.org/download.html)
- [GLM](https://github.com/g-truc/glm/releases)

ref:[makefile tutorial](https://makefiletutorial.com/)

## Drawing a triangle

### Setup

#### Base code

##### General structure

- Init Vulkan
- Main Loop
- Clean Up

##### Resource Management

Vulkan's niche is to be explicit about every operation to avoid mistakes.

Vulkan objects are either created directly with functions like vkCreateXXX, or allocated through another object with functions like vkAllocateXXX. After making sure that an object is no longer used anywhere, you need to destroy it with the counterparts vkDestroyXXX and vkFreeXXX.

The parameters for these functions generally vary for different types of objects, but there is one parameter that they all share: pAllocator. This is an optional parameter that allows you to specify callbacks for a custom memory allocator. We will ignore this parameter in the tutorial and always pass nullptr as argument.

##### Integrating GLFW

`glfwInit()` `glfwTerminate()`

`glfwCreateWindow(WIDTH, HEIGHT, "Vulkan", nullptr, nullptr)`The first three parameters specify the width, height and title of the window. The fourth parameter allows you to optionally specify a monitor to open the window on and the last parameter is only relevant to OpenGL.

`glfwDestroyWindow(window)`

#### Instance

The instance is the connection between your application and the Vulkan library and creating it involves specifying some details about your application to the driver.

VkApplicationInfo contains some information about our application.

VkInstanceCreateInfo include extension and validation layer info for create instance.

vkCreateInstance.

The general pattern that object creation function parameters in Vulkan follow is:

- Pointer to struct with creation info
- Pointer to custom allocator callbacks, always nullptr in this tutorial
- Pointer to the variable that stores the handle to the new object

`vkCreateInstance` `vkDestroyInstance`

#### Validation layers

Because Vulkan requires you to be very explicit about everything you're doing, it's easy to make many small mistakes like using a new GPU feature and forgetting to request it at logical device creation time.

Validation layers are optional components that hook into Vulkan function calls to apply additional operations. Common operations in validation layers are:

- Checking the values of parameters against the specification to detect misuse
- Tracking creation and destruction of objects to find resource leaks
- Checking thread safety by tracking the threads that calls originate from
- Logging every call and its parameters to the standard output
- Tracing Vulkan calls for profiling and replaying

VK_LAYER_KHRONOS_validation

##### Message Callback

Handel debug message in explicit callback.

VK_EXT_debug_utils extension

`VkDebugUtilsMessengerEXT`

#### Physical devices

`VkPhysicalDevice` `VkPhysicalDeviceProperties` `VkPhysicalDeviceFeatures`

#### Queue families

`vkGetPhysicalDeviceQueueFamilyProperties`

#### Logical device

`VkDevice` `VkDeviceQueueCreateInfo` `VkPhysicalDeviceFeatures` `VkDeviceCreateInfo`

### Presentation

#### Window surface

`VK_KHR_surface` `VkSurfaceKHR`
