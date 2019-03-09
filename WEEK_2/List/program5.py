""" Write a Python program to get a list, sorted in increasing order by the last element in each tuple
    from a given list of non-empty tuples.
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] """


from myprograms.Utility import UtilityDS


class List4:
    create = []

    # function to perform operations on list
    def string_char(self):
        while 1:
            print("---------------------------------------------------")
            print("1.View List""\n""2.Get Sorted Result ""\n""3.Exit")
            try:
                choice = int(input("Enter any choice :"))
                # validating choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # create list
                    if choice == 1:
                        self.create = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
                        print("List is : ", self.create)

                    elif choice == 2:

                        # if list is empty
                        if len(self.create) == 0:
                            print("List is empty..create list first.")
                        # if list in not empty then display smallest element
                        else:
                            # getting string which 1st char and last char is same
                            result = UtilityDS.print_sort_list(self.create)
                            print("List in increasing order by LastName in each tuple  : ", result)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter number for choice")

            except Exception as e:
                print(e)


# instantiation of class
List4_object = List4()
List4_object.string_char()
