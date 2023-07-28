+++
# Title of the page
title = "Example"
# Tags
tags = ["tag"]
# Categories
categories = ["category"]
# Page weight
weight = 10
# Date
date = "2023-07-01T00:00:00+08:00"
# Draft
draft = "false"

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
menuPre = "<i class='fas fa-pepper-hot'></i> "
# The title of the page in menu will be postfixed by this HTML content
menuPost = ""
# Hide a menu entry by setting this to true
hidden = false
# Display name of this page modifier. If set, it will be displayed in the footer.
LastModifierDisplayName = ""
# Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
LastModifierEmail = ""
+++

Lorem Ipsum.

Lorem ipsum dolor sit amet, graecis denique ei vel, at duo primis mandamus.

---

Et legere ocurreret pri, animal tacimates complectitur ad cum. Cu eum inermis inimicus efficiendi. Labore officiis his ex, soluta officiis concludaturque ei qui, vide sensibus vim ad.

# h1 Heading

## h2 Heading

### h3 Heading

#### h4 Heading

##### h5 Heading

###### h6 Heading

I am rendered with **bold text**

I am rendered with _italicized text_

~~Strike through this text~~

Double quotes `"` and single quotes `'` of enclosed text are replaced by **"double curly quotes"** and **'single curly quotes'**.

Double dashes `--` and triple dashes `---` are replaced by en-dash **--** and em-dash **---** entities.

Double arrows pointing left `<<` or right `>>` are replaced by arrow **<<** and **>>** entities.

Three consecutive dots `...` are replaced by an ellipsis **...** entity.

- Lorem ipsum dolor sit amet
- Consectetur adipiscing elit
  - Vestibulum laoreet porttitor sem
  - Ac tristique libero volutpat at
- Nulla volutpat aliquam velit
  - Phasellus iaculis neque
  - Purus sodales ultricies
- Faucibus porta lacus fringilla vel

1. Lorem ipsum dolor sit amet
3. Consectetur adipiscing elit
    1. Integer molestie lorem at massa
    7. Facilisis in pretium nisl aliquet
99. Nulla volutpat aliquam velit
    1. Faucibus porta lacus fringilla vel
    1. Aenean sit amet erat nunc
17. Eget porttitor lorem

- [x] Basic Test
- [ ] More Tests
  - [x] View
  - [x] Hear
  - [ ] Smell

Apple
: Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
: An American computer company.

Orange
: The fruit of an evergreen tree of the genus Citrus.

  You can make juice out of it.
: A telecommunication company.

  You can't make juice out of it.

In this example, `<div></div>` is marked as code.

Be impressed by my advanced code:

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code

```js
grunt.initConfig({
  assemble: {
    options: {
      assets: 'docs/assets',
      data: 'src/data/*.{json,yml}',
      helpers: 'src/custom-helpers.js',
      partials: ['src/partials/**/*.{hbs,md}']
    },
    pages: {
      options: {
        layout: 'default.hbs'
      },
      files: {
        './': ['src/templates/pages/index.hbs']
      }
    }
  }
};
```

| Option | Description |
|--------|-------------|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

| Option | Number | Description |
|-------:|:------:|:------------|
| data   | 1      | path to data files to supply the data that will be passed into templates. |
| engine | 2      | engine to be used for processing templates. Handlebars is the default. |
| ext    | 3      | extension to be used for dest files. |

> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue. Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi.
>
> > Sed adipiscing elit vitae augue consectetur a gravida nunc vehicula. Donec auctor odio non est accumsan facilisis. Aliquam id turpis in dolor tincidunt mollis ac eu diam.
>
> Mauris sit amet ligula egestas, feugiat metus tincidunt, luctus libero. Donec congue finibus tempor. Vestibulum aliquet sollicitudin erat, ut aliquet purus posuere luctus.

This is a link to https://example.com. 

[Assemble](http://assemble.io)


[Example][somelinkID]

[somelinkID]: https://example.com "Go to example domain"

That's some text with a footnote[^1]

[^1]: And that's the footnote.

That's some more text with a footnote.[^someid]

[^someid]:
    Anything of interest goes here.

    Blue light glows blue.

![Spock](https://octodex.github.com/images/spocktocat.png)

![Picard](https://octodex.github.com/images/jean-luc-picat.jpg "Jean Luc Picard")


![La Forge][laforge]

[laforge]: https://octodex.github.com/images/trekkie.jpg "Geordi La Forge"


![Minion](https://octodex.github.com/images/minion.png?height=50px)


![Spidertocat](https://octodex.github.com/images/spidertocat.png?classes=shadow)


![Spidertocat](https://octodex.github.com/images/spidertocat.png?classes=inline)
![DrOctocat](https://octodex.github.com/images/droctocat.png?classes=inline)
![Supertocat](https://octodex.github.com/images/okal-eltocat.jpg?classes=inline)
![Riddlocat](https://octodex.github.com/images/riddlocat.jpg?classes=inline)

![X-tocat](https://octodex.github.com/images/xtocat.jpg?classes=shadow,border,left)


![Homercat](https://octodex.github.com/images/homercat.png?lightbox=false)