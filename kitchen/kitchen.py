import sys
import time
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
  

from helpers import print_slow

def kitchen():
    print_slow("Wow this kitchen is a mess!",0.05)
    print_slow("Pirates need to learn how to organize!\n",0.05)
    
    time.sleep(1)
    print_slow("*looks around*",0.2)
    time.sleep(1)

    print_slow("\nHmmmm... I see a chef taking a nap area over there.",0.05)
    print_slow("Maybe if I bring the chef all of the ingredients, they'll make me a sandwich.",0.05)


    print_slow("Where should I look for ingredeints?",0.05)

kitchen()