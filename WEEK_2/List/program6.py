""" Write a Python program to remove duplicates from a list. """

from myprograms.Utility import UtilityDS


class List6:
    create = []

    # function to perform operations on list
    def duplicate(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2. Remove Duplicates ""\n""3.view list""\n""4.Exit")
            try:
                choice = int(input("Enter any choice :"))
                # validating choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # create list
                    if choice == 1:
                        print("we are creating list : ")
                        # number of element to add
                        element = int(input("How many element you want to add: "))
                        # validating the number
                        e = UtilityDS.validate_num(element)
                        if e:
                            # if valid then create list
                            self.create = UtilityDS.create_list(element)
                            print("List is created : ", self.create)
                    elif choice == 2:
                        # if list is empty
                        if len(self.create) == 0:
                            print("List is empty..create list first.")
                        # if list in not empty then display list after removal of duplicate
                        else:
                            remove = UtilityDS.remove_duplicate(self.create)
                            print("After removing duplicate : ", remove)
                    elif choice == 3:
                        # view list
                        print("List is : ", self.create)
                    elif choice == 4:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List6_object = List6()
List6_object.duplicate()
