""" Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
    Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Expected Output : ['Green', 'White', 'Black']  """

from myprograms.Utility import UtilityDS


class List10:
    create = []

    # function to perform operations on list
    def specified_list(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2. Get specified list ""\n""3.Exit")
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
                            self.create = UtilityDS.create_list_all(element)
                            print("List  is created : ", self.create)
                    elif choice == 2:
                        # remove element from list at specified position
                        rem = UtilityDS.specified_element_rm(self.create)
                        print("Removed element at position 0th 4th 4th")
                        print("After removing : ", rem)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List10_object = List10()
List10_object.specified_list()
