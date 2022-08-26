import os
from sre_constants import SUCCESS
from helpers import print_slow, TEXT_SPEED

complete_file = open("kitchen/chef/.complete.txt", "r")
COMPLETE = complete_file.read()

welcome_file = open(".welcome.txt", "r")
WELCOME = welcome_file.read()


FILES = [
    '.awake.txt',
    '.sandwich_maker.txt',
    '.supplies.txt',
    '.complete.txt',
]

def welcome():
    print_slow("Ahoy, welcome back! ",TEXT_SPEED)
    print_slow("You just escaped death back there!",TEXT_SPEED)
    print_slow("That sea monster was vicious.",TEXT_SPEED)
    print_slow("Speaking of which, you must be starving after all that treasure hunting.",TEXT_SPEED)
    print_slow("Why don't you go find the Chef in the Kitchen.",TEXT_SPEED)
    print_slow("Come back when you're fed!",TEXT_SPEED)

    with open('.welcome.txt', 'w') as f:
        f.write('True')
        f.close()

def already_welcome():
    print_slow("Why are you still here!",TEXT_SPEED)
    print_slow("I told you to go talk to the Chef.",TEXT_SPEED)
    print_slow("Come back when you're fed!",TEXT_SPEED)
    print_slow("\n--Try using `ls` to explore.--",TEXT_SPEED)


def end():
    print_slow("So, looks like the Chef get you sorted.\n",TEXT_SPEED)
    print_slow("Hope it was to your liking.\n",TEXT_SPEED)
    print_slow("*shrugs*",TEXT_SPEED/2)
    print_slow("\nWell... You're adventure has finally come to end.",TEXT_SPEED)
    print_slow("Time to create your own adventure!",TEXT_SPEED)

def reset():
    os.remove('kitchen/chef/sandwich.jpeg')

    for file in FILES:
        path = 'kitchen/chef/'
        with open(path+file, 'w') as f:
                f.write('False')

        f.close()
    with open('.welcome.txt', 'w') as f:
        f.write('False')
        f.close()

if COMPLETE != 'False':
    reset()
    end()
elif WELCOME == 'False':
    welcome()
else:
    already_welcome()
