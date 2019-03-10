""" Write a python program to check whether two lists are circularly identical."""

from myprograms.Utility import UtilityDS


class List13:
    create1 = []
    create2 = []
    create3 = []

    # function to perform operations
    def difference_list(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2. Perform circular identical on lists""\n""3.Exit")
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
                            self.create1 = UtilityDS.create_list(element)
                            print("create List 2 ----------- : ")
                            self.create2 = UtilityDS.create_list(element)
                            print("create List 3 ----------- :")
                            self.create3 = UtilityDS.create_list(element)
                            print("List 1 : ", self.create1)
                            print("List 2 : ", self.create2)
                            print("List 3 : ", self.create3)
                    elif choice == 2:
                        # if list is empty
                        if len(self.create1) == 0 or len(self.create2) == 0:
                            if len(self.create1) < 1:
                                print("please create list 1")
                            elif len(self.create2) < 1:
                                print("please create list 2")
                            else:
                                print("List are empty..create list first.")
                        # if list in not empty then display whether lists are circular identical
                        else:
                            compare1 = UtilityDS.circular_identical(self.create1, self.create2)
                            print("Circular identical with List 1 & List 2  : ", compare1)
                            compare2 = UtilityDS.circular_identical(self.create1, self.create3)
                            print("Circular identical with List 1 & List 3  : ", compare2)
                            compare3 = UtilityDS.circular_identical(self.create1, self.create3)
                            print("Circular identical with List 2 & List 3  : ", compare3)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")
            except Exception as e:
                print(e)


# instantiation of class
List13_object = List13()
List13_object.difference_list()
