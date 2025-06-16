+++
title = 'Tabular'
date = 2025-06-16
only_content = true
description = "Short CV in Tabular Form"
+++

<style>
h1,h2,h3 {
    padding-bottom: 8px;
    margin-bottom: 8px;
    border-bottom: solid 1px var(--color-border-post);
}
</style>

I am a software engineer trapped in the career of a scientist, always aiming to extend existing
functionality or to write new libraries.
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
    title = "University of Freiburg"
    employer = "MSc. Physics"
    date = "04/2020 - 07/2021"
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

## Publications

## Further Commitment

### iGEM

{{< wrap >}}{{% entry
    title = "Supervisor"
    date = "2023 - 2024"
%}}
**2024**<br>
Top 10 Overgrad, Gold Medal, Best Infectious Diseases, Nominated
for: Best Wiki, Best Presentation, best Integrated Human Practices,
Best Measurement, Best Composite Part

**2023**<br>
Top 10 Overgrad, Gold Medal, Nominated for: Best Foundational
Advance Project, Best New Composite Part, Best Wiki

{{% /entry %}}{{< /wrap >}}

### Badminton

{{< wrap >}}{{% entry
    title = "State-recognized Coach for the competitive Sport Badminton License level B"
    employer = "Deutscher Badminton Verband (DBV)"
    date = "2019"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "State-recognized Coach for the competitive Sport Badminton License level C"
    employer = "Deutscher Badminton Verband (DBV)"
    date = "2018"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "Honorary Trainer of Children and Adults"
    employer = "FT Freiburg 1844"
    date = "since 01/2020"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "Honorary Trainer of Children and Adults"
    employer = "TSG Wiesloch"
    date = "2016 - 2019"
%}}{{% /entry %}}{{< /wrap >}}

### Camp KjG Wiesloch

{{< wrap >}}{{% entry
    title = "Board Member (Lagerleitung)"
    employer = "KjG Wiesloch"
    date = "11/2020 - 11/2021"
%}}{{% /entry %}}{{< /wrap >}}

{{< wrap >}}{{% entry
    title = "Active honorary member in organizing and conducting the yearly camp and further events"
    employer = "KjG Wiesloch"
    date = "10/2011 - 01/2024"
%}}{{% /entry %}}{{< /wrap >}}

### FIRST LEGO League

{{< wrap >}}{{% entry
    title = "Participation at Competitions of the \"FIRST LEGO League\""
    employer = "Nemo Kids"
    date = "2008 - 2011"
%}}
**2011** 7th in Germany

**2010** 3rd in Germany, 9th in Europe
{{% /entry %}}{{< /wrap >}}
