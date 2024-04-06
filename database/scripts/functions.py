'''
This file contains a collection of useful functions in Python.
Gabor Parti, 2024
'''
################################################################
from urllib import request

# Check if there is an internet connection
def internet_is_on():
    '''
    Returns True if internet is on, False if not.

        Parameters:
            None

        Returns:
            Boolean: True if internet is on, False if not.
    '''
    try:
        request.urlopen('https://github.com', timeout=1)
        return True
    except request.URLError as err: 
        return False


################################################################
# List all files in a folder, including subfolders
def list_files(dir):
    '''
    Returns a list of all files in a folder, including subfolders.

        Parameters:
            dir (str): Path to the folder.

        Returns:
            r (list): List of all files in the folder, including subfolders.
    '''                                                                   
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(os.path.join(subdir, file))                                                                         
    return r


################################################################
import os, shutil, pathlib, fnmatch

# Move files between folders
def move_dir(src: str, dst: str, pattern: str = '*'):
    '''
    Moves files from one folder to another.

        Parameters:
            src (str): Path to the source folder.
            dst (str): Path to the destination folder.
            pattern (str): Pattern to match files to move.

        Returns:
            None
    '''
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.move(os.path.join(src, f), os.path.join(dst, f))



################################################################
# Copy files between folders
def copy_dir(src: str, dst: str, pattern: str = '*'):
    '''
    Copies files from one folder to another.
    
        Parameters:
            src (str): Path to the source folder.
            dst (str): Path to the destination folder.
            pattern (str): Pattern to match files to copy.
            
        Returns:
            None
    '''
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.copy(os.path.join(src, f), os.path.join(dst, f))



################################################################
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")

# Get coordinates for a place
def coordinates(place):
    '''
    Returns the latitude and longitude of a place.
    
        Parameters:
            place (str): Name of the place.

        Returns:
            lat (float): Latitude of the place.
            lon (float): Longitude of the place.
    '''
    location = geolocator.geocode(place)
    lat, lon = location.latitude, location.longitude
    return lat, lon



################################################################
import pandas as pd
import time
# Generate geo-coordinates from location in a df
def generate_coordinates(df):
    '''
    Returns a dataframe with latitude and longitude columns generated from the location column.
    
        Parameters:
            df (pandas dataframe): Dataframe with a location column.
            
        Returns:
            df (pandas dataframe): Dataframe with latitude and longitude columns generated from the location column.
    '''
    for index, row in df.iterrows():
        time.sleep(0.5)
        if pd.isna(row['lat']) and pd.isna(row['lon']):
            if pd.notna(row['location']):
                location = geolocator.geocode(str(row['location']))
                df.at[index, 'lat'] = location.latitude
                df.at[index, 'lon'] = location.longitude
            else:
                df.at[index, 'lat'] = np.nan
                df.at[index, 'lon'] = np.nan
    return df



################################################################
import geopandas as gpd
# Generate coordinates based on centroid of native regions
def centroid_coordinates(df):
    # Load the geographic data (shapefile or GeoJSON) # https://github.com/tdwg/wgsrpd
    gdf = gpd.read_file("data\\resources\\geo\\level3.geojson")
    for index, row in df.iterrows():
        print("Calculating coordinates of", row['item'])
        if pd.notna(row['native']):
            if pd.isna(row['lat']) and pd.isna(row['lon']): #
                # Split native regions into a list
                native_distribution = row['native'].split(', ')
                # Filter data for native distribution from gdf dataframe's LEVEL3_NAM column
                native_data = gdf[gdf['LEVEL3_NAM'].isin(native_distribution)].copy() 
                # Calculate centroid data
                native_centroid = native_data.to_crs('+proj=cea').centroid.to_crs(native_data.crs)
                df.at[index, 'lat'] = native_centroid.y.iloc[0]
                df.at[index, 'lon'] = native_centroid.x.iloc[0]
                time.sleep(1)
        else:
            df.at[index, 'lat'] = np.nan
            df.at[index, 'lon'] = np.nan
    return df


################################################################
# Year to century
def century(year):
    '''
    Returns the century of a year.
    
        Parameters:
            year (int): Year.
            
        Returns:
            century (int): Century of the year.
    '''
    return (year) // 100 + 1 



################################################################
# Roman numerals from Arabic numerals
def roman(num: int) -> str:
    '''
    Returns a string of the Roman numeral representation of an integer.
    
        Parameters:
            num (int): Integer.
            
        Returns:
            roman (str): Roman numeral representation of the integer.
    '''

    chlist = "VXLCDM"
    rev = [int(ch) for ch in reversed(str(num))]
    chlist = ["I"] + [chlist[i % len(chlist)] + "\u0304" * (i // len(chlist))
                    for i in range(0, len(rev) * 2)]
    def period(p: int, ten: str, five: str, one: str) -> str:
        if p == 9:
            return one + ten
        elif p >= 5:
            return five + one * (p - 5)
        elif p == 4:
            return one + five
        else:
            return one * p
    return "".join(reversed([period(rev[i], chlist[i * 2 + 2], chlist[i * 2 + 1], chlist[i * 2]) for i in range(0, len(rev))]))



### Colors and images #########################################

###############################################################
# Hex to RGBA
from PIL import ImageColor as ic

def hex_to_rgba(hex):
    '''
    Returns the RGBA value of a hex color.
    
        Parameters:
            hex (str): Hex color.
            
        Returns:
            rgba (str): RGBA value of the hex color.
    '''
    rgb = str(ic.getrgb(hex))
    rgba = re.sub('\)', ', 1.0)', rgb)
    return rgba



###############################################################
# Make thumbnails from images that don't already have one
from PIL import Image
import re

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



# ### Language and linguistics ##################################

# ###############################################################
# # Convert Chinese Text to Simplified or Traditional Chinese
# import opencc
# t2s = opencc.OpenCC('t2s.json')
# s2t = opencc.OpenCC('s2t.json')
# # print(t2s.convert('錫蘭肉桂'), s2t.convert('锡兰肉桂'))



# ###############################################################
# # Transcribe Chinese into pinyin or jyutping
# import pinyin
# import jyutping
# py = pinyin.get('錫蘭肉桂')
# jp = jyutping.get('錫蘭肉桂')
# print(py)
# print(' '.join(jp))



################################################################
# # # Convert PDFs
# # from pdf2image import convert_from_path

# # def convert_pdf_to_png(file):
# #     name = str(file)
# #     name = re.sub(".*(?=/)", "", name)
# #     name = re.sub("\..*", "", name)
# #     pages = convert_from_path(file, 0)
# #     for page in pages:
# #         page.save(path + name + ".png", 'PNG')



################################################################
# Regex cheatsheet

# (?!) - negative lookahead
# (?=) - positive lookahead
# (?<=) - positive lookbehind
# (?<!) - negative lookbehind

# (?>) - atomic group



################################################################
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

# Others
polyu='#8f1329'
polyu_complimenter = '#138f79'
midnight_blue='#006795'