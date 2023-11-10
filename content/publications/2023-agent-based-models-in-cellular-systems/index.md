+++
title = 'Agent Based Models in Cellular Systems'
date = 2023-01-04T14:00:00+02:00
post_image = "turing-pattern.png"
post_image_display = false
link = "https://doi.org/10.3389/fphy.2022.968409"
link_display = "doi.org/10.3389/fphy.2022.968409"
tags = ['paper','mini-review']
+++

This mini-review discusses agent-based models as modeling techniques for studying pattern formation of multi-cellular systems in biology. We introduce and compare different agent-based model frameworks with respect to spatial representation, microenvironment, intracellular and extracellular reactions, cellular properties, implementation, and practical use. The guiding criteria for the considered selection of agent-based model frameworks are that they are actively maintained, well documented, and provide a model development workflow.

<div style="text-align: center;">
    <img alt="An agent-based model of cells organizing along a turing pattern" src="turing-pattern.png" style="width: 90%; max-width: 1000px;">
    <figcaption>
        FIGURE 1. We implemented a RD system (see also Supplementary Equation SB1-SB4–Equations) in an ABM to showcase results. The simulation contains two distinct cell types, which are both motile and initially randomly distributed. Cell type I (blue-shaded, white border) obey reaction equations given by a substrate-depletion system [1] and are colored by their internal concentration of the activator. Cell type II (orange) is smaller than cell type I and is chemotactically attracted by the activator which is secreted by cell type I. The background displays the density profile of the secreted activator molecule (yellow: high density, blue: low density). The number of cells I is increased from (A–D) (256, 484, 1,024, 2,025), while the number of cells II remains fixed to 3,000. Cell death reduces the overall number of agents. The pictures show the final state of the simulation after reaching (up to statistical fluctuations) a steady-state. The variations in cell number alone lead to different emerging patterns. While these results may be obtainable by a modified purely PDE-based approach, they are much easier to interpret and develop in an ABM. The simulations were carried out using PhysiCell [2].
    </figcaption>
</div>

<br>
<a>[2] Ghaffarizadeh A, Heiland R, Friedman SH, Mumenthaler SM, PhysiCell MP. PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems. PLOS Comput Biol (2018) 14:e1005991. <a href="doi:10.1371/journal.pcbi.1005991">doi:10.1371/journal.pcbi.1005991</a></a>

<script defer src="https://cdn.rawgit.com/larsgw/citation.js/archive/citation.js/citation-0.4.0-9.min.js" type="text/javascript" integrity="sha384-kJjxdvLlabsAGkfvB39DUjWTIQluK9B53cCYlkLRtAyuhmmC0wgPP3uio4mI2IvS" crossorigin="anonymous"></script>
<script>
    const Cite = require('citation-js')
</script>
