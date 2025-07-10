+++
title = 'peace-of-posters'
date = 2024-05-09
link = "https://github.com/jonaspleyer/peace-of-posters"
link_display = "github.com/jonaspleyer/peace-of-posters"
post_image = "dove.svg"
tags = ['Typst', 'Science']
description = "Create scientific posters in Typst."
+++

Before I headed out to the [Physics of Life](/posts/2023-03-31-physics-of-life-conference/)
conference, I had prepared a poster in $\LaTeX$ in which I really struggled.
Although I am quite familiar with $\LaTeX$, it took me quite a while to achieve the results which I
desired.
I have already summarized many of my pain-points in
[a previous post](/posts/2023-10-17-creating-posters-with-typst/).
Coming from this conference and in preparation for the next presentation at the
[bwHPC Symposium](http://localhost:1313/posts/2023-10-23-bwhpc-symposium-2023/), I started to
migrate my work from $\LaTeX$ to typst.
While the code only consisted of very little functionality in the beginning, more and more started
to pile up over time.
For the final poster at the 
[bwHPC Symposium](http://localhost:1313/posts/2023-10-23-bwhpc-symposium-2023/), I was able to
completely use my typst solution.

## peace-of-posters
The following sections describe my experience as I have worked on this project.
The full documentation of the package is hosted at
[jonaspleyer.github.io/peace-of-posters/](https://jonaspleyer.github.io/peace-of-posters/).

### Documentation
The step from a working script to a package was rather small since I had already modularized much of
my code in order to reuse it.
However, documentation of said code was still a problem.
I was very much spoiled by solutions such as `rustdoc` which generate documentation directly from
source code.
However, since the typst ecosystem is rather young, there does not exist such a solution yet.
Instead I opted to use [Hugo](https://gohugo.io/) with which I was already familiar to create a
custom solution for documenting the code.
In particular, I wrote a partial which parses Hugo markdown and then automatically detects marked
types and inserts the corresponding objects in order to nicely visualize them (see documentation of
[`boxes.typ`](https://jonaspleyer.github.io/peace-of-posters/documentation/boxes/)).

### Usage
It is straightforward to construct new posters with this package.
Simply take the [peace-of-posters template](https://typst.app/universe/package/peace-of-posters)
and modify the contents and boxes to your liking.
This can be done either via the command line

```text
typst init @preview/peace-of-posters
```
or directly in the [webapp](https://typst.app/universe/package/peace-of-posters).
To see posters which have been created by me or other users visit the
[showcase](https://jonaspleyer.github.io/peace-of-posters/showcase/) section of the documentation.

### Maintenance
The overall maintenance of `peace-of-posters` has been very smooth.
Some minor bugs have been brought forth and some users opened PRs in order to contribute to the
project.
I was very pleased with the overall interaction of the typst team.
Pushing new changes upstream via [typst-packages](https://github.com/typst/packages) has been very
straightforward.
The response time was fast.
The maintainers performed some high-level quality checking and support new contributors with any
question they might have.
