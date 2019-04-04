""" Write a Python program to extract single key-value pair of a dictionary in variables. """

# dictionary of one element
dict1 = {'Name': 'harsh'}

# getting key-value pair in variables k,v
(k, v), = dict1.items()

# display variables
print(k, "-->", v)
