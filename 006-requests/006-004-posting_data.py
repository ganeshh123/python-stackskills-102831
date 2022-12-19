# https://stackskills.com/courses/102831/lectures/1499461

import requests

my_data = {"name": "Ganesh", "email": "ganesh@email.com"}
r = requests.post('http://www.w3schools.com/php/welcome.php', data=my_data)

print(r.text)