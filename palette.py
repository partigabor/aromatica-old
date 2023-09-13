# Colour palette file

# General
transparent = "rgba(0,0,0,0)"
three_quarters_transparent = 'rgba(0,0,0,0.75)'
half_transparent = 'rgba(0,0,0,0.5)'
quarter_transparent = 'rgba(0,0,0,0.25)'
tenth_transparent = 'rgba(0,0,0,0.1)'

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



# Nord colour scheme (https://www.nordtheme.com/docs/colors-and-palettes).

# Polar Night
nord0 = "#2e3440"
nord1 = "#3b4252"
nord2 = "#434c5e"

# Snow Storm
nord3 = "#4c566a"
nord4 = "#d8dee9"
nord5 = "#e5e9f0"

# Frost
nord6 = "#eceff4"
nord7 = "#8fbcbb"
nord8 = "#88c0d0"
nord9 = "#81a1c1"

# Aurora
nord10 = "#5e81ac"
nord11 = "#bf616a"
nord12 = "#d08770"
nord13 = "#ebcb8b"
nord14 = "#a3be8c"
nord15 = "#b48ead"



# Others
polyu='#8f1329'
polyu_complimenter = '#138f79'
midnight_blue='#006795'