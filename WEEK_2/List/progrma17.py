""" Write a Python program to remove duplicates from a list of lists.
    Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    New List : [[10, 20], [30, 56, 25], [33], [40]] """

from myprograms.Utility import UtilityDS


class List17:
    create = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

    # function to perform operations on list
    def split_list(self):
        while 1:
            print("---------------------------------------------------")
            print("1.split list ""\n""2.Exit")
            try:
                choice = int(input("Enter any choice :"))
                # validating choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # create list
                    if choice == 1:
                        # if list is empty
                        if len(self.create) == 0:
                            print("List is empty..create list first.")
                        # if list in not empty then perform remove duplicate from list of list
                        else:
                            print("original list : ", self.create)
                            item = UtilityDS.list_to_list(self.create)
                            print("Removed duplicates in list of list : ", item)
                    elif choice == 2:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List17_object = List17()
List17_object.split_list()
