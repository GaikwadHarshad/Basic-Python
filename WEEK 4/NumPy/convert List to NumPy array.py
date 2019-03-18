""" Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
    Expected Output:
    Original List: [12.23, 13.32, 100, 36.32]
    One-dimensional numpy array: [ 12.23 13.32 100. 36.32]  """

# importing numpy for performing mathematical operation on arrays
import numpy as np
# list of element
List = [12.23, 13.32, 100, 36.32]
print("Original List is : ", List)
# function to convert list into NumPy array
arr = np.array(List)
print("1D NumPy array : ", arr)
