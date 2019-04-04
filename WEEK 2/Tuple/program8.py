""" Write a Python program to remove an item from a tuple. """

from myprograms.Utility import UtilityDS


class Tuple8:
    tuple1 = (2, 9, 5, 6, 3, 7)

    # operation to remove element from tuple
    def remove(self):
        print("Tuple : ", self.tuple1)
        while True:
            try:
                print("1. Remove Item""\n""2. View Tuple""\n""3.Exit")
                choice = int(input("Enter your choice : "))
                # validate choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # choice to remove item
                    if choice == 1:
                        item = int(input("Enter items to be remove : "))
                        rm = UtilityDS.remove_tuple(self.tuple1, item)
                        print("After removing item : ", rm)
                    # choice to display tuple element
                    elif choice == 2:
                        print("Tuple : ", self.tuple1)
                    # exiting from program
                    elif choice == 3:
                        print("Exiting...")
                        exit()
                    else:
                        print("Invalid choice""\n")
                else:
                    print("Enter only number""\n")
            except Exception as e:
                # raise and print exception
                print(e)


# instance creation
Tuple8_obj = Tuple8()
Tuple8_obj.remove()
