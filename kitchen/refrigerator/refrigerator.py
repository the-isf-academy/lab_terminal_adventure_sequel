import sys
import time
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)
  

from helpers import print_slow

def cabinet():
    print_slow("brrrrrrrrr",0.05)
    print_slow("Wow! Tons of supplies in here.",0.05)
    # print_slow("I see a few different kinds of bread...\n",0.05)

    # os.system('cp ./../../.assets/bread.jpeg .')
    # os.system('cp ./../../.assets/roll.jpeg .')
    # os.system('cp ./../../.assets/pineapple_bun.png .')

    print("What kind of sandwich do I want?")
    print("The Captain said I can open files with, open <filename>")
    print("Once I pick a few items, I better bring them to the chef!")



cabinet()