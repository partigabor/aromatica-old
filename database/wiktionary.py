import os
import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup



# Variables
key = 'pepper'
path = 'database\\data\\wiktionary\\'

# Check if the directory exists, if not, create it
if not os.path.exists(path):
    os.makedirs(path)

# Define the URL
url = f"https://en.wiktionary.org/wiki/{key}"

# Get the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Define the list of ids
senses = ['Translations-spice']

# Create a list of tuples containing the language, translation, sense, and level
translations = []
for id in senses:
    # Get the translations for the specific noun sense
    translations_div = soup.find('div', {'id': id})

    if translations_div is not None:
        for li in translations_div.find_all('li'):
            split_text = li.get_text().split(":", 1)
            lang = split_text[0]
            trans = split_text[1].split('\n')[0] if len(split_text) > 1 else ''
            sense = id.split('-')[1]  # Extract the sense from the id
            level = 'main'  # This row is not from a level
            translations.append((lang, trans, sense, level))

            # Check if there are sub-items (dl and dd tags)
            dl = li.find('dl')
            if dl is not None:
                for dd in dl.find_all('dd'):
                    # Extract language and translation from the dd tag
                    split_text = dd.get_text().split(":", 1)
                    lang = split_text[0]
                    trans = split_text[1].split('\n')[0] if len(split_text) > 1 else ''
                    level = 'sub'  # This row is from a level
                    translations.append((lang, trans, sense, level))

# Create a DataFrame from the list of tuples
df = pd.DataFrame(translations, columns=['language', 'item', 'sense', 'level'])

# # Replace "" with NaN
# df['item'] = df['item'].replace('', pd.NA)

# # Use backfill for NA in items
# df['item'] = df['item'].fillna(method='bfill')

# Define a function to split on commas not inside parentheses
def split_not_in_parentheses(s):
    return re.split(r',\s*(?![^()]*\))', s)

# Apply the function to the 'item' column
df['item'] = df['item'].apply(split_not_in_parentheses)

# Explode the 'item' column
df = df.explode('item')

# Drop duplicates (keep first with spice sense)
df = df.drop_duplicates(subset = ['language', 'item'], keep = 'first').reset_index(drop = True)

# Cleaning
df['item'] = [re.sub('\xa0', " ", str(x)) for x in df['item']]
df['item'] = [re.sub(r' m ', " ", str(x)) for x in df['item']]
df['item'] = [re.sub(r' f ', " ", str(x)) for x in df['item']]
df['item'] = [re.sub(r' n ', " ", str(x)) for x in df['item']]
df['item'] = [re.sub(r' c ', " ", str(x)) for x in df['item']]
df['item'] = [re.sub(r' pl ', " ", str(x)) for x in df['item']]
df['item'] = [re.sub(r' m,', ",", str(x)) for x in df['item']]
df['item'] = [re.sub(r' f,', ",", str(x)) for x in df['item']]
df['item'] = [re.sub(r' n,', ",", str(x)) for x in df['item']]
df['item'] = [re.sub(r' c,', ",", str(x)) for x in df['item']]
df['item'] = [re.sub(r' pl,', ",", str(x)) for x in df['item']]
df['item'] = [re.sub(r' m$', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r' f$', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r' n$', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r' c$', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r' pl$', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\(bcl\)', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\(nds\)', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\(scn\)', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\(ast\)', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\(Föhr-Amrum\)', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\s?\(\w\w\)', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\(please verify\)', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\s+', " ", str(x)) for x in df['item']]
df['item'] = [re.sub(r' ,', ",", str(x)) for x in df['item']]
df['item'] = [re.sub(r'^\s', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\s$', "", str(x)) for x in df['item']]

# Other
df['item'] = [re.sub(r"\(taraškievica\)", "", str(x)) for x in df['item']]
df['item'] = [re.sub(r"\(collective\)", "", str(x)) for x in df['item']]
df['item'] = [re.sub(r"class 9/10", "", str(x)) for x in df['item']]

# Change ( and ) to * and * 
df['item'] = [re.sub(r'\(', "*", str(x)) for x in df['item']]
df['item'] = [re.sub(r'\)', "*", str(x)) for x in df['item']]

# Remove ⁧ and ⁩ from item
df['item'] = [re.sub(r'⁧', "", str(x)) for x in df['item']]
df['item'] = [re.sub(r'⁩', "", str(x)) for x in df['item']]

# drop NA
df = df[df.item != "please add this translation if you can"]

# If there is a star in the item column, split the column into 'script' and 'transliteration' columns
df['term'] = df['item'].apply(lambda x: x.split('*')[0].strip())
df['transliteration'] = df['item'].apply(lambda x: x.split('*')[1].strip() if len(x.split('*')) > 1 else None)

# CLean '' in the sense column
df['sense'] = [re.sub(r"''", "", str(x)) for x in df['sense']]

# Reorder by alphabetizing the language column
# df = df.sort_values('language').reset_index(drop=True)

# Create source
df['source'] = 'Wiktionary'
df['group'] = ''

# reorder
df = df[['language', 'term', 'transliteration', 'item', 'group', 'sense', 'source']]

# Save the DataFrame to file
df.to_excel(path + f'{key}_gen.xlsx', sheet_name='wiktionary', index=None)

# Print
df