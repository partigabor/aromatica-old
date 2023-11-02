+++
title = "Test"
author = "Gabor Parti"
date = "2023-08-01T00:00:00+08:00"
description = "Description."
weight = 1
categories = []
tags = []
draft = false
hidden = false
plotly = true
# mermaidZoom = true
bibFile = "static/files/bibliography.json"
disableComments = false
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

### Testing other scripts

Amharic: <span class="amharic-text">የአማርኛ ጽሑፍ</span>

Arabic: <span class="arabic-text" dir="rtl">نص بالعربي</span>

Armenian: <span class="armenian-text">Հայերեն տեքստ</span>

Balinese: <span class="balinese-text">ᬧᬲᬃᬦᬃ ᬓᬲᬓᬲ</span>

Bengali: <span class="bengali-text">বাংলা টেক্সট</span>

Burmese: <span class="burmese-text">မြန်မာစာ</span>

Cyrillic: <span class="cyrillic-text">Македонски текст</span>

Cuneiform: <span class="cuneiform-text">𒀭𒆗𒀳𒀭𒁇𒀀𒈾𒀀</span>

Chinese, Simplified: <span class="simplified-chinese-text">简体中文</span>

Chinese, Traditional: <span class="traditional-chinese-text">繁體中文</span>

Devanagari: <span class="devanagari-text">हिन्दी में टेक्स्ट</span>

Ethiopic: <span class="ethiopic-text">የአማርኛ ጽሑፍ</span>

Greek: <span class="greek-text">Ελληνικό κείμενο</span>

Hebrew: <span class="hebrew-text" dir="rtl">טקסט בעברית</span>

Japanese: <span class="japanese-text">日本語のテキスト</span>

Javanese: <span class="javanese-text">ꦥꦿꦚꦠꦤ꧀ꦲꦸꦩꦸꦩ꧀ꦔꦼꦤꦤ</span>

Kawi: <span class="kawi-text">𑼡𑼪𑼒𑽎</span>

Korean: <span class="korean-text">한국어 텍스트</span>

Linear B: <span class="linear-b-text">𐀴𐀪𐀡𐀆𐄀𐁁𐀐𐀄𐄀𐀐𐀩𐀯𐀍𐄀𐀸𐀐 𐃠</span>

Nastaliq: <span class="nastaliq-text" dir="rtl">نستعلیق</span>

Syriac: <span class="syriac-text" dir="rtl">ܠܫܢܐ ܠܫܢܐ</span>

Sundanese: <span class="sundanese-text">ᮘᮞ ᮞᮥᮔ᮪ᮓ ᮞᮥᮔ᮪ᮓ</span>

Tamil: <span class="tamil-text">தமிழ் உரை</span>

Tibetan: <span class="tibetan-text">བོད་སྐད་ཡིག་གཟུགས།</span>

Thai: <span class="thai-text">ข้อความภาษาไทย</span>

<center>Centered text.</center>

>Blockquote

    Code snippet example

`code inline example`

[Example for a link](www.link.com)

### Image

![Saffron](/images/photos/saffron/saffron-0-Vera_De_on_Unsplash.jpg?width=10rem "Saffron")

### Gallery

{{< load-photoswipe >}}

{{< gallery dir="/images/photos/saffron/gallery" hover-effect="slideup" caption-effect="fade" />}}

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

⚓ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae nisi eget nunc ultricies aliquam. Nulla facilisi. Sed euismod, nisl eget ultricies ultricies, nisl nisl aliquam nisl, quis aliquam nisl nisl eget nisl.

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

{{< cite -lewis_latin_1879 >}}

{{< bibliography cited >}}

### SVG

{{< svg "static/images/svgs/borobudur-green.svg" >}}

### Mermaid

{{< mermaid zoom="true" >}}
pie title Spice names by language
    "English" : 120
    "Arabic" : 90
    "Chinese" : 60
{{< /mermaid >}}

### Highlighting

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

### Columns

{{< comments >}}