""" Write a Python program to sort files by date. """

# import glob for pathname pattern matching expansion
import glob
import os
files = glob.glob("*.txt")
# sort file by their modification date
files.sort(key=os.path.getmtime)
# display files on console
print("\n".join(files))
