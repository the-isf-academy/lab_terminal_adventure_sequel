import sys
import time
import os
import shutil


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)
  
from helpers import print_slow, TEXT_SPEED

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
    print_slow("Oof, sorry there.",TEXT_SPEED)
    print_slow("I must've dozed off.\n",TEXT_SPEED)

    time.sleep(1)

    print_slow("Ahh, I see. You're hungry and would like a sandwich!",TEXT_SPEED)
    print_slow("No problem young sea explorer.",TEXT_SPEED)
    print_slow("Go gather sandwich ingredients, put them all in a 'sandwich_maker'",TEXT_SPEED)
    print_slow("Then come back to me and I'll whip it up for you.",TEXT_SPEED)


def check_sandwich_maker():
    global SANDWICH_MAKER

    sub_folders = [name for name in os.listdir(current) if os.path.isdir(os.path.join(current, name))]
    if 'sandwich_maker' in sub_folders:
        SANDWICH_MAKER = True

        with open('.sandwich_maker.txt', 'w') as f:
            f.write('True')

def check_supplies():
    global SUPPLIES
    
    sandwich_maker = current + '/sandwich_maker'

    num_supplies = len([name for name in os.listdir(sandwich_maker) if os.path.isfile(os.path.join(sandwich_maker, name))])
    if num_supplies >= 3:
        SUPPLIES = True
        
        with open('.supplies.txt', 'w') as f:
            f.write('True')



def insufficient_suppplies():
    print_slow("Sorry pal, looks like you're still not prepared.",TEXT_SPEED)
    print_slow("All items gotta be in 'sandwich_maker.",TEXT_SPEED)
    print_slow("And a `sandwich_maker` needs at least 3 items to work.",TEXT_SPEED)


    print_slow("\nHmmmmm......",.03)

    print_slow("\nI vaguely remember the Captain saying: ",TEXT_SPEED)
    print_slow("  - mkdir can make a sandwich maker",TEXT_SPEED)
    print_slow("  - to move items us 'mv' ",TEXT_SPEED)

def sandwich():
    shutil.rmtree('sandwich_maker') 

    print_slow("*chop chop chop*",0.1)
    print_slow("Here ya go, pal!",TEXT_SPEED)
    print_slow("Bon Apetit!",TEXT_SPEED)
    os.system('cp ./../../.assets/sandwich.jpeg .')

    print_slow("Take a look at your sandwich!",TEXT_SPEED)

def already_eaten():
    print_slow("you just ate!",TEXT_SPEED)
    print_slow("go check in with the Captain.",TEXT_SPEED)



if AWAKE == 'False':
    chef_awakens()

    with open('.awake.txt', 'w') as f:
        f.write('True')

else:
    check_sandwich_maker()
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







