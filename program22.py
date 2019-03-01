""" Write a Python program to get the command-line arguments
    (name of the script, the number of arguments, arguments) passed to a script. """

import sys
print("Name of the script : ", sys.argv[0])
print("Number of arguments : ", len(sys.argv))

# returns string which is representation of given object
print("Arguments list : ", str(sys.argv))
