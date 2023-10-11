# Colour palette file

# Transparency from black
transparent = "rgba(0,0,0,0)"
three_quarters_transparent = 'rgba(0,0,0,0.75)'
half_transparent = 'rgba(0,0,0,0.5)'
quarter_transparent = 'rgba(0,0,0,0.25)'
tenth_transparent = 'rgba(0,0,0,0.1)'

# Transparency from white
transparent_white = "rgba(255,255,255,0)"
three_quarters_transparent_white = 'rgba(255,255,255,0.75)'
half_transparent_white = 'rgba(255,255,255,0.5)'
quarter_transparent_white = 'rgba(255,255,255,0.25)'
tenth_transparent_white = 'rgba(255,255,255,0.1)'

# Colors

# Plotly color schemes (https://plotly.com/python/discrete-color/; https://plotly.com/python/builtin-colorscales/)
# print(px.colors.qualitative.Prism)
# prism = px.colors.qualitative.Prism

# Prism colors in hex code (without gray)
prism = ['#5f4690', '#1d6996', '#38a6a5', '#0f8554', '#73af48', '#edae08', '#e17909', '#cc503e', '#94346e', '#6f4070']

# New colour of a lighter shade based on the above prism color scheme
prism_light = ['#a28aba', '#6baed6', '#8dd3d7', '#7fbf7b', '#b2cf6b', '#fddc69', '#fdae61', '#f4a582', '#d17e9a', '#c994c7', ]

# New colour of a darker shade based on the above prism color scheme
prism_dark = ['#3f2b5b', '#0b4f6c', '#1f7872', '#0b4228', '#4f6228', '#9c6d00', '#984806', '#803d24', '#66234f', '#4f2a6b']

# Combine the above three lists into one
prism = prism + prism_light + prism_dark

# Color names
purple = '#5f4690'
blue = '#1d6996'
turquoise = '#38a6a5'
green = '#0f8554'
lime = '#73af48'
yellow = '#edad08'
orange = '#e17c05'
red = '#cc503e'
magenta = '#94346e'
fuchsia = '#6f4070'
gray = '#666666'
black = '#000000'

# Nord colour scheme (https://www.nordtheme.com/docs/colors-and-palettes) © 2016-2023 Arctic Ice Studio & Sven Greb
# Polar Night
nord0 = "#2e3440"
nord1 = "#3b4252"
nord2 = "#434c5e"
nord3 = "#4c566a"

# Snow Storm
nord4 = "#d8dee9"
nord5 = "#e5e9f0"
nord6 = "#eceff4"

# Frost
nord7 = "#8fbcbb"
nord8 = "#88c0d0"
nord9 = "#81a1c1"
nord10 = "#5e81ac"

# Aurora
nord11 = "#bf616a"
nord12 = "#d08770"
nord13 = "#ebcb8b"
nord14 = "#a3be8c"
nord15 = "#b48ead"

# Dark jungle
dark_jungle0 = "#282828"  # Dark charcoal
dark_jungle1 = "#303030"  # Slightly lighter charcoal
dark_jungle2 = "#383838"  # Even lighter charcoal
dark_jungle3 = "#404040"  # Lighter charcoal

dark_jungle4 = "#7e8a97"  # Light gray
dark_jungle5 = "#8f979f"  # Slightly darker light gray
dark_jungle6 = "#9ea7b0"  # Even darker light gray

dark_jungle7 = "#355c47"  # Dark green
dark_jungle8 = "#2f5440"  # Slightly darker green
dark_jungle9 = "#294a39"  # Even darker green
dark_jungle10 = "#1f3a28"  # Dark forest green

dark_jungle11 = "#753037"  # Dark red
dark_jungle12 = "#82523e"  # Slightly lighter dark red
dark_jungle13 = "#8f5c34"  # Even lighter dark red
dark_jungle14 = "#5e493b"  # Dark brown
dark_jungle15 = "#684f55"  # Dark purple

dark_jungle16 = "#425a73"  # Dark blue
dark_jungle17 = "#3b4f64"  # Slightly lighter dark blue
dark_jungle18 = "#34475d"  # Even lighter dark blue
dark_jungle19 = "#2c3a4e"  # Dark navy blue
dark_jungle20 = "#594770"  # Dark violet

# Others
polyu='#8f1329'
polyu_complimenter = '#138f79'
midnight_blue='#006795'

# relearn
primary = '#73af48'
secondary = '#73af48'
accent = '#489caf'

main_text = '#e0e0e0'
main_link_hover = '#8dd759'
main_bg = '#202020'
main_titles_text = '#ffffff'

code_block = '#f8f8f2'
code_block_bg = '#2b2b2b'

code_inline = '#489caf'
code_inline_bg = '#2d2d2d'
code_inline_border = '#464646'
