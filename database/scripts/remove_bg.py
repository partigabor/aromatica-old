from rembg import remove
from PIL import Image

import easygui as eg
# input_path = eg.fileopenbox(title='Select image file')
# output_path = eg.filesavebox(title='Save file to..')

filename = "achiote"
input = Image.open(f"database/scripts/{filename}.png")
output = remove(input)
output.save(f"database/scripts/{filename}_nobg.png")