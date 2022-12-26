import os
import json
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

download_folder = "downloads"

if not os.path.exists("./" + download_folder + "/"):
        os.makedirs("./" + download_folder + "/")

def RunSearch():
    search = input("Search for:")
    params = {"q": search}
    # params = {"q": search, "qft": "+filterui:imagesize-wallpaper"}
    r = requests.get("https://www.bing.com/images/search", params=params)
    print(r.url)
    dir_name = "./" + download_folder + "/" + search.replace(" ", "_").lower() + "/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.findAll("a", {"class": "iusc"})

    for result in results:
        # print(result.prettify())
        if result.has_attr("m"):
            img_data = json.loads(result.attrs["m"])
            try:
                img_obj = requests.get(img_data["murl"])
                title = img_data["desc"]
                img = Image.open(BytesIO(img_obj.content))
                print(img, title, "\n")
                img.save(dir_name + title + ".jpg")
            except:
                print("Couldn't get image: ", img_data["murl"], "\n")
    RunSearch()

RunSearch()
