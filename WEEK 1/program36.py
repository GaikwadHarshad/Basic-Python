"""  Write a Python program to determine if variable is defined or not.  """

# try block
try:
    var1

# except block for handle exception
except NameError:
    print("var1 Variable is undefined")

# else when try block executed unexceptionally
else:
    print(" var1 Variable is defined")


try:
    var2 = 100
# except block for handle exception
except NameError:
    print("var2 Variable is undefined")

# else when try block executed unexceptionally
else:
    print("var2 Variable is defined")
