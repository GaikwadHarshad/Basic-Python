""" Write a Python program to sort three integers without using conditional statements and loops. """

# accept three integers from user
int1 = int(input("Enter integer 1: "))
int2 = int(input("Enter integer 2: "))
int3 = int(input("Enter integer 3: "))
# get minimum of three numbers
low = min(min(int1, int2), int3)
# get maximum of three numbers
high = max(max(int1, int2), int3)
# get middle number
middle = (int1+int2+int3)-low-high
# sorted integers display on console
print("Sorted integer are : ", low, middle, high)

