"""  Write a Python program to get file creation and modification date/times. """
# import os.path, time
import os.path
import time
# get file modification time
print("last modified: ", time.ctime(os.path.getmtime('raw.txt')))
# get file creation time
print("created: ", time.ctime(os.path.getctime('raw.txt')))
