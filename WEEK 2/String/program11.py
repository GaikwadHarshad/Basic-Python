""" Write a Python program to reverse a string """

from myprograms.Utility import UtilityDS


class String11:
    str1 = ''

    # perform operation on string
    def reverse(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Enter string input""\n""2.Get reverse string""\n""3.Exit")
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
                            # get string reverse
                            output = UtilityDS.reverse_string(self.str1)
                            print("Reverse string is : ", output)
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String11_object = String11()
String11_object.reverse()
