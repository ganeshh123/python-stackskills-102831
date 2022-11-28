# https://stackskills.com/courses/102831/lectures/1499495

import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)

# Remove capital letters
new = re.sub('[A-Z]', '', string)
print(new)

# Remove small letters
new2 = re.sub('[a-z]', '', string)
print(new2)

# Remove full stop, comma, single quotes
new3 = re.sub('[.,\']', '', string)
print(new3)

# Remove full stop, comma, single quotes, small letters, capital letters
new4 = re.sub('[.,\'a-zA-Z]', '', string)
print(new4)

# Remove full stop, comma, single quotes, capital letters
new5 = re.sub('[.,\'A-Z]', '', string)
print(new5)

# Remove full stop, comma, single quotes, capital letters, spaces
new6 = re.sub('[.,\'A-Z+" "]', '', string)
print(new6)

string = string + "6 298 - 345"
print(string)

# Remove everything except numbers
new7 = re.sub('[^0-9]', '', string)
print(new7)
