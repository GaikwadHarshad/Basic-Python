""" Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
    If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
     given string is less than 3, leave it unchanged.
    Sample String : 'abc'
    Expected Result : 'abcing'
    Sample String : 'string'
    Expected Result : 'stringly"""

from myprograms.Utility import UtilityDS


class String3:
    str1 = ''

    # perform operation on string
    def char_replace(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Enter String""\n""2.String operation ing/ly at end""\n""3.Exit")
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
                            string = UtilityDS.string_suffix(self.str1)
                            print("String after operation perform : ", string)
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
