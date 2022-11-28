# https://stackskills.com/courses/python-complete/lectures/1499491

def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Nick", "Dan", "Jack", "King", "Smiley")
