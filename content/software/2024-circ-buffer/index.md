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
