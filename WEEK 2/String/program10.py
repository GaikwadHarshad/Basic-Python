""" Write a Python program to count occurrences of a substring in a string.  """

from myprograms.Utility import UtilityDS


class String10:

    # perform operation on string
    def count_substring(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Enter substring input""\n""2.Get count of substring""\n""3.Exit")
            try:
                choice = int(input("Enter choice :"))
                # validate choice
                ch = UtilityDS.validate_num(choice)
                if ch:
                    if choice == 1:
                        # getting substring
                        sub_str = input("which sub string you want to count : ")
                        print("substring is : ", sub_str)
                    elif choice == 2:
                        # get count of substring in string
                        output = UtilityDS.count_substring(sub_str)
                        print("Count of substring : ", output)
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String10_object = String10()
String10_object.count_substring()
