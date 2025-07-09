+++
title = 'crate2bib'
date = 2025-02-06
link = "https://github.com/jonaspleyer/crate2bib"
link_display = "github.com/jonaspleyer/crate2bib"
post_image = "logo.png"
tags = ['Rust', 'science']
description = "A crate to generate a BibTeX entry from a given crate name and optional version number."
+++

I often write scientific texts in which I need to cite existing work.
However, citing crates can be a hassle since most do not provide predefined citation and so you have
to scramble together your very own version of it.
But this problem should be solvable.
After all, basically all crates are published on crates.io from which we can retrieve metadata in
order to automatically generate our very own BiBTeX entry.

## Base Crate
The base crate is a pure Rust library.
It relies on multiple dependencies, most notably [reqwest](https://crates.io/crates/reqwest),
[biblatex](https://crates.io/crates/biblatex),
[citeworks-cff](https://crates.io/crates/citeworks-cff) and modified version of the
[crates_io_api](https://crates.io/crates/crates_io_api) crate which provides wasm support:
[crates_io_api-wasm-patch](https://crates.io/crates/crates_io_api-wasm-patch).
The last modification was necessary in order to provide Wasm support for the [webapp](#webapp).
Its main functionality is provided by the `get_biblatex` function.

```Rust {linenos=table}
#[async_std::main]
async fn main() -> crate2bib::Result<()> {
    let crate_name = "serde";
    let version = Some("1.0.219");
    let user_agent = Some("my-user-agent");

    let entries = crate2bib::get_biblatex(
        crate_name,
        version,
        user_agent,
        None,// branch name
        vec!["CITATION.cff", "citation.bib"]
    ).await?;

    for entry in entries {
        println!("{}", entry);
    }

    Ok(())
}
```

The `get_biblatex` function retrieves information from [crates.io] and then queries the github
repository for more information.
It also searches for additional files which might contain a bibliography entry.
At the time of writing, 2 formats are supported: `CFF,BibLaTeX`.
The base crate also provides functions for only querying [github.com](https://github.com) or
[crates.io](https://crates.io).

The base crate also contains python bindings which are generated with [pyo3](https://pyo3.rs/)
and [maturin](https://github.com/PyO3/maturin) and automatically published to
[pypi](https://pypi.org/project/crate2bib/).

```python {linenos=table}
import asyncio
from crate2bib import get_biblatex

results = await get_biblatex(
    "serde",
    "1.0.219",
    "crate2bib-py-testing-serde-user-agent"
    # Optional arguments branch_name & filenames were omitted
)

expected = "\
@software {Tolnay2025,\n\
    author = {David Tolnay},\n\
    title = {{serde}: A generic serialization/deserialization framework},\n\
    url = {https://github.com/serde-rs/serde},\n\
    date = {2025-03-09},\n\
    version = {1.0.219},\n\
    license = {MIT OR Apache-2.0},\n\
}"

assert results[0] == expected
```

## Cli
The [crate2bib-cli](https://crates.io/crates/crate2bib-cli) crate provides a simply interface for
using the crate from the command line.

```text
[user@machine ~]$ crate2bib nalgebra -v 0.33
Generated enty from crates.io information
@software {Crozet2024,
    author = {Sébastien Crozet},
    title = {{nalgebra}: General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices.},
    url = {https://github.com/dimforge/nalgebra},
    date = {2024-10-29},
    version = {0.33.2},
    license = {Apache-2.0},
}
```

## WebApp
The [crate2bib-app](https://jonaspleyer.github.io/crate2bib/) uses [dioxus](https://dioxuslabs.com/)
for the web-app.
Building project was relatively straightforward due to the Wasm support of crate2bib.
It is automatically built and hosted on the Github-provided pages of the repository.
