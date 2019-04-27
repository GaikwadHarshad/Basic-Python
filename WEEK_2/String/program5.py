"""  Write a Python function that takes a list of words and returns the length of the longest one. """

from myprograms.Utility import UtilityDS


class String5:
    str1 = []

    # perform operation on string
    def long_word(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Create List of String""\n""2.Length of longest word.""\n""3.Exit")
            try:
                choice = int(input("Enter choice :"))
                # validate choice
                ch = UtilityDS.validate_num(choice)
                if ch:
                    if choice == 1:
                        print("we are creating list : ")
                        # number of element to add
                        element = int(input("How many element you want to add: "))
                        # validating the number
                        e = UtilityDS.validate_num(element)
                        if e:
                            # if valid then create list
                            self.str1 = UtilityDS.create_list_all(element)
                            print("List is created : ", self.str1)
                    elif choice == 2:
                        if self.str1.__len__() < 1:
                            print("Enter string first")
                        else:
                            # getting longest word from given list of string
                            longest = UtilityDS.get_long_word(self.str1)
                            print("Longest word in list of string is : ", longest)
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String5_object = String5()
String5_object.long_word()
