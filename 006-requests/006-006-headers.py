# https://stackskills.com/courses/102831/lectures/1499463

import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longurl": "https://example.com/"}
headers = {"Content-Type": "application.json"}
r = requests.post(url, json=payload, headers=headers)

print(r.headers)