+++
title = 'cellular_raza - Happy Birthday'
date = 2025-08-27T11:02:14+02:00
post_image = "cellular_raza_dark_mode.png"
description = "Today, my PhD project cellular_raza turns 3 years old. It is and has been a very enlightening journey. Let me elaborate .."
+++

My journey of using Rust as my primary programming language started with the inception of
`cellular_raza`.
At first, my ambitions were very simple:
Start a toy project in order to learn a new and promising programming language which was already
very much loved by the community.
Today, this project has grown a lot and celebrates its 3rd birthday.

## The development process

As you can see from my initial commit, the first iteration was just a simple
[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

```text
commit d2c9464b4bd5a5ee19a2c247069865f7a6d6c5b9
Author: Jonas Pleyer <jonas.pleyer@fdm.uni-freiburg.de>
Date:   Sat Aug 27 23:14:50 2022 +0200

    initial commit: cartesian conway example
```

Fast-forward to the 15th of September where commit
[`2ee03a09e9d4c19aa8cdd427a1252a2eb7b07e94`](https://github.com/jonaspleyer/cellular_raza/commit/2ee03a09e9d4c19aa8cdd427a1252a2eb7b07e94)
introduced the first working prototype for an agent-based model.
This layed the very foundation for the resulting structure of `cellular_raza`.
The changes from the initial commit to this state show a separation of concepts, helpers such as
database, implementations such as the domain and solvers.

```text
 .cargo/config.toml                 |  14 ++++
 .gitignore                         |   3 +
 Cargo.toml                         |  12 ++-
 LICENSE.md                         |   0
 README.md                          |   2 +
 examples/template/main.rs          | 115 ++++++++++++++++++++++++++
 examples/template/setup.rs         |  81 ++++++++++++++++++
 src/cell_properties/cell_model.rs  |  16 ++++
 src/cell_properties/cycle.rs       |  16 ++++
 src/cell_properties/death.rs       |   8 ++
 src/cell_properties/interaction.rs |  11 +++
 src/cell_properties/mod.rs         |   5 ++
 src/cell_properties/spatial.rs     |  47 +++++++++++
 src/concepts/cell_properties.rs    |   0
 src/concepts/domain.rs             |   6 ++
 src/concepts/errors.rs             |   4 +
 src/concepts/mod.rs                |   4 +
 src/concepts/spatial.rs            |   0
 src/database/mod.rs                |   0
 src/database/write.rs              |   0
 src/domain/cuboid.rs               |  29 +++++++
 src/domain/mod.rs                  |   1 +
 src/lib.rs                         |   3 +
 src/methods/mod.rs                 |   0
 tools/plot.py                      |  43 ++++++++++
 tools/potential.py                 |  29 +++++++
 26 files changed, 447 insertions(+), 2 deletions(-)
```

This very separation became a key concept throughout the entire development process.
By using such clear separations, `cellular_raza` allows users to define their own agents and domains
bottom-up and thus allows for much greater flexibility to design agents and the domain in which they
live.
It is the core feature of this project.
With this mechanism, researchers can investigate many different systems instead of being stuck to
study just a single one in particular.
Furthermore, effective model-reductions where the core components of the cellular representation
need to be changed are not only possible but also supported and encouraged.

Today we distinguish between 3 core components which are hosted by individual crates.
The `cellular_raza` crate, combines all of them (see also
[cellular-raza.com/internals/code-structure](https://cellular-raza.com/internals/code-structure/))
for more convenient access.

```text
cellular_raza-concepts
cellular_raza-core
cellular_raza-building-blocks
cellular_raza
```

To summarize this, `cellular_raza` as a project encourages researchers to think in terms of actual
modeling instead of in terms of "What can I achieve with the given simulation code that somebody
else wrote 10 years ago and is not designed to be adaptable?"

## Achievements

Apart from all the knowledge which I was able to gather within the Rust ecosystem, my Supervisor and
I published `cellular_raza` in the
[Journal of Open Source Software](https://joss.theoj.org/papers/10.21105/joss.07723).
It was also used in other publications (see
[cellular-raza.com/publications](https://cellular-raza.com/publications]) and by other researchers
which overall had only positive things to say about it.
I also had the opportunity to present my work at the
[Scientific Computing in Rust](/posts/2025-06-04-scientific-computing-in-rust/) conference in a
short-talk.

## What did I learn?

Where do I begin to answer this question?
I learned **A LOT**.
Concerning the Rust ecosystem, I learned how to build, patch and maintain your own crates.
Furthermore, I got to know many other projects such as
[`plotters`](https://docs.rs/plotters/latest/plotters/) or
[`nalgebra`](https://docs.rs/nalgebra/latest/nalgebra/) along the way and had the opportunity to
inspect their inner workings.

Especially during the migration from the
[cpu_os_threads](https://cellular-raza.com/internals/backends/cpu-os-threads/) to the
[chili](https://cellular-raza.com/internals/backends/chili/) backend, I had to learn the hard way
what it means to own your solutions.
I had previously used the first one extensively and now had to convert some simulation code.
And although most of that went pretty smoothly, the way to get there took some work.
Finally I was thrilled with the overall improvements in ergonomics and performance.

Another neat experience was when I discovered how easily it is possible to use my crate and
construct python bindings with [`pyo3`](https://docs.rs/pyo3/latest/pyo3/) and
[`maturin`](https://github.com/PyO3/maturin).
In this way I was able to utilize all of my existing visualization and data-analysis workflows and
combine it with my Rust-based crates.
Definitely a game-changer from my point of view.

## Final Verdict

Would I do it again? - Sure if I will ever have the time and be paid well.
But you should also consider: I am still actively involved in maintaining `cellular_raza` and using
it myself on a daily basis.
So there is no end to this yet.

Image reference:
<a href="https://www.flaticon.com/free-stickers/party-hat">Support from Flaticon</a>
