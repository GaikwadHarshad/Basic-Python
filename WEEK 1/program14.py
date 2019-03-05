""" Write a Python program to list all files in a directory in Python. """

import os
import fnmatch
# os.listdir() will return all directories
listOfFile = os.listdir('.')
pattern = "*.py"
for entry in listOfFile:
    # fnmatch() will test whether filename matches string pattern or not, return True or False
    if fnmatch.fnmatch(entry, pattern):
        print(entry)

