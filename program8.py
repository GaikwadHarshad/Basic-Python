""" Write a Python program to create a histogram from a given list of integers """


def histogram(group_data):
    for i in group_data:
        dis = ' '
        num = i
        while num > 0:
            dis += '#'
            num = num - 1
        print(dis)


# accept list of integers
n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
n3 = int(input("Enter number 3:"))
n4 = int(input("Enter number 4:"))
# function call to histogram
histogram([n1, n2, n3, n4])
