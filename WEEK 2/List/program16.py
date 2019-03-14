"""  Write a Python program to split a list based on first character of word. """

from myprograms.Utility import UtilityDS


class List16:
    create = []

    # function to perform operations on list
    def split_list(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2. split list ""\n""3.Exit")
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
                            print("List is created : ", self.create)
                    elif choice == 2:
                        # if list is empty
                        if len(self.create) == 0:
                            print("List is empty..create list first.")
                        # if list in not empty then perform split
                        else:
                            UtilityDS.split_word(self.create)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List16_object = List16()
List16_object.split_list()
