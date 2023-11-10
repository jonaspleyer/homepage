+++
title = 'Scientific Computing in Rust 2023'
date = 2023-05-22T10:04:00+02:00
post_image = "ferris-scientific-computing-1536x1147.png"
tags = ['Math', 'Programming', 'Science']
+++

Last week I attended the [Scientific Computing in Rust 2023](https://scientificcomputing.rs/) virtual conference. The organizers put together a well-stirred mixture of talks covering a wide range of topics. It was good to see so many other enthusiastic researchers using [Rust](https://www.rust-lang.org/) as their main tool to build software surrounding computational needs.

The invited speakers Gonzalo Brito, Sarah El Kazdadi and Manuel Drehwald had particularly interesting talks. Gonzalo presented a Lattice-Boltzmann CFD solver as an application of [rayon](https://github.com/rayon-rs/rayon), Rusts multithreading library. Sarah presented [faer-rs](https://github.com/sarah-ek/faer-rs), an implementation of low-dimensional linear algebra routines which could in the future be used as a backend to popular crates such as [nalgebra](https://github.com/dimforge/nalgebra) or [ndarray](https://github.com/rust-ndarray/ndarray). Manuel’s talk evolved around a heavily modified version of the rust compiler called [rust-enzyme](https://github.com/EnzymeAD/rust) to bring auto-differentiation to the Rust language.

A common problem and question of many attendees was regarding GPU-specific functionality and libraries. At the moment, there does not seem to be a unified crate which the community has agreed upon to use or that even offers every feature desirable. [wgpu](https://github.com/gfx-rs/wgpu) aims to provide a useful graphics API which can also be exploited for numerical computations. [rust-cuda](https://github.com/Rust-GPU/Rust-CUDA) and [rust-gpu](https://github.com/EmbarkStudios/rust-gpu) are two other crates in this space. While wgpu and rust-gpu compile native Rust code to [SPIR-V](https://en.wikipedia.org/wiki/Standard_Portable_Intermediate_Representation), rust-cuda provides direct access to low-level bindings of the [CUDA](https://developer.nvidia.com/cuda-toolkit) framework by NVIDIA. Similarly, there exist libraries functioning as wrappers for popular C++ graphics libraries such as [arrayfire-rust](https://github.com/arrayfire/arrayfire-rust). For the next conference, I am looking forward to more interesting talks tackling this problem.

All together, I can only say positive things about the event and I hope to be attending again in the near future.

Image Credit: [scientificcomputing.rs/ferris](scientificcomputing.rs/ferris)
