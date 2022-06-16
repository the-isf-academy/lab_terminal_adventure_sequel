import sys
import time
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)
  

from helpers import print_slow, TEXT_SPEED


def cabinet():
    print_slow("Ooooooh",TEXT_SPEED)
    print_slow("Lots of random scraps of food lying around in here.",TEXT_SPEED)
    print_slow("I see a few different kinds of bread...\n",TEXT_SPEED)

    os.system('cp ./../../.assets/bread.jpeg .')
    os.system('cp ./../../.assets/roll.jpeg .')
    os.system('cp ./../../.assets/pineapple_bun.png .')

    print_slow("What kind of bread should I choose?",TEXT_SPEED)
    print_slow("\nThe Captain said I can open files with, open <filename>",TEXT_SPEED)
    print_slow("They also said I can move files files with, mv <filename> <location>",TEXT_SPEED)

    print_slow("\nOnce I pick a bread, I better bring it to the chef!",TEXT_SPEED)



cabinet()