""" Write a Python program to add leading zeroes to a string. """

string1 = '123.45'
print("Original String is : ", string1)
# string is fill with leading zero's
string1 = string1.zfill(9)
print("Added leading zero to string : ", string1)
# string is left justified of length 9 with zero's
string1 = string1.ljust(9, '0')
print("Added 10 leading zero's to string: ", string1)
