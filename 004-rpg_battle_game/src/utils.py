import os

def cls():
    pass
    os.system("clear")

def input_number(label, min=0, max=9999999):
    while True:
        try:
            inp = input(label)
            if inp == 'quit':
                exit(0)
            choice = int(inp)
            if choice >= min and choice <= max:
                return choice
            print('Please choose a number between', min, 'and', max + '.')
        except ValueError:
            print('Please enter an integer.')
