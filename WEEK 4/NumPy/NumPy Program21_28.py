import numpy as np
from myprograms.Utility.UtilityDS import validate_num


# class for mathematical/logical operation using NumPy
class NumPyPrograms:
    choice = 0

    def numpy_operations(self):
        # list of program
        print()
        print("21. concatenate two 2-dimensional arrays")
        print("22. make an array immutable (read-only)")
        print("23. create an array of (3, 4) shape, multiply every element value by 3 and display the new array")
        print("24. convert a NumPy array into Python list structure")
        print("25. convert a NumPy array into Python list structure with output as precision 3")
        print("26. suppresses the use of scientific notation for small numbers in numpy array.")
        print("27. program to how to add an extra column to an numpy array")
        print("28.  remove specific elements in a numpy array")
        print("0. Exit")
        print("--------------------------------------------------------------------------------------")
        while True:
            try:
                print()
                # accept choice from user
                self.choice = input("Enter choice : ")
                # validate choice number
                valid_choice = validate_num(self.choice)
                if valid_choice:
                    choice = int(self.choice)
                    if choice == 21:
                        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
                        print("Array 1:")
                        print(arr1)
                        arr2 = np.array([[7, 8, 9], [10, 11, 12]])
                        print("Array 2:")
                        print(arr2)
                        arr3 = np.concatenate((arr1, arr2), axis=1)
                        print("Concatenated array :")
                        print(arr3)
                    elif choice == 22:
                        arr = np.arange(10)
                        # set this to false lack the data and make it read only
                        arr.flags.writeable = False
                        print("Test whether array is read only")
                        # try to change value of immutable array
                        arr[0] = 5
                    elif choice == 23:
                        arr = np.arange(1, 13).reshape(3, 4)
                        print("array of (3, 4) shape:")
                        print(arr)
                        # iterate over array and openflags as read write
                        for x in np.nditer(arr, op_flags=['readwrite']):
                            # each element is multiply with 3
                            # x[...] is 0d so x[:] could not work here
                            x[...] = 3 * x
                        print("multiplied every element value by 3")
                        print(arr)
                    elif choice == 24:
                        arr = np.arange(8).reshape(4, 2)
                        print("original array :""\n", arr)
                        # convert numpy array into python list structure
                        print("List is : ""\n", arr.tolist())
                    elif choice == 25:
                        # These options determine the way floating point numbers,
                        # arrays and other NumPy objects are displayed.
                        np.set_printoptions(precision=3)
                        arr = np.array([0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349, 0.35399976,
                                        0.99469633, 0.0694458, 0.54711478])
                        # convert array to python list
                        print("Original array : ", arr.tolist())
                        print("Values with precision 3 : ", np.array(arr))
                    elif choice == 26:
                        arr = np.array([1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])
                        print(arr)
                        # If True, always print floating point numbers using fixed point notation
                        np.set_printoptions(suppress=True, precision=3)
                        print(arr)
                    elif choice == 27:
                        arr1 = np.array([[10, 20, 30], [40, 50, 60]])
                        print("Original array:""\n", arr1)
                        arr2 = np.array([[100], [200]])
                        print("After appending :""\n", np.append(arr1, arr2, axis=1))
                    elif choice == 28:
                        arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
                        print("Original array :""\n", arr)
                        index = [1, 4, 5]
                        # delete specific element from array
                        print("Delete 1st, 4th, 5th element:""\n", np.delete(arr, index))
                    elif choice == 0:
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Enter only numbers")
            except Exception as e:
                print(e)


# instantiation of class
NumPyProgram_object = NumPyPrograms()
NumPyProgram_object.numpy_operations()
