""" Write a Python program to create an array of 5 integers and display the array items.
    Access individual element through indexes.  """

# import all function from array module
from array import *


class ArrayItems:
    def access_array(self, group_arr):
        # accessing element through their indexes
        print(group_arr[0])
        print(group_arr[1])
        print(group_arr[2])
        print(group_arr[3])
        print(group_arr[4])


# created array of 5 integers
group_arr_list = array('i', [5, 3, -6, 2, 7])
# creating object of ArrayItems Class
ArrayItems_obj = ArrayItems()
# function call using object
ArrayItems_obj.access_array(group_arr_list)
