import sys
import time

def print_slow(str,seconds):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(seconds)
    sys.stdout.write('\n')
