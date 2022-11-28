# https://stackskills.com/courses/python-complete/lectures/1499489

def print_something(name, age):
    print("My name is", name, "and my age is", age)

print_something("Ganesh", 22)

def print_something_2(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)

print_something_2()
print_something_2("Ganesh")