# Pexels downloader

# Terminal usage:
# python pexels.py --query "black pepper" --resolution original --sleep 0.1 --path ./pexels_downloads
# python database/scripts/pexels.py --query "saffron"

import argparse
import json
import os
import time

import requests
import tqdm
from pexels_api import API

PEXELS_API_KEY = 'ltytGu4h9mZXbRbAJdUMaMjTUBMLScsWPwNITfSyGItoav3YiHhzOIAy'
MAX_IMAGES_PER_QUERY = 20
RESULTS_PER_PAGE = 10
PAGE_LIMIT = MAX_IMAGES_PER_QUERY / RESULTS_PER_PAGE

def get_sleep(t):
    def sleep():
        time.sleep(t)
    return sleep

def pexels_downloader(args):
    sleep = get_sleep(args.sleep)

    api = API(PEXELS_API_KEY)
    query = args.query

    page = 1
    counter = 0

    photos_dict = {}

    # Step 1: Getting urls and meta information
    while page <= PAGE_LIMIT:
        api.search(query, page=page, results_per_page=RESULTS_PER_PAGE)
        photos = api.get_entries()

        for photo in tqdm.tqdm(photos):
            photos_dict[photo.id] = vars(photo)['_Photo__photo']
            counter += 1

        if not api.has_next_page:
            break

        page += 1
        sleep()

    print(f"Finishing at page: {page}")
    print(f"Images were processed: {counter}")

    # Step 2: Downloading
    if photos_dict:
        os.makedirs(args.path, exist_ok=True)

        # Saving dict
        with open(os.path.join(args.path, f'{query}.json'), 'w') as fout:
            json.dump(photos_dict, fout)

        for val in tqdm.tqdm(photos_dict.values()):
            url = val['src'][args.resolution]
            fname = os.path.basename(val['src']['original'])
            # image_path = os.path.join(args.path, fname)
            image_path = os.path.join(args.path)

            if not os.path.isfile(image_path):  # ignore if already downloaded
                response = requests.get(url, stream=True)

                with open(image_path, 'wb') as outfile:
                    outfile.write(response.content)
            else:
                print(f"File exists: {image_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--path', type=str, default='./pexels_downloads')
    parser.add_argument('--resolution', choices=['original', 'large2x', 'large',
                                                 'medium', 'small', 'portrait',
                                                 'landscape', 'tiny'], default='original')
    parser.add_argument('--sleep', type=float, default=0.1)
    args = parser.parse_args()
    pexels_downloader(args)
    
# ########

# import argparse

# # Define the arguments as a dictionary
# args = {
#     'query': key,
#     'path': f"./output/photos/{key}",
#     'resolution': "original",
#     'sleep': 0.1
# }

# # Create an ArgumentParser and set the arguments
# parser = argparse.ArgumentParser()
# parser.add_argument('--query', type=str, required=True)
# parser.add_argument('--path', type=str, default='./pexels_downloads')
# parser.add_argument('--resolution', choices=['original', 'large2x', 'large', 'medium', 'small', 'portrait', 'landscape', 'tiny'], default='original')
# parser.add_argument('--sleep', type=float, default=0.1)

# # Parse the arguments from the dictionary
# namespace = argparse.Namespace(**args)

# pexels_downloader(namespace)