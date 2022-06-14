import sys
import time
import os


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)
  
from helpers import print_slow

awake_file = open(".awake.txt", "r")
sandwich_maker_file = open(".sandwich_maker.txt", "r")
supplies_file = open(".supplies.txt", "r")
complete_file = open(".complete.txt", "r")


AWAKE = awake_file.read()
SANDWICH_MAKER = sandwich_maker_file.read()
SUPPLIES = supplies_file.read()
COMPLETE = complete_file.read()


def chef_awakens():
    print_slow("*pokes chef*",0.02)
    time.sleep(1)

    print_slow("AAAAaaaaaaarrrrggggggggghhhhhhh",0.01)
    print_slow("Oof, sorry there.",0.05)
    print_slow("I must've dozed off.\n",0.05)

    time.sleep(1)

    print("Ahh, I see. You're hungry and would like a sandwich!")
    print("No problem young sea explorer.")
    print("Once you've gathered you're supplies, put them all in a 'sandwich_maker'")
    print("Then come back to me and I'll whip it up for you.")


def check_sandwich_maker():
    sub_folders = [name for name in os.listdir(current) if os.path.isdir(os.path.join(current, name))]
    if 'sandwich_maker' in sub_folders:
        SANDWICH_MAKER = True

        with open('.sandwich_maker.txt', 'w') as f:
            f.write('True')

def check_supplies():
    sandwich_maker = current + '/sandwich_maker'

    num_supplies = len([name for name in os.listdir(sandwich_maker) if os.path.isfile(os.path.join(sandwich_maker, name))])
    if num_supplies >= 3:
        SANDWICH_MAKER = True

        with open('.supplies.txt', 'w') as f:
            f.write('True')

def insufficient_suppplies():
    print("Sorry pal, looks like you're still not prepared.")
    if SANDWICH_MAKER == 'False':
        print("All items gotta be in 'sandwich_maker.")
    if SUPPLIES == 'False':
        print("Looks like you're a bit short on items.")


    print_slow("\nHmmmmm......",.03)

    print("\nI vaguely remember the Captain saying: ")
    print("  - directories are great for sandwich making")
    print("  - to move items us 'mv' ")

def sandwich():
    print_slow("*chop chop chop*",0.1)
    print("Here ya go, pal!")
    print("Bon Apetit!")
    os.system('cp ./../../.assets/sandwich.jpeg .')

    print("Take a look at your sandwich!")

def already_eaten():
    print("you just ate!")
    print("go check in with the Captain.")



if AWAKE == 'False':
    chef_awakens()

    with open('.awake.txt', 'w') as f:
        f.write('True')

else:
    check_sandwich_maker()

    if SANDWICH_MAKER != 'False' and SUPPLIES == 'False':
        check_supplies()

    if SANDWICH_MAKER == 'False' or SUPPLIES == 'False':
        insufficient_suppplies()
        
    else:
        if COMPLETE == 'False':
            sandwich()
            with open('.complete.txt', 'w') as f:
                f.write('True')
        else:
            already_eaten()







