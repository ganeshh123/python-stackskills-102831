# https://stackskills.com/courses/102831/lectures/1499496

import re

print("Calculator\n")
print("Type 'quit' to exit")
print("Type 'clear' to clear the result\n")

previous = 0
run = True

def perform_math():
    # Required to make variables accessible inside performMath
    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        # If there's already a result allow the user to type further equations next to it
        equation = input(str(previous) + " ")
    
    if equation == "quit":
        print("\nGoodbye.")
        run = False
    elif equation == "clear":
        print("")
        previous = 0
    else:
        # eval runs input as code so make sure to only keep numbers
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            # If there's already a result, append the new equation to the result before evaluating
            previous = eval(str(previous) + equation)

while run:
    perform_math()
