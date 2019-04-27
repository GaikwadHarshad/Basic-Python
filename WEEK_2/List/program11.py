""" Write a Python program to generate all permutations of a list in Python. """

from myprograms.Utility import UtilityDS


class List11:
    create = []
    k = 0

    # function to perform operations on list
    def specified_list(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Generate permutations of list ""\n""2.Exit")
            try:
                choice = int(input("Enter any choice :"))
                # validating choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # generate permutation of list
                    if choice == 1:
                        li = [1, 2, 3]
                        print("List is : ", li)
                        UtilityDS.perm(li)
                    elif choice == 2:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List11_object = List11()
List11_object.specified_list()
