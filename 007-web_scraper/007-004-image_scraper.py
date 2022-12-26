# https://stackskills.com/courses/102831/lectures/1499456

import os
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("Search for:")
params = {"q": search}
r = requests.get("https://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
images = soup.findAll("img", {"class": "mimg"})

if not os.path.exists('./scraped_images/'):
    os.makedirs('./scraped_images/')

count = 1
for image in images:
    if image.has_attr("src"):
        img_obj = requests.get(image.attrs["src"])
    elif image.has_attr("data-src"):
        img_obj = requests.get(image.attrs["data-src"])
    else:
        continue
    # title = image.attrs["src"].split("/")[-1]
    title = search + str(count)
    img = Image.open(BytesIO(img_obj.content))
    img.save("./scraped_images/" + title + ".jpg")
    count = count + 1