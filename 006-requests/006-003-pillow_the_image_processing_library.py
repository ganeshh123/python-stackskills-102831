# https://stackskills.com/courses/102831/lectures/1499460

import requests
from io import BytesIO
from PIL import Image

r = requests.get('http://wallpapercave.com/wp/TuVhQdr.jpg')

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")