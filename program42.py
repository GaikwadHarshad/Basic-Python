""" Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system """


# struct module pack and unpack data to/from c representation
import struct

# getting pointer size and display mode of os executing
print(struct.calcsize("P")*8)
