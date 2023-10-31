import requests
from bs4 import BeautifulSoup
import os
import lxml

def photo_downloader(item, path):
    url = "https://unsplash.com/s/photos/" + item
    request = requests.get(url,allow_redirects = True)
    data = BeautifulSoup(request.text,'lxml')
    all_image=data.find_all('figure',itemprop="image")
    count = 1
    # # make a dir from path if it doesn't exist yet
    if not os.path.exists(path + item):
        os.makedirs(path + item) 
    for i in all_image:
        url=i.find('a',rel="nofollow")
        if url != None:
            i_url = url['href']
            photo_bytes = requests.get(i_url,allow_redirects=True)
            with open(f'{path}/{item}/{item}-{count}-Unsplash.jpg','wb') as photo:
                photo.write(photo_bytes.content)
                count +=1

    print("Done")

# if __name__ == "__main__":
#     photo_downloader("https://unsplash.com/s/photos/", "saffron")

# Download images from Unsplash to be curated later
dashed_key = "allspice"
photo_downloader(dashed_key, 'unsplash_downloads/')