# Useful functions

## Files and directories

### List all files in a folder, including subfolders
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



### Move or copy files between folders
import os, shutil, pathlib, fnmatch

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

def copy_dir(src: str, dst: str, pattern: str = '*'):
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.copy(os.path.join(src, f), os.path.join(dst, f))



### Check if internet is on
from urllib import request

def internet_on():
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
    


### Roman numerals from Arabic numerals
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



### Year to century
def century(year):
    '''
    Returns the century of a year.
    
        Parameters:
            year (int): Year.
            
        Returns:
            century (int): Century of the year.
    '''
    return (year) // 100 + 1 



### Get coordinates for a place
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")

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

    # print(coordinates("Hong Kong"))



### Generate geo-coordinates from location in a df
import pandas as pd
import numpy as np

def generate_coordinates(df):
    '''
    Returns a dataframe with latitude and longitude columns generated from the location column.
    
        Parameters:
            df (pandas dataframe): Dataframe with a location column.
            
        Returns:
            df (pandas dataframe): Dataframe with latitude and longitude columns generated from the location column.
    '''
    for index, row in df.iterrows():
        if pd.isna(row['lat']) and pd.isna(row['lon']):
            if pd.notna(row['location']):
                location = geolocator.geocode(str(row['location']))
                df.at[index, 'lat'] = location.latitude
                df.at[index, 'lon'] = location.longitude
            else:
                df.at[index, 'lat'] = np.nan
                df.at[index, 'lon'] = np.nan
    return df



### Generate coordinates based on centroid of native regions
import geopandas as gpd

def generate_centroid_coordinates(df):
    # Load the geographic data (shapefile or GeoJSON) # https://github.com/tdwg/wgsrpd
    gdf = gpd.read_file("data\\resources\\geo\\level3.geojson")
    for index, row in df.iterrows():
        if pd.isna(row['lat']) and pd.isna(row['lon']):
            if pd.notna(row['native_regions']):
                # Split native regions into a list
                native_distribution = row['native_regions'].split(', ')
                # Filter data for native distribution from gdf dataframe's LEVEL3_NAM column
                native_data = gdf[gdf['LEVEL3_NAM'].isin(native_distribution)].copy() 
                # Calculate centroid data
                native_centroid = native_data.to_crs('+proj=cea').centroid.to_crs(native_data.crs)
                df.at[index, 'lat'] = native_centroid.y.iloc[0]
                df.at[index, 'lon'] = native_centroid.x.iloc[0]
            else:
                df.at[index, 'lat'] = 0
                df.at[index, 'lon'] = 0
    return df



## Images and colors

### Hex to RGBA
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



### Make thumbnails from images that don't already have one
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



## Language and linguistics

### Convert Chinese Text to Simplified if needed
import opencc
t2s = opencc.OpenCC('t2s.json')
s2t = opencc.OpenCC('s2t.json')
# print(t2s.convert('錫蘭肉桂'), s2t.convert('锡兰肉桂'))

### Transcribe Chinese into pinyin or jyutping
import pinyin
import jyutping
py = pinyin.get('錫蘭肉桂')
jp = jyutping.get('錫蘭肉桂')
print(py)
print(' '.join(jp))



## Wordnet

import nltk
from nltk.corpus import wordnet as wn
# nltk.download("wordnet")
# nltk.download("omw-1.4")
# nltk.download("extended_omw") # if you want the wiktionary data

# Wordnets using the Open Multilingual WordNet (https://omwn.org/omw1.html) # 100%: cmn, fin, hrv
# wn_langs = ['als', 'arb', 'bul', 'cat', 'cmn', 'dan', 'ell', 'eng', 'eus', 'fin', 'fra', 'glg', 'heb', 'hrv', 'ind', 'isl', 'ita', 'ita_iwn', 'jpn', 'lit', 'nld', 'nno', 'nob', 'pol', 'por', 'slv', 'spa', 'swe', 'tha', 'zsm'] # 100%: cmn, fin, hrv

wn_langs = ['fra'] # 'eng', 'arb', 'cmn', 
print(wn.synset('allspice.n.03').definition())
print(wn.synsets('allspice', pos='n'))
print(wn.synset('allspice.n.03').lemma_names('ita'))

### WordNet definitions
def wn_definition(df):
    '''
    Returns a dataframe with Wordnet definitions of the words in the wn column.

        Parameters:
            df (pandas dataframe): Dataframe with a wn column.

        Returns:
            df (pandas dataframe): Dataframe with Wordnet definitions of the words in the wn column.
    '''
    for index, row in df.iterrows():
        if pd.notna(row['wn']):
            wn_definition = str(wn.synset(row['wn']).definition())
            df.at[index, "wn_definition"] = str(wn_definition)
    return df



### WordNet translations
def wn_translate(df, lan):
    '''
    Returns a dataframe with Wordnet translations of the words in the wn column.

        Parameters:
            df (pandas dataframe): Dataframe with a wn column.
            lan (str): Language code of the language to translate to.

        Returns:
            df (pandas dataframe): Dataframe with Wordnet translations of the words in the wn column.
    '''
    for index, row in df.iterrows():
        if pd.notna(row['wn']):
            translated_list = wn.synset(row['wn']).lemma_names(lan)
            translated = ", ".join(str(x) for x in translated_list)
            translated = re.sub("_", " ", translated)
            df.at[index, f"wn_translation_{lan}"] = translated
    return df



### Translator
from googletrans import Translator
translator = Translator()
def translate(input, language):
    '''
    Returns a translation of a word or phrase into a language.
    
            Parameters:
                input (str): Word or phrase to translate.
                language (str): Language code of the language to translate to.
    
            Returns:
                translated (str): Translation of the word or phrase into the language.
        '''
    translated = translator.translate(input, dest=language)
    return translated.text

   

#### Translate with DeepL, using Google Translate
# https://developers.google.com/admin-sdk/directory/v1/languages
# dl_languages = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

dl_languages = {'french': 'fr'} # 'hungarian': 'hu', 'english': 'en', 'arabic': 'ar', 'chinese': 'zh-TW',
dl_language_list = list(dl_languages.values())

from deep_translator import GoogleTranslator as dl
# translated = dl(source='en', target='hu').translate("allspice") # api_key=openai
# print(translated)

def dl_translate(df, lang):
    '''
    Returns a dataframe with DeepL translations of the words in the English column.

        Parameters:
            df (pandas dataframe): Dataframe with an English column.
            lang (str): Language code of the language to translate to.

        Returns:
            df (pandas dataframe): Dataframe with DeepL translations of the words in the English column.
    '''    
    for index, row in df.iterrows():
        if pd.notna(row['English']):
            translated = dl(source='en', target=lang).translate(row['English'])
            df.at[index, f"dl_translation_{lang}"] = translated
    return df



##################
# Regex cheatsheet

# (?!) - negative lookahead
# (?=) - positive lookahead
# (?<=) - positive lookbehind
# (?<!) - negative lookbehind

# (?>) - atomic group