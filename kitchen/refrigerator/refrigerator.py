import sys
import time
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)
  

from helpers import print_slow

TEXT_SPEED = 0.05

def cabinet():
    print_slow("*brrrrrrrrrrrrrrrrr*",TEXT_SPEED)
    print_slow("\nJackpot!",TEXT_SPEED)
    # print_slow("I see a few different kinds of bread...\n",TEXT_SPEED)

    os.system('cp ./../../.assets/eggs.jpeg .')
    os.system('cp ./../../.assets/meats1.jpeg .')
    os.system('cp ./../../.assets/meats2.jpeg .')
    os.system('cp ./../../.assets/meats3.jpeg .')
    os.system('cp ./../../.assets/lettuce.png .')

    print_slow("What kind of sandwich do I want?",TEXT_SPEED)

    print_slow("\nThe Captain said I can open files with, open <filename>",TEXT_SPEED)
    print_slow("They also said I can move files files with, mv <filename> <location>",TEXT_SPEED)

    print_slow("\nOnce I pick a few items, I better bring them to the chef!",TEXT_SPEED)



cabinet()