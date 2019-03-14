""" Write a Python program to empty a variable without destroying it.
    Sample data: n=20
    d = {"x":200}
    Expected Output : 0
    {} """

n = 20
# dictionary with 1 element
d = {"x": 200}
# list of elements
var = [2, 4, 5]
# tuple of elements
tuple_name = ('s', 't', 'r')
# get type of variable used and empty variable
print(type(n)())
print(type(d)())
print(type(var)())
print(type(tuple_name)())


