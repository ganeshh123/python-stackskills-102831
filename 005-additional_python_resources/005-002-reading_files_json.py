# https://stackskills.com/courses/102831/lectures/1499465

import simplejson as json
import os

file_name = "./ages.json"

if os.path.isfile(file_name) and os.stat(file_name).st_size != 0:
    old_file = open(file_name, "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open(file_name, "w+")
    data = {"name": "Ganesh", "age": 21}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
