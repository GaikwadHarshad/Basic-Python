""" Write a Python program that accepts a comma separated sequence of words as input
    and prints the unique words in sorted form (alphanumerically).
    Sample Words : red, white, black, red, green, black
    Expected Result : black, green, red, white,red """

from myprograms.Utility import UtilityDS


class String7:

    # perform operation on string
    def sort_unique_word(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Get unique word in sorted manner""\n""2.Exit")
            try:
                choice = int(input("Enter choice :"))
                # validate choice
                ch = UtilityDS.validate_num(choice)
                if ch:
                    if choice == 1:
                        # get word in sorted manner
                        output = UtilityDS.sort_word()
                        print("Unique word in sorted way : ", output)
                    elif choice == 2:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String7_object = String7()
String7_object.sort_unique_word()
