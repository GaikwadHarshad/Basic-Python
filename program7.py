""" Write a Python program to check whether a specified value is contained in a group of values.
    Test Data :
     3 -> [1, 5, 8, 3] : True
    -1 -> [1, 5, 8, 3] : False. """


def check_data(group_data, num):
    for i in group_data:
        if num == i:
            return True
    return False


print(check_data([1, 5, 8, 3], 5))
print(check_data([1, 5, 8, 3], -1))



