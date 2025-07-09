+++
title = 'approx-derive & approxim'
date = 2025-05-05
link = "https://github.com/jonaspleyer/approx-derive"
link_display = "github.com/jonaspleyer/approx-derive"
tags = ['Rust']
post_image = "image.png"
description = "Provides derive macros for the popular approx crate. Approxim is a fork of approx which includes additional functionality."
+++

During my development of [cellular_raza](https://cellular-raza.com), I often came across the task of
comparing floating point numbers, especially during testing.
The Rust ecosystem has the [aprox](https://docs.rs/approx/latest/approx/) crate which is popular for
this use-case and widely used.
But the crate was missing derive macros for the `AbsDiffEq` and `RelativeEq` traits.
So I decided to fix this by providing an external crate `approx-derive` which addresses this
problem.

## Functionality

The crate only provides the two derive macros `AbsDiffEq` and `RelativeEq` which generate
implementations of the identically-named traits.
It relies mainly on [syn](https://crates.io/crates/syn/) for parsing code,
and [quote](https://crates.io/crates/quote) for generating code.

The following example shows how to use the derive macro.
During the development and usage of this crate, I have added multiple features (see
[docs.rs/approx-derive](https://docs.rs/approx-derive/latest/approx_derive/)).

```Rust {linenos=table}
use approx::assert_abs_diff_eq;
use approx_derive::AbsDiffEq;

#[derive(AbsDiffEq, PartialEq, Debug)]
struct Player {
    x: f64,
    y: f64
    #[approx(equal)]
    id: (u64, u16),
}

#[test]
fn test() {
    let player1 = Player {
        x: 1.0,
        y: 2.0,
        id: (0, 0),
    };
    let player2 = Player {
        x: 1.1,
        y: 1.9,
        id: (0, 0),
    };
    assert_abs_diff_eq!(player1, player2, epsilon = 0.11);
    assert_abs_diff_ne!(player1, player2, epsilon = 0.01);
}
```

## Approxim
At the time of writing, the [approx](https://docs.rs/approx/latest/approx/) crate has not been
updated since $\approx$ 3 years and many PRs and feature requests have been ignored.
Furthermore, derive macros have not been added to the crate.
For this reason, I have forked [approx](https://docs.rs/approx/latest/approx/), creating
[approxim](https://github.com/jonaspleyer/approxim) which includes all open PRs as well as derive
macros.
In order to provide a working solution for two crates with different names, I needed to infer the
name of the crate automatically.
I guarded this functionality behind the `infer_name` feature which does not have to be activated
when using with [approx](https://docs.rs/approx/latest/approx/).
Although this crate exists, I hope that my solution for derive macros will be incorporated within
`approx` at some point in the future.
