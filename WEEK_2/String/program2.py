""" Write a Python program to count the number of characters (character frequency) in a string. """

from myprograms.Utility import UtilityDS


class String2:
    str1 = ''

    # calculate length of string
    def calculate_len(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Enter String""\n""2.Get character frequency""\n""3.Exit")
            try:
                choice = int(input("Enter choice :"))
                # validate choice
                ch = UtilityDS.validate_num(choice)
                if ch:
                    if choice == 1:
                        # create string
                        self.str1 = input("Enter Any string : ")
                        # validate string
                        valid = UtilityDS.validate_string(self.str1)
                        if valid:
                            print()
                        else:
                            print("Enter only string")
                    elif choice == 2:
                        if self.str1.__len__() < 1:
                            print("Enter string first")
                        else:
                            # get length of string
                            frequency = UtilityDS.char_frequency(self.str1)
                            print("Length of string is: ", frequency)
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String2_object = String2()
String2_object.calculate_len()
