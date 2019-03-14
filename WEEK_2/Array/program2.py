""" Write a Python program to reverse the order of the items in the array """

# array module to get array functions
from array import array


class Reverse:
    group_arr = array('i', [2, 6, 8, 3, 5])

    def reverse_array(self):
        print("The original array :" + str(self.group_arr))
        # reversing array items
        self.group_arr.reverse()
        print("Reverse array: " + str(self.group_arr))


Reverse_instance = Reverse()
Reverse_instance.reverse_array()
