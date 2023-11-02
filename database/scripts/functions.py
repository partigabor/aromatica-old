# Useful functions

# Make thumbnails from images for those that don't already have one
import re
from PIL import Image

def create_thumbnail(file):
    '''
    Returns a thumbnail of an image unless there is already a thumbnail present (searches for "-thumb" in the filename) and saves it to the same location.    

            Parameters:
                    file (str): Path to the image file.

            Returns:
                    image (PIL Image): Thumbnail of the image (500x500).
    '''
    
    # If filename does not contain "-thumb", then create a thumbnail
    if not re.search("-thumb", file):
        # Extract extension from photo path, and keep it in a variable
        ext = re.sub(".*(?=\.)", "", file)
        # Remove the extension from the photo path by finding the last dot and removing everything after it
        filename = re.sub("\.[^.]+$", "", file) 
        # Open the image, create and save a thumbnail, change resolutions if needed
        image = Image.open(f'{filename}{ext}')
        image.thumbnail((500,500))
        image.save(f'{filename}-thumb{ext}')
        return image