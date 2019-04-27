""" Write a Python program to get a string from a given string where all occurrences of
    its first char have been changed to '$', except the first char itself.
    Sample String : 'restart'
    Expected Result : 'resta$t' """

from myprograms.Utility import UtilityDS


class String3:
    str1 = ''

    # perform operation on string
    def char_replace(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Enter String""\n""2.Replace Character except 1st""\n""3.Exit")
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
                            # replace characters with $ except 1st char
                            replace = UtilityDS.replace_char(self.str1)
                            print("Replacement of char with $ : ", replace)
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String3_object = String3()
String3_object.char_replace()
