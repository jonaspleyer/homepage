+++
title = 'Downloading Files with Progress Bars in Rust'
date = 2025-09-02
tags = ['Rust']
link = 'https://github.com/jonaspleyer/2025-09-02-download-file-progress-bar-rust'
post_image = 'progress_bar_screenshot.png'
+++

I could not find any short snippets on how to download files in Rust using a progress bar.
So here is my take on it.

During the past days, I was working on a project in which I wanted to analyze specific crates of the
Rust ecosystem.
To do this I wanted to download the dump of [crates.io] which is described in the
[Data Access Policy](https://crates.io/data-access).
Since the [`async_std`](https://crates.io/crates/async_std) has been discontinued and recommends to
use [`smol`](https://crates.io/crates/smol), I did pick it up as well for my async runtime.
However, if you want to combine it with [`reqwest`](https://crates.io/crates/reqwest/), there are
some challenges.
`reqwest` expects a running tokio adapter and will introduce runtime panics if it cannot find it.
Therefore, we have to also use the [`async_compat`](https://crates.io/crates/async_compat) crate
which was specifically designed to circumvent these challenges.
Additionally, I want to provide a progress bar for which I will use
[`kdam`](https://crates.io/crates/kdam).
Finally, to not having to worry about any errors, I use [`anyhow`](https://crates.io/crates/anyhow).

```rust
use anyhow::Result;

const DB_DUMP_LINK: &str = "https://static.crates.io/db-dump.tar.gz";

// This applies the `main` macro of the smol_macro crate.
#[macro_rules_attribute::apply(smol_macros::main)]
async fn main() -> Result<()> {
    // Open a file to store the downloaded data.
    let mut file = smol::fs::File::create("/temp/db-dump.tar.gz").await?;

    // Create request and obtain response
    // Note: We need to use async_compat for compatibility with tokio.
    let request = async_compat::Compat::new(reqwest::get(DB_DUMP_LINK));
    let mut response = request.await?;

    // Obtain the number of total bytes in the response
    let total_bytes = response.content_length().unwrap_or_default() as usize;

    // Define the format of the progress bar
    let bar_format = "{desc}{percentage:3.0}%|{animation}| {count}/{total} [{elapsed} {rate:.2}{unit}/s{postfix}]";

    // Construct a new progress bar
    let mut pb = kdam::BarBuilder::default()
        .total(total_bytes)
        .unit_scale(true)
        .unit("Mb")
        .bar_format(bar_format)
        .build()
        .unwrap();

    // Main loop to obtain chunks iteratively
    while let Some(chunk) = response.chunk().await? {
        // Write next chunk to file
        use smol::io::AsyncWriteExt;
        file.write_all(&chunk).await?;

        // Update progress bar
        use kdam::BarExt;
        pb.update(chunk.len())?;
    }

    Ok(())
}
```

And voila!
The resulting output looks quite nice.

```text
# cargo run -r
    Finished `release` profile [optimized] target(s) in 0.07s
     Running `target/release/download_file`
 45%|██████████████████▋                      | 532M/1.18G [00:08 64Mb/s]
```

For completeness the `Cargo.toml` file which I have used.

```toml
[package]
name = "download_file"
version = "0.1.0"
edition = "2024"

[dependencies]
anyhow = "1.0.99"
async-compat = "0.2.5"
kdam = { version = "0.6.3", features = ["template"] }
macro_rules_attribute = "0.2.2"
reqwest = "0.12.23"
smol = "2.0.2"
smol-macros = "0.1.1"
```

## Note
If you want to use this snippet to download files when they are not present, remember to not only
check that the file exists but also that it is complete.
You can achieve this by comparing the `total_bytes` variable with the actual file-size.
It would be even better to compare checksums of course.
