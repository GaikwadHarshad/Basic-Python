"""  Write a Python program to get the number of occurrences of a specified element in an array. """

# import all function from array module

from myprograms.Utility import UtilityDS

while True:
    try:
        print("1: Get occurrences of element""\n""2: Exit""\n")
        choice = int(input("\n""Enter you choice : "))
        # validate choice number
        ch = UtilityDS.validate_num(choice)
        if ch:
            if choice == 2:
                exit()
            elif choice == 1:
                # get number of occurrence of specific element
                print("Number of occurrence of specified element is :", UtilityDS.get_occurrence())
            else:
                print("Invalid choice")
        else:
            print("Enter number only")
    except Exception as e:
        print(e)
