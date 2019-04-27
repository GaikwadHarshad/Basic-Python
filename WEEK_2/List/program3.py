""" Write a Python program to get the smallest number from a list. """

from myprograms.Utility import UtilityDS


class List3:
    create = []

    # function to perform list creation and get smallest number from list
    def get_small_element(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2.Smallest element from list ""\n""3.Exit")
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
                            self.create = UtilityDS.create_list(element)
                            print("List is created : ", self.create)
                    elif choice == 2:
                        # if list is empty
                        if len(self.create) == 0:
                            print("List is empty..create list first.")
                        # if list in not empty then display smallest element
                        else:
                            # getting smallest element
                            small = UtilityDS.small_element(self.create)
                            print("Smallest element in list : ", small)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List3_object = List3()
List3_object.get_small_element()
