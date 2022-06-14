import sys
import time
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)
  

from helpers import print_slow

def cabinet():
    print_slow("Ooooooh",0.05)
    print_slow("Lots of random scraps of food lying around in here.",0.05)
    print_slow("I see a few different kinds of bread...\n",0.05)

    os.system('cp ./../../.assets/bread.jpeg .')
    os.system('cp ./../../.assets/roll.jpeg .')
    os.system('cp ./../../.assets/pineapple_bun.png .')

    print("What kind of bread should I choose?")
    print("The Captain said I can open files with, open <filename>")
    print("Once I pick a bread, I better bring it to the chef!")



cabinet()