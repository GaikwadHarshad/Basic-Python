""" Write a Python program to find files and skip directories of a given directory.  """

from os import listdir
from os.path import isfile
from os.path import join

# get list of files from the given directory and skip directories
list_of_files = []
for f in listdir("/home/admin1/PycharmProjects/FunctionalProgram"):
    if isfile(join("/home/admin1/PycharmProjects/FunctionalProgram", f)):
        list_of_files.append(f)
# gets each file from list end display on console
for f in list_of_files:
    print(f)
