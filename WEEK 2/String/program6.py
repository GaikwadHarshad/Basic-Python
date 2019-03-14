"""   Write a Python script that takes input from the user and displays that input back in upper and lower cases """

from myprograms.Utility import UtilityDS


class String6:
    str1 = []

    # perform operation on string
    def upper_lower(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Enter string input""\n""2.Get result in UPPER/lower Case.""\n""3.Exit")
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
                            # get string output in UPPER/lower Case
                            output = UtilityDS.upper_lower(self.str1)
                            print("Upper and Lower Case String : ", output)
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String6_object = String6()
String6_object.upper_lower()
