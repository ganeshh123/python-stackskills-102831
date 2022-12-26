# https://stackskills.com/courses/102831/lectures/1499457

import os
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

if not os.path.exists('./scraped_images/'):
        os.makedirs('./scraped_images/')

def RunSearch():
    search = input("Search for:")
    params = {"q": search}
    r = requests.get("https://www.bing.com/images/search", params=params)
    dir_name = './scraped_images/' + search.replace(" ", "_").lower() + "/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    print(dir_name)


    soup = BeautifulSoup(r.text, "html.parser")
    images = soup.findAll("img", {"class": "mimg"})

    count = 1
    for image in images:
        try:
            if image.has_attr("src"):
                img_obj = requests.get(image.attrs["src"])
            elif image.has_attr("data-src"):
                img_obj = requests.get(image.attrs["data-src"])
            else:
                continue
            # title = image.attrs["src"].split("/")[-1]
            title = search + str(count)
            img = Image.open(BytesIO(img_obj.content))
            img.save(dir_name + title + ".jpg")
        except:
            print("Couldn't get image")
            print(image)
        count = count + 1
    RunSearch()

RunSearch()
