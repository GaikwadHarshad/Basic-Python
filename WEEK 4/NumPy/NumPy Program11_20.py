import numpy as np
from myprograms.Utility.UtilityDS import validate_num


# class for mathematical/logical operation using NumPy
class NumPyProgram:
    choice = 0

    def numpy_operations(self):
        # list of programs
        print()
        print("11. find the number of elements of an array, length of one array element""\n"
              "   in bytes and total bytes consumed by the elements")
        print()
        print("12. find common values between two arrays")
        print()
        print("13. find the set difference of two arrays. The set difference will return the sorted,""\n"
              "   unique values in array1 that are not in array2.")
        print()
        print("14. find the set exclusive-or of two arrays. Set exclusive-or will return the sorted,""\n"
              "   unique values that are in only one (not both) of the input arrays. ")
        print()
        print("15. compare two arrays using numpy")
        print()
        print("16. save a NumPy array to a text file")
        print()
        print("17. create a contiguous flattened array")
        print()
        print("18. change the data type of an array")
        print()
        print("19. create a 3-D array with ones on a diagonal and zeros elsewhere.")
        print()
        print("20.  program to create an array which looks like below array")
        print(np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]))
        print()
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
                    if choice == 11:
                        # array declaration
                        arr = np.array([10, 20, 30, 40, 50], dtype=float)
                        # get size of element
                        print("Number of element : ", arr.size)
                        # get length of element
                        print("Length of 1 element : ", arr.itemsize)
                        # get total bytes consumed by elements of array
                        print("Total bytes consumed by elements : ", arr.nbytes)
                    elif choice == 12:
                        arr1 = np.array([10, 20, 30, 40, 50])
                        print("Array 1: ", arr1)
                        arr2 = np.array([15, 25, 10, 35, 30])
                        print("Array 2: ", arr2)
                        print("Common values : ", np.intersect1d(arr1, arr2))
                    elif choice == 13:
                        arr1 = np.array([0, 10, 60, 40, 20, 80])
                        print("Array 1: ", arr1)
                        arr2 = np.array([10, 30, 40, 50, 70, 90])
                        print("Array 2: ", arr2)
                        # getting set difference between two arrays
                        print("Set difference between two arrays: ", np.setdiff1d(arr1, arr2))
                    elif choice == 14:
                        arr1 = np.array([0, 10, 20, 40, 60, 80])
                        print("Array 1: ", arr1)
                        arr2 = np.array([10, 30, 40, 50, 70])
                        print("Array 2: ", arr2)
                        print("set exclusive-or of two arrays : ", np.setxor1d(arr1, arr2))
                    elif choice == 15:
                        arr1 = np.array([1, 2])
                        print("Array 1: ", arr1)
                        arr2 = np.array([3, 4])
                        print("Array 2: ", arr2)
                        print("Array 1 < Array 2 : ", np.less(arr1, arr2))
                        print("Array 1 <= Array 2 : ", np.less_equal(arr1, arr2))
                        print("Array 1 > Array 2 : ", np.greater(arr1, arr2))
                        print("Array 1 >= Arrays 2 : ", np.greater_equal(arr1, arr2))
                    elif choice == 16:
                        a = np.arange(0, 10, 1)
                        # save array in text file
                        np.savetxt("array.txt", a[:], fmt="%d")
                        print("Array saved in array.txt file")
                        # open file to read
                        f = open("array.txt", 'r')
                        # read file
                        print(f.read())
                    elif choice == 17:
                        arr = np.array([[1, 2, 3], [4, 5, 6]])
                        print(arr)
                        # contiguous flattened array
                        arr_new = np.ravel(arr)
                        print("Contiguous Flattened array : ", arr_new)
                    elif choice == 18:
                        arr1 = np.array([1, 2, 3])
                        print("Data type of array : ", arr1.dtype)
                        # change data type of an array
                        new_arr = arr1.astype(float)
                        print("Data type of array after change : ", new_arr.dtype)
                    elif choice == 19:
                        # 3x3 array of 0 with 1 on diagonal (Identity matrix)
                        x = np.eye(3)
                        print(x)
                    elif choice == 20:
                        def get_pattern(matrix, row, col):
                            # iterate over rows
                            for r_count in range(0, row):
                                # iterate over cols
                                for c_count in range(0, col):
                                    # if row 1 or more and col less than row print 1
                                    if r_count > 0 and c_count < r_count:
                                        print("1", end=" ")
                                    else:
                                        # print zero's as it is
                                        print(matrix[r_count][c_count], end=" ")
                                print()

                        arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
                        r = 4
                        c = 3
                        # function call to get above pattern
                        get_pattern(arr, r, c)
                    elif choice == 0:
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Enter only numbers")
            except Exception as e:
                print(e)


# instantiation
NumPyProgram_object = NumPyProgram()
NumPyProgram_object.numpy_operations()
