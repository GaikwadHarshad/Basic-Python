"""  Write a Python program to get the last part of a string before a specified character.
    https://www.w3resource.com/python-exercises
    https://www.w3resource.com/python """

from myprograms.Utility import UtilityDS


class String8:
    # perform operation on string
    def get_last_part(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Get String Result""\n""2.Exit")
            try:
                choice = int(input("Enter choice :"))
                # validate choice
                ch = UtilityDS.validate_num(choice)
                if ch:
                    if choice == 1:
                        # get last part of string before specified char
                        UtilityDS.last_part_string()

                    elif choice == 2:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String8_object = String8()
String8_object.get_last_part()
