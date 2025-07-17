+++
title = 'indexing_fmt'
date = 2025-05-05
link = "https://github.com/jonaspleyer/indexing_fmt"
link_display = "github.com/jonaspleyer/indexing_fmt"
tags = ['Rust']
post_image = "indexing.svg"
post_image_display = false
+++

This crate allows the formatting of integer types as superscripts or subscripts.
It is written in pure safe Rust and no_std compatible.

The necessity for this crate came up when I wanted to automatically name variables which are simply
displayed in pure UTF-8.
It simply converts any integer type into a sequence of super- or subscripts as defined by their
respective and works for all standard integer types.
In the following example, we use a ring-buffer from the [circ_buffer](/software/2024-circ-buffer)
crate to store variable values.

**Example**

```rust
use indexing_fmt::*;
use circ_buffer::RingBuffer;

let mut circ_buffer = RingBuffer::<f32, 6>::new();

// Fill with Fibonacci numbers
circ_buffer.push(0.0);
circ_buffer.push(1.0);
circ_buffer.push(1.0);
circ_buffer.push(2.0);
circ_buffer.push(3.0);
circ_buffer.push(5.0);
circ_buffer.push(8.0);

for (n, value) in circ_buffer.iter().enumerate() {
    let subscript = n.to_subscript();
    println!("x{} = {}", subscript, value);
}
```

**Output**
```text
x₀ = 1
x₁ = 1
x₂ = 2
x₃ = 3
x₄ = 5
x₅ = 8
```
