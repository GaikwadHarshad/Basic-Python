""" Write a Python program to lowercase first n characters in a string.  """

from myprograms.Utility import UtilityDS


class String12:
    str1 = ''

    # perform operation on string
    def lower_case(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Enter string ""\n""2.String with lowercase of n char""\n""3.Exit")
            try:
                choice = int(input("Enter choice :"))
                # validate choice
                ch = UtilityDS.validate_num(choice)
                if ch:
                    if choice == 1:
                        # create string
                        self.str1 = input("Enter string in Upper Case Only : ")
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
                            print("String is : ", self.str1)
                            n = int(input("Enter N length to get lowercase letter :"))
                            # validate N length number
                            num = UtilityDS.validate_num(n)
                            if num:
                                # get string with lowercase letter of n char
                                output = UtilityDS.get_lowercase(self.str1, n)
                                print("Letter with lowercase of 1st N char : ", output)
                            else:
                                print("please enter number only")
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String12_object = String12()
String12_object.lower_case()
