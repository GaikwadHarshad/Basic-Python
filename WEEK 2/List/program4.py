""" Write a Python program to count the number of strings where the string length is 2 or more
    and the first and last character are same from a given list of strings.
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2 """

from myprograms.Utility import UtilityDS


class List4:
    create = []

    # function to perform operations on string list
    def string_char(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2. Get Result ""\n""3.Exit")
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
                            self.create = UtilityDS.create_list_all(element)
                            print("List is created : ", self.create)
                    elif choice == 2:
                        # if list is empty
                        if len(self.create) == 0:
                            print("List is empty..create list first.")
                        # if list in not empty then display smallest element
                        else:
                            # getting string which 1st char and last char is same
                            result = UtilityDS.count_string_char(self.create)
                            print("Number of string whose FirstChar and LastChar are same : ", result)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List4_object = List4()
List4_object.string_char()
