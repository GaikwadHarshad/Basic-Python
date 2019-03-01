""" Write a Python program to print out a set containing all the colors from color_list_1
    which are not present in color_list_2.
    Test Data :
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    Expected Output :
    {'Black', 'White'} """


color_list_1 = ["Red", "White", "Green", "Blue"]
color_list_2 = ["White", "Yellow", "Blue", "Black"]
Final_list = []

for i in color_list_1:
        if i not in color_list_2:
            # if color not present in another list then add it to final list
            Final_list.append(i)


print(Final_list)
