# Remove background of an image using rembg
# https://github.com/danielgatis/rembg

from rembg import remove
from PIL import Image

filename = "pink_peppercorn"
input_path = f"C:\\Users\\gparti\\Downloads\{filename}.png"
output_path = "C:\\Users\\gparti\\Downloads\\no_bg.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

print("Done!")

##############
# How to iterate over files in a performatic way

# from pathlib import Path
# from rembg import remove, new_session

# session = new_session()

# for file in Path('C:\\Users\\gparti\\Downloads\\remove_bg').glob('*.png'):
#     input_path = str(file)
#     output_path = str(file.parent / (file.stem + ".out.png"))

#     with open(input_path, 'rb') as i:
#         with open(output_path, 'wb') as o:
#             input = i.read()
#             output = remove(input, session=session)
#             o.write(output)