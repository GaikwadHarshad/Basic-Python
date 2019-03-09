""" Write a Python program to get the difference between the two lists """

from myprograms.Utility import UtilityDS


class List12:
    create1 = []
    create2 = []

    # function to perform operations on list
    def difference_list(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2. Calculate difference b/w lists""\n""3.Exit")
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
                            self.create1 = UtilityDS.create_list_all(element)
                            print("List 2 create : ")
                            self.create2 = UtilityDS.create_list_all(element)
                            print("List is created : ", self.create2)
                    elif choice == 2:
                        # if list is empty
                        if len(self.create1) == 0 or len(self.create2) == 0:
                            if len(self.create1) < 1:
                                print("please create list 1")
                            elif len(self.create2) < 1:
                                print("please create list 2")
                            else:
                                print("List are empty..create list first.")
                        # if list in not empty then display list of word longer than Num
                        else:
                            common = UtilityDS.common_member(self.create1, self.create2)
                            print("Common members are : ", common)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List12_object = List12()
List12_object.difference_list()
