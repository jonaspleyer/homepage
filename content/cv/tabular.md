+++
title = 'Tabular'
date = 2025-06-16
only_content = true
description = "Short CV in Tabular Form"
+++

<style>
h1,h2 {
    padding-bottom: 8px;
    margin-bottom: 8px;
    border-bottom: solid 1px var(--color-border-post);
}
</style>

I am a software engineer trapped in the career of a scientist, always aiming to extend existing
functionality or write new libraries.
I care about functionality, quality and team spirit.
To me, any temporary solution is undesirable.

## Experience

{{< wrap >}}{{% entry
    title = "Doctoral Candidate"
    employer = "University of Freiburg"
    location = "Freiburg im Breisgau"
    date = "since 08/2021"
    style = "background:#344A9A;"
%}}

- Development and Implementation of novel agent-based simulation framework cellular_raza in Rust
    - Induced more development in the broader Rust ecosystem
- Applications in cell-based systems; bacterial branching patterns, mechanics of rod-shaped bacteria
- Theoretical methods for individual-based numerical simulation frameworks

{{% /entry %}}{{< /wrap >}}

<br>

{{< wrap >}}{{% entry
    title = "Tutor"
    employer = "University of Freiburg"
    location = "Freiburg im Breisgau"
    date = "since 04/2020"
    style = "background:linear-gradient(to top, #5D6BAD, #344A9A);"
%}}

- Lectures: Elementargeometrie, Analysis I, Analysis II, Analysis III, Einführung in die
  Systembiologie, Experimentalphysik I, Theoretische Physik III, Höhere Mathematik II
- Preparation and correction of mandatory work sheets and exams, lecture substitute for Prof.

{{% /entry %}}{{< /wrap >}}

<br>

{{< wrap >}}{{% entry
    title = "HiWi"
    employer = "Fraunhofer Institute ISE Freiburg"
    location = "Freiburg im Breisgau"
    date = "02/2020 - 04/2021"
    style = "background: #009374"
%}}

- Uncertainty estimation for heat pumps and sensors, eco-label validation and assignment

{{% /entry %}}{{< /wrap >}}

<br>

{{< wrap >}}{{% entry
    title = "Internship"
    employer = "SAP"
    location = "Walldorf"
    date = "08/2017 - 10/2017"
    style = "background: #006BB8"
%}}

- Machine Learning, AI, Natural Language Processing, Python

{{% /entry %}}{{< /wrap >}}

## Skills

**Programming Languages:** Rust, Python, C++, C<br>
**Other Tools:** $\LaTeX$, Typst, Github CI, Hugo

## Selected Projects

{{< wrap >}}{{% entry
    title = "cellular_raza"
    date = "since 08/2021"
%}}
`cellular_raza` is a library to construct numerical simulations cellular systems.
It is written in Rust with templates and generics and thus allows for user-defined
designs of agents from a clean slate.
It is well-documented (see [cellular-raza.com](https://cellular-raza.com))
with guides and showcases as well as peer-reviewed and published.
Throughout my PhD, my own use-cases and requirements by collaborators required me to
frequently extend and maintain the package which taught me valuable lessons in the mid and
long-term support of software.
Its development sparked many more contributions in the broader Rust ecosystem
([github.com/jonaspleyer/cellular_raza](https://github.com/jonaspleyer).
{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "cr_mech_coli"
    date = "since 10/2024"
%}}
This Python package allows to simulate rod-shaped bacteria as well as automatically estimate
their mechanical parameters by fitting to time series of microscopic images.
It uses the packages `cellular_raza,ndarray,nalgebra` in the numerical Rust code and
`numpy,scipy,matplotlib,pyvista` for analysis, initialization and visualization.
Bindings between Rust and Python are generated using `pyo3` and `maturin`.
{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "peace-of-posters"
    date = "since 10/2023"
%}}
I created this package since I was unsatisfied with existing solutions to create scientific posters.
It uses the new `typst` typesetting system and is being used frequently by other PhD students.
{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "approx-derive"
    date = "04/2024"
%}}
This extends the existing crate `approx` which enables approximate comparison of floating point
operations.
It allows users to very quickly implement its functionality by using derive macros.
{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "vtk-rs"
    date = "05/2025"
%}}
This crate provides interoperability between Rust and a subset of the Visualization Toolkit (VTK)
C++ library.
It uses multiple technologies such as [cmake](https://cmake.org), [cxxbridge](https://cxx.rs)
and [WrapVTK](https://vtk.org) to automate boilerplate generation of the bindings.
{{% /entry %}}{{< /wrap >}}

## Education

{{< wrap >}}{{% entry
    title = "University of Freiburg"
    employer = "Doctoral Candidate (Computational Systems Biology)"
    date = "since 08/2021"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "Heidelberg University"
    employer = "MSc. Physics"
    date = "04/2018 - 04/2020"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "Heidelberg University"
    employer = "BSc. Physics"
    date = "09/2013 - 03/2018"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "Ottheinrich-Gymnasium"
    employer = "High School"
    date = "09/2005 - 06/2013"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "Schillerschule Wiesloch"
    employer = "Elementary School"
    date = "09/2001 - 06/2005"
%}}{{% /entry %}}{{< /wrap >}}
