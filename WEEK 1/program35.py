""" Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. """

number_list = [44, 75, 21, 65, 135, 34, 91, 78]
# uses anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), number_list))
# display result
print("Numbers divisible by 15 are : ", result)
