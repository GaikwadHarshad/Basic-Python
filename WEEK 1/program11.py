"""  Write a Python program to check whether a file exists.  """

from os import path
# it will return boolean value True if file exist and False if does not exist
print("File Exist : "+str(path.exists('abc.txt')))
print("File Exist : "+str(path.exists('raw.txt')))
print("File Exist : "+str(path.exists('text.txt')))
