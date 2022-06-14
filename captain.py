import os

complete_file = open("kitchen/chef/.complete.txt", "r")

complete = complete_file.read()

FILES = [
    '.awake.txt',
    '.sandwhich_maker.txt',
    '.supplies.txt',
    '.complete.txt'
]

def welcome():
    name = input("Enter your name: ")
    os.system('cls' if os.name == 'nt' else 'clear')


    print("Ahoy, {}! Welcome back! ".format(name))
    print("You just escaped death back there!")
    print("That sea monster was vicious.")
    print("Speaking of which, you must be starving after all that treasure hunting.")
    print("Why don't you take a look in the kitchen and see what you can come up with.")
    print("Come back when you're fed!")

def end():
    print('end')

def reset():
    os.rmdir('kitchen/chef/sandwhich_maker')
    os.remove('kitchen/chef/sandwhich.jpeg')

    for file in FILES:
        path = 'kitchen/chef/'
        with open(path+file, 'w') as f:
                f.write('False')

        f.close()
   


if complete == 'False':
    welcome()
else:
    reset()
    end()

