""" Write a Python program to concatenate all elements in a list into a string and return it. """


def concatenate_list(list_temp):
    result = ' '
    for i in list_temp:
        # add list of ith element to the result string
        result += str(i)
    return result


# accept list of element
n1 = int(input("Enter list element 1: "))
n2 = int(input("Enter list element 2: "))
n3 = int(input("Enter list element 3: "))
n4 = int(input("Enter list element 4: "))
list1 = [n1, n2, n3, n4]
print("The list element are : ", list1)
# function call and print return string on console
print("List elements return in string is : ", concatenate_list(list1))
