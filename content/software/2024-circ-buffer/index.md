+++
title = 'circ-buffer'
date = 2024-03-14
link = "https://github.com/jonaspleyer/circ-buffer"
link_display = "github.com/jonaspleyer/circ-buffer"
post_image = "circ-buffer-scheme.png"
post_image_display = false
tags = ['Rust']
description = "A no_std crate for a fixed-size statically allocated ring-buffer with optional serde (De)-Serialization."
+++

A `no_std` crate for a fixed-size statically allocated ring-buffer with optional serde
(De)-Serialization.

{{< highlight Rust "linenos=table" >}}
use circ_buffer::RingBuffer;

fn main() {
    // Create a new buffer
    let mut circ_buffer = RingBuffer::<u8, 4>::new();

    // Add Elements
    circ_buffer.push(3);
    assert_eq!(circ_buffer.len(), 1);
    circ_buffer.push(1);
    assert_eq!(circ_buffer.len(), 2);
    circ_buffer.push(12);
    assert_eq!(circ_buffer.len(), 3);
    circ_buffer.push(212);
    assert_eq!(circ_buffer.len(), 4);

    // Now the buffer is full and we overwrite the initial element
    circ_buffer.push(122);
    assert_eq!(circ_buffer.len(), 4);
    assert_eq!(circ_buffer[0], 2);
}
{{< /highlight >}}

## Motivation
During my development of [`celluar_raza`](https://cellular-raza.com), I implemented various
numerical solvers.
One of them was the Adams-Bashforth solver for updating position and velocities of the individual
agents.
This solver utilizes a number of previously saved integration steps `N`.
Since `cellular_raza` aims to provide flexibility in model design, the type which represents the
position or velocity of the agent must be generic.
Furthermore, since this solver only requires the last `N` steps, we can overwrite any step before
that.
This leads to the Ringbuffer datastructure.
My main problem with existing solutions was that none provided statically-sized buffers which are
very important for performance and many did not have support for `serde` which I am using
extensively.

## Design
This leads us to a datastructure which holds `N` elements of generic type `T`.
For efficient access, cache locality and efficient iteration, I chose a generic array `[T; N]` as
the underlying type.
Together with two internal counters of type `usize`, this is a very small memory footprint.
To iterate over this datastructure, I had to implement a custom type which is returned by the
[`IntoIterator`](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html) trait.
Finally, implementing `serde` was a simply matter of deriving it.
