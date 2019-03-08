""" Write a Python program to sum all the items in a list. """

from myprograms.Utility import UtilityDS


class List1:
    # function to perform list creation and get sum of list
    def sum_list(self):
        while 1:
            print("1.Create List""\n""2.Sum of list""\n""3.Exit")
            try:
                choice = int(input("Enter any choice :"))
                # validating choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # create list
                    if choice == 1:
                        print("we are creating list ")
                        # number of element to add
                        element = int(input("How many element you want to add: "))
                        # validating the number
                        e = UtilityDS.validate_num(element)
                        if e:
                            # if valid then create list
                            create = UtilityDS.create_list(element)
                            print("List is created : ", create)
                    elif choice == 2:
                        # display sum of the list element
                        sum_list = UtilityDS.sum_list(create)
                        print("Sum of list : ", sum_list)
                    elif choice == 3:
                        # exit from program
                        exit()

            except Exception as e:
                print(e)


List1_object = List1()
List1_object.sum_list()
