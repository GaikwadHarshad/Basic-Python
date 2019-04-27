""" Write a Python program to check whether an element exists within a tuple. """

from myprograms.Utility import UtilityDS


class Tuple6:
    # object of UtilityDS
    util = UtilityDS

    def check_existence(self):
        tuple1 = (1, 5, 6, 3, 15, 7)
        while True:
            try:
                print("1. Check Existence of element""\n""2. View tuple""\n""3. Exit")
                choice = int(input("Select Any option :"))
                # validate choice number
                if self.util.validate_num(choice):
                    if choice == 1:
                        element = int(input("Enter any element to check existence : "))
                        # validate element to check existence
                        e = self.util.validate_num(element)
                        if e:
                            # check element for existence in tuple
                            check = self.util.check_existence(tuple1, element)
                            if check:
                                print("Element ", element, "is existed in tuple""\n")
                            else:
                                print("Element is Not exist in tuple")
                                print()
                        else:
                            print("Enter only number")
                    # view tuple element
                    elif choice == 2:
                        print("Tuple elements : ", tuple1)
                    elif choice == 3:
                        # exiting from program
                        print("Exiting...")
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Invalid option")
            except Exception as e:
                    print(e)


Tuple6_object = Tuple6()
Tuple6_object.check_existence()
