+++
title = "Testing"
author = "Gabor Parti"
date = "2023-08-01T00:00:00+08:00"
description = "Description."
weight = 10
draft = "false"
categories = ['spice']
tags = ['culinary']
# plotly = true
bibFile = "static/files/bibliography.json"

# Table of contents (toc) is enabled by default. Set this parameter to true to disable it.
# Note: Toc is always disabled for chapter pages
disableToc = false
# If set, this will be used for the page's menu entry (instead of the `title` attribute)
menuTitle = ""
# If set, this will explicitly override common rules for the expand state of a page's menu entry
alwaysopen = true
# If set, this will explicitly override common rules for the sorting order of a page's submenu entries
ordersectionsby = "title"
# The title of the page heading will be prefixed by this HTML content
headingPre = ""
# The title of the page heading will be postfixed by this HTML content
headingPost = ""
# The title of the page in menu will be prefixed by this HTML content
menuPre = ""
# The title of the page in menu will be postfixed by this HTML content
menuPost = ""
# Hide a menu entry by setting this to true
hidden = false
# Display name of this page modifier. If set, it will be displayed in the footer.
LastModifierDisplayName = ""
# Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
LastModifierEmail = ""

mermaidInitialize = "{ \"theme\": \"dark\" }"
mermaidZoom = true
+++

Lorem Ipsum.

Box

{{% notice primary "There may be pirates" "skull-crossbones" %}}
It is all about the boxes.
{{% /notice %}}

<!-- {{% attachments sort="asc" /%}} -->

Badge

{{% badge style="primary" title="Version" %}}6.6.6{{% /badge %}}

Button 

{{% button href="https://gohugo.io/" style="primary" %}}Get Hugo{{% /button %}}

{{% expand "Expand me..." %}}Thank you!{{% /expand %}}

    Code

Icons

{{% icon mortar-pestle %}}

{{% include "content/materials/something.md" %}}

{{< mermaid zoom="true" >}}
pie title Spice names by language
    "English" : 120
    "Arabic" : 90
    "Chinese" : 60
{{< /mermaid >}}