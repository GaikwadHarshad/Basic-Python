""" Write a Python program to remove the first occurrence of a specified element from an array. """

# getting all functions from array module
from array import *
from myprograms.Utility import UtilityDS
# declare and initialise array
arr_num = array('i', [2, 3, 5, 2, 5, 6])
print("Original array : ", arr_num)

while 1:
    try:
        print("1:Remove Occurrence""\n""2: Exit""\n")
        ch = int(input("Enter choice : "))
        # validate choice
        choice = UtilityDS.validate_num(ch)
        if choice:
            # remove element
            if ch == 1:
                s_element = int(input("Enter element to remove its 1st occurrence : "))
                # validate element to remove from array
                num = UtilityDS.validate_num(s_element)
                if num:
                    # if element present then remove
                    if s_element in arr_num:
                        # removing element from array
                        arr_num.remove(s_element)
                        print("After removing : ", str(arr_num))
                    else:
                        print("Number is not present")
                else:
                    print("Invalid number")
            elif ch == 2:
                # exiting from program
                exit()
            else:
                print("Invalid choice")
        else:
            print("Enter only number")
    except Exception as e:
        print(e)
