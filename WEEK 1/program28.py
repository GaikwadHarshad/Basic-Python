""" Write a Python program to clear the screen or terminal. """

import time, os

# import call for calling external command
from subprocess import call

# call ls command to list
call(["ls", "-l"])

# screen will hold for 3 seconds
time.sleep(3)

# clear the terminal
os.system('clear')
