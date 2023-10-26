+++
title = "Testing"
author = "Gabor Parti"
date = "2023-08-01T00:00:00+08:00"
description = "Description."
weight = 10
# draft = "false"
categories = ['test']
tags = ['test']
# disableComments = "true"
plotly = "true"
mermaidZoom = true
bibFile = "static/files/bibliography.json"

# # Table of contents (toc) is enabled by default. Set this parameter to true to disable it.
# # Note: Toc is always disabled for chapter pages
# disableToc = false
# # If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle = "Test"
# # If set, this will explicitly override common rules for the expand state of a page's menu entry
# alwaysopen = true
# # If set, this will explicitly override common rules for the sorting order of a page's submenu entries
# ordersectionsby = "title"
# # The title of the page heading will be prefixed by this HTML content
# headingPre = ""
# # The title of the page heading will be postfixed by this HTML content
# headingPost = ""
# # The title of the page in menu will be prefixed by this HTML content
# menuPre = ""
# # The title of the page in menu will be postfixed by this HTML content
# menuPost = ""
# # Hide a menu entry by setting this to true
# hidden = false
# # Display name of this page modifier. If set, it will be displayed in the footer.
# LastModifierDisplayName = ""
# # Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
# LastModifierEmail = ""
+++

## Two

### Three

#### Four

##### Five

###### Six

**Lorem ipsum** *dolor sit amet*, __*consectetur*__ adipiscing elit. Sed vitae nisi eget nunc ultricies aliquam. Nulla facilisi. Sed euismod, nisl eget ultricies ultricies, nisl nisl aliquam nisl, quis aliquam nisl nisl eget nisl. 

This is some mixed text with <span class="arabic-text" dir="rtl">نص بالعربي</span>, <span class="chinese-text">中文文字</span>, <span class="devanagari-text">हिन्दी में टेक्स्ट</span>, and <span class="hebrew-text" dir="rtl">טקסט בעברית</span> mixed inline with English text.

>Blockquote

    Code snippet example

`code inline example`

[Example for a link](www.link.com)

### {{% icon mortar-pestle %}} Icons

{{% icon pepper-hot %}} Spices

{{% icon seedling %}} Herbs

{{% icon fire-alt %}} Incense

{{% icon vial %}} Perfume

### Badges

{{% badge style="primary" title="Version" %}}6.6.6{{% /badge %}}

### Buttons

{{% button href="https://gohugo.io/" style="primary" %}}Get Hugo{{% /button %}}

### Expand

{{% expand "Expand me..." %}}Thank you!{{% /expand %}}

### Attachments

{{% attachments sort="asc" /%}}

### Including other files

{{% include "content/items/manuscripts/allspice_ms.md" %}}

### Boxes

{{% notice primary "There may be pirates" "skull-crossbones" %}}
It is all about the boxes.
{{% /notice %}}

{{% notice accent "There may be corsairs" "skull-crossbones" %}}
But it's all about the boxes.
{{% /notice %}}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae nisi eget nunc ultricies aliquam. Nulla facilisi. Sed euismod, nisl eget ultricies ultricies, nisl nisl aliquam nisl, quis aliquam nisl nisl eget nisl.

***

### Gallery

{{< load-photoswipe >}}

{{< gallery dir="/images/testing/" hover-effect="slideup" caption-effect="fade" />}}

<!-- {{< gallery >}}
  {{< figure src="/images/testing/anatto-1.jpg" >}}
  {{< figure src="/images/testing/anatto-2.jpg" >}}
  {{< figure src="/images/testing/anatto-3.jpg" >}}
{{< /gallery >}} -->

### Plotly

{{< load-plotly >}}

{{< plotly json="/aromatica/plotly/home.json" height="900" >}}

### Hugo Cite

{{< cite lewis_latin_1879 >}}

{{< bibliography cited >}}

### SVG

{{< svg "static/images/svgs/borobudur-green.svg" >}}

<!-- ### Mermaid

{{< mermaid zoom="true" >}}
pie title Spice names by language
    "English" : 120
    "Arabic" : 90
    "Chinese" : 60
{{< /mermaid >}} -->

```python
#!/usr/bin/env python
"""Test file for Python syntax highlighting in editors / IDEs.
Meant to cover a wide range of different types of statements and expressions.
Not necessarily sensical or comprehensive (assume that if one exception is
highlighted that all are, for instance).
Extraneous trailing whitespace can't be tested because of svn pre-commit hook
checks for such things.
"""
# Comment
# OPTIONAL: XXX catch your attention
# TODO(me): next big thing
# FIXME: this does not work

# Statements
from __future__ import with_statement  # Import
from sys import path as thing

print(thing)

assert True  # keyword


def foo():  # function definition
    return []


class Bar(object):  # Class definition
    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

foo()  # UNCOLOURED: function call
while False:  # 'while'
    continue
for x in foo():  # 'for'
    break
with Bar() as stuff:
    pass
if False:
    pass  # 'if'
elif False:
    pass
else:
    pass

# Constants
'single-quote', u'unicode'  # Strings of all kinds; prefixes not highlighted
"double-quote"
"""triple double-quote"""
'''triple single-quote'''
r'raw'
ur'unicode raw'
'escape\n'
'\04'  # octal
'\xFF'  # hex
'\u1111'  # unicode character
1  # Integral
1L
1.0  # Float
.1
1+2j  # Complex

# Expressions
1 and 2 or 3  # Boolean operators
2 < 3  # UNCOLOURED: comparison operators
spam = 42  # UNCOLOURED: assignment
2 + 3  # UNCOLOURED: number operators
[]  # UNCOLOURED: list
{}  # UNCOLOURED: dict
(1,)  # UNCOLOURED: tuple
all  # Built-in functions
GeneratorExit  # Exceptions
```

## Missing

### Tabs

### Columns

# Questions

- How to justify/center multiple inline images?

- Can I re-init my git repo and all previous commits?



{{< comments >}}