+++
title = 'EuroRust 2025'
date = 2025-10-09
post_image = "logo-250307.svg"
tags = ['Conference', 'Rust', 'Programming']
+++

Over the past two days I attended the [EuroRust 2025](https://eurorust.eu/) conference.
The talks very very interesting, covering a wide range of topics.
In particular, I very much enjoyed 3 talks which I want to talk about briefly.

## [Rust/C++ Interop: Carcinization or Intelligent Design](https://eurorust.eu/2025/talks/rust-c-plus-plus-interop/)
A very interesting talk about the need for the Rust ecosystem to "play nice" with C++ within the
same sandbox.
I cannot agree more with this sentiment.
I find, that some programmers view C++ too negatively.
If anything, we should be grateful for the technologies and advancements that languages such as C
and C++ have given us.
Many design principles of C++ have been translated directly into Rust and are simply awesome.

The talk was by [Victor Ciura](https://ciura.ro/), who works for Microsoft.
It is good to see the commercial interest in the Rust language since long-term viability and broad
adoption can only be assured with commercial support.
The talk was about various tools which can be used for interop.
I was particularly interested in the talk since I have started to work on
[vtk-rs](https://github.com/jonaspleyer/vtk-rs).
His key points were that we have so far not made it yet and that we should pick whichever tool suits
our pupose the best.
Here is a short list of some tools

- [cbindgen](https://github.com/mozilla/cbindgen)
- [rustbindgen](https://github.com/rust-lang/rust-bindgen)
- [cxx](https://cxx.rs/)
- [crubit](https://github.com/google/crubit)

## [Trust your Benchmarks, Not your Instincts: A Rust Performance Quiz](https://eurorust.eu/2025/talks/trust-your-benchmarks/)
This talk by [Arthur Pastel](https://www.linkedin.com/in/arthurpastel/) and
[Adrien Cacciaguerra](https://www.linkedin.com/in/adrien-cacciaguerra/) was a lot of fun.
The speakers presented small code snippets and asked questions related to the performance of the
code.
Everyone was able to participate in this quiz via an online form and the correct answer was
explained promptly.
Most notably It was made clear that almost all mini-optimizations such as inline assembly, manual
loop unrolling, etc. are not necessary since the compiler will mostly handle this better.

## [Rendering at 1 Million Pixels / Millisecond with gpui](https://eurorust.eu/2025/talks/rendering-at-1-million-pixels-millisecond-with-gpui/)
The final keynote of day 1 was a very memorable experience.
The speaker, [Conrad Irwin](https://github.com/conradirwin) is known for many things but works on a
novel code editor [zed](https://zed.dev/) which uses GPU acceleration to reach very fast speeds.
His talk was a mixture of hist personal story and overcoming technical challenges and overall very
inspiring.
I am looking forward to testing out Zed in the future and am glad that there is a competitor for
VSCode.
