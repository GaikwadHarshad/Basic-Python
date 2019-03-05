""" Write a Python program which accepts a sequence of comma-separated numbers from user and
    generate a list and a tuple with those numbers.
    Sample data : 3, 5, 7, 23
    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23') """

# accept number from user
numbers = input("Enter the values/numbers : ")

# generate list by split function
list1 = numbers.split(",")
# generate tuple on list
tuple1 = tuple(list1)
print("List is :", list1)
print("Tuple is :", tuple1)
