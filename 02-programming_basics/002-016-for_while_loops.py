# https://stackskills.com/courses/102831/lectures/1499494

numbers = [1,2,3,4,5]

for item in numbers:
    print(item)

names = ["Name1","Name2", "Name3"]

for n in names:
    print("Name is", n)

run = True
current = 1

while run:
    print(current)
    if current == 100:
        run = False
    else:
        current = current + 1
