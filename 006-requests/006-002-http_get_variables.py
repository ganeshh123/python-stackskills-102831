# https://stackskills.com/courses/102831/lectures/1499459

import requests

params = {"q": "pizza"}
r = requests.get("http://bing.com/search")
print("Status", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)