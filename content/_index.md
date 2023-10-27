+++
archetype = "home"
title = ""
date = "2023-08-01T00:00:00+08:00"
author = "Gabor Parti"
bibFile = "static/files/bibliography.json"
+++

# Welcome to Aromatica

*Aromatica* is a database containing historical, cultural, and linguistic information on spices, herbs, incense, and other aromatics, aiming to gather the whole spectrum of these unique materials. The website currently contains information on 24 items.

>The database is under construction, please come back in 2024.


{{< load-plotly >}}

{{< plotly json="/aromatica/plotly/home.json" height="600" >}}

<!-- ### Background -->

### On the Name

*Aromatica* is the singular feminine or plural neuter nominative form of *arōmāticus* (a, um, adj.), meaning "composed of spice, aromatic, fragrant" {{< cite lewis_latin_1879 >}} [{{% icon book-open %}}](https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0059:entry=aromaticus), cf. Ancient Greek ἀρωματικός *arōmatikós* (adj.) 'aromatic', and the etymon ἄρωμα *árōma* (n.) "aromatic herb or spice" {{< cite liddell_greekenglish_1940 >}} [{{% icon book-open %}}](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Da%29%2Frwma1).

The term therefore refers to any substance of fragrance, focusing on spices, but also includes incense, medicinal herbs, oils and perfume, aromatic woods, and other exotica[^1] with special olfactory and gustatory qualities. 

[^1]: objects considered interesting because they are out of the ordinary, especially because they originated in a distant foreign country

<!-- Definition -->
<!-- 
### Credits

#### Data

[Plants of the World Online (POWO)](https://powo.science.kew.org/)

World Checklist of Vascular Plants (WCVP)

TDWG

#### Logo

The logo of Aromatica depicts the [Borobodur ship](https://en.wikipedia.org/wiki/Borobudur_ship), an 8th to 9th-century wooden double outrigger Javanese ship carved on the wall of the ꦧꦫꦧꦸꦝꦸꦂ Borobodur temple. The ship is depicted as a symbol of the maritime trade routes of the Indian Ocean, which connected the ancient world and allowed the spread of spices and other aromatics.

#### Fonts

This website uses the [Noto](https://www.youtube.com/watch?v=16_NYHUZ1kM) Sans font commissioned by Google. Privacy: The website hosts these fonts locally, and does not send or receive requests to Google's servers. -->

***

### Versioning \& Update history

<!-- {{% badge style="accent" title="Version" %}}0.1.0{{% /badge %}} &ensp;(2024-06-01) &ensp; [beta] initial development release -->

{{% badge style="accent" icon="angle-double-up" title="Version" %}}0.0.4{{% /badge %}} &ensp; 2023-10-24 &ensp; [alpha] &ensp; added [gallery](https://github.com/liwenyip/hugo-easy-gallery) and [cite](https://github.com/loup-brun/hugo-cite) features, finalized logo

{{% badge color="#404040" icon="angle-double-up" title="Version" %}}0.0.3{{% /badge %}} &ensp; 2023-10-21 &ensp; [alpha] &ensp; implemented [Noto](https://www.monotype.com/resources/case-studies/more-than-800-languages-in-a-single-typeface-creating-noto-for-google) typeface for non-Latin fonts; 

{{% badge color="#404040" icon="angle-double-up" title="Version" %}}0.0.2{{% /badge %}} &ensp; 2023-10-20 &ensp; [alpha] &ensp; finalized [theme](https://mcshelby.github.io/hugo-theme-relearn/index.html) and functionality; added placeholder content

{{% badge color="#404040" style="primary" icon="angle-double-up" title="Version" %}}0.0.1{{% /badge %}} &ensp; 2023-08-01 &ensp; [alpha] &ensp; website creation; entering development mode

# Bibliography

{{< bibliography cited >}}