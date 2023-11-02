+++
title = "About"
# menuTitle = "About"
author = "Gabor Parti"
date = "2023-08-01T00:00:00+08:00"
description = "Description."
weight = 2
categories = ['test']
tags = ['test']
draft = false
hidden = false
plotly = true
# mermaidZoom = true
bibFile = "static/files/bibliography.json"
disableComments = false
+++

### The Name

*Aromatica* is the singular feminine or plural neuter nominative form of *arōmāticus* (a, um, adj.), meaning "composed of spice, aromatic, fragrant" {{< cite lewis_latin_1879 >}} [{{% icon book-open %}}](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0059:entry=aromaticus), cf. Ancient Greek ἀρωματικός *arōmatikós* (adj.) 'aromatic', and the etymon ἄρωμα *árōma* (n.) "aromatic herb or spice" {{< cite liddell_greekenglish_1940 >}} [{{% icon book-open %}}](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Da%29%2Frwma1).

The term therefore refers to any substance of fragrance, focusing on spices, but also includes incense, medicinal herbs, aromatic woods, oils and perfume, and other exotica[^1] with special olfactory and gustatory qualities.

[^1]: objects considered interesting because they are out of the ordinary, especially because they originated in a distant foreign country

### The Logo

{{< svg "static/images/svgs/borobudur-green.svg" >}}

The logo of Aromatica depicts the [Borobodur ship](https://en.wikipedia.org/wiki/Borobudur_ship), an 8th to 9th-century wooden double outrigger Javanese ship carved on the wall of the Borobodur temple (ꦧꦫꦧꦸꦝꦸꦂ). The ship is depicted as a symbol of the maritime trade routes across the Indian Ocean region, which connected the ancient world and allowed the spread of spices and other aromatics.

## The Data

In what follows, you can find the main resources that were used while building the database, and the rationale behind the selections.

### A Master List of All Spices?

The first step was to create a list of spices that are relatively well-known, using information gathered by professionals from various fields. The second step was to collate the data on these materials, and morph it into a unified database to faciliate further enquiries. In the later stages of researching specific items, new and less common substances would reveal themselves, and their addition will help to reach the ultimate goal of a comprehensive list of spices.

Encyclopedias can be a great starting point to kick off research in any topic, and the *Encyclopaedia Britannica* does have a non-exhaustive list of herbs and spices assembled by Melissa Petruzzello {{< cite -petruzzello_list_2023 >}}. I consider three academic fields crucial for research into the spice domain: *botany*, *history*, and *gastronomy*. Regarding the realm of plants, I relied on the book of South African botanist Ben-Erik van Wyk {{< cite -vanwyk_culinary_2014 >}}. For a cultural and historical account, I turned towards the book of English historian and linguist Andrew Dalby {{< cite -dalby_dangerous_2000 >}}. Finally, for a perspective from the culinary arts I used the book of Tony Hill {{< cite -hill_contemporary_2004 >}}, a spice merchant from Seattle.

**Table 1.** The main resources used for the spice list, and the number of items found in each.

|Source | Discipline | Number of items |
| --- | --- | --- |
| Petruzzello {{< cite -petruzzello_list_2023 >}} | Reference | 70 |
| Hill {{< cite -hill_contemporary_2004 >}} | Gastronomy | 127 |
| Dalby {{< cite -dalby_dangerous_2000 >}} | History | 183 |
| van Wyk {{< cite -vanwyk_culinary_2014 >}} | Botany | 667 |

{{< gallery dir="/images/books/" />}}

The main challenge of combining different spice datasets is that the basis of comparison is not always straightforward. Depending on scientific discipline, sources identify spices either by the binomial name of the species, common names, or even some general culinary/medicinal functions and uses. Binomial names are the safe way to go when we talk about the plants, but differentiating certain spices that might or might not be of the same flora can be challenging, not to mention trying to navigate historical data. Common names are almost always problematic, since many spices have many distinct names and name variations in different times, and they are often confused &ndash; especially so in multilingual settings. Moreover, the information complied by experts of a certain scientific field is vastly different in nature, focusing on botany, chemistry, history, economics, gastronomy, etc. The problematics of spice identification is due to the fact that different disciplines focus on different aspects of these fascinating subjects of study: the magnifying glass of the botanist, the zeal of the historian, and the needs of the chefs are all enormously diverse perspectives.

### External datasets

#### Plant names backbone and maps

Plant distribution and habitat data is taken from [Plants of the World Online (POWO)](https://powo.science.kew.org/) , which uses the [World Checklist of Vascular Plants (WCVP)](https://wcvp.science.kew.org/) dataset hosted and maintained by the Royal Botanic Gardens at Kew. Geographical codes, names, and polygon data comes from the level 3 [dataset](https://github.com/tdwg/wgsrpd) ("botanical countries") of the [*World Geographical Scheme for Recording Plant Distributions* (2nd ed.)](https://web.archive.org/web/20160125135239/http:/www.nhm.ac.uk/hosted_sites/tdwg/TDWG_geo2.pdf) of the *International Working Group on Taxonomic Databases For Plant Sciences* (TDWG).

Linguistic and geographic data on languages are from Glottolog and WALS...

## Technical details

### Typeface and Fonts

This website uses [Noto](https://en.wikipedia.org/wiki/Noto_fonts) fonts commissioned by Google and created by Monotype. Noto ([no tofu](https://www.youtube.com/watch?v=16_NYHUZ1kM)) is a typeface (font family) that covers most scripts and writing systems of the world. They are hosted on [Google Fonts](https://fonts.google.com), open source and free to use.

### Maps and Plots

The interactive visualizations were made by the Plotly graphing library using Python.

### Website

The website was built using the Hugo framework, a static website generator, and a modified version of the Hugo Relearn theme.

# Bibliography

{{< bibliography cited >}}