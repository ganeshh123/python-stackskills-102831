# https://stackskills.com/courses/102831/lectures/1499458

import requests

r = requests.get("http://google.com")
print("Status", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)
