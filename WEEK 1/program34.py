"""  Write a Python program to retrieve file properties. """

import os.path
import time
__file__ = "abc.txt"

# get filesystem path to current file
print("File name : ", __file__)
# accessing file
print("Accessing file : ", time.ctime(os.path.getatime(__file__)))
# get modified date of file
print("Modified date: ", time.ctime(os.path.getmtime(__file__)))
# get date of file creation
print("Created on : ", time.ctime(os.path.getctime(__file__)))
# get size of current file
print("Size of file is : ", os.path.getsize(__file__))
