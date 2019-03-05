""" Write a Python program to get the size of an object in bytes. """

import sys
object1 = "object_One"
object2 = "object_two"
object3 = "object_three"
str2 = "hello"
print()
# returns the memory size of object
print("The size of "+object1+"  is :", sys.getsizeof(object1))
print("The size of "+object2+" is :", sys.getsizeof(object2))
print("The size of "+object3+" is :", sys.getsizeof(object3))
print("The size of "+str2+" is :", sys.getsizeof(str2))

