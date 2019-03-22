import numpy as np
from myprograms.Utility.UtilityDS import validate_num


# class for mathematical/logical operation using NumPy
class NumPyProgram:
    choice = 0

    def numpy_operations(self):
        # list of programs
        print("1. convert a list of numeric value into a one-dimensional NumPy array")
        print("2. 3x3 matrix with values ranging from 2 to 10")
        print("3. create a null vector of size 10 and update sixth value to 11")
        print("4. reverse an array (first element becomes last).")
        print("5. create a 2d array with 1 on the border and 0 inside")
        print("6. program to add a border (filled with 0's) around an existing array")
        print("7. create a 8x8 matrix and fill it with a checkerboard pattern")
        print("8. convert a list and tuple into arrays")
        print("9. program to append values to the end of an array")
        print("10.find the real and imaginary parts of an array of complex numbers")
        print("0. Exit")
        print()
        while True:
            try:
                print()
                # accept choice from user
                self.choice = input("Enter choice : ")
                # validate choice number
                valid_choice = validate_num(self.choice)
                if valid_choice:
                    choice = int(self.choice)
                    if choice == 1:
                        list1 = [12.23, 13.32, 100, 36.32]
                        print("Original List is : ", list1)
                        # function to convert list into NumPy array
                        arr = np.array(list1)
                        print("1D NumPy array : ", arr)
                    elif choice == 2:
                        # create array within range and reshape it 3x3
                        matrix = np.arange(2, 11).reshape(3, 3)
                        print(matrix)
                    elif choice == 3:
                        # create vector of 11 zero's
                        vector = np.zeros(11)
                        print("Null Vector : ", vector)
                        vector[5] = 11
                        print("Update sixth value to 11 : ", vector)
                    elif choice == 4:
                        arr = np.arange(12, 38)
                        print("original : ", arr)
                        # reverse array
                        print("reverse : ", arr[::-1])
                    elif choice == 5:
                        # create 5x5 array with one's value
                        arr = np.ones((5, 5))
                        print("Original array : ""\n", arr)
                        print("array with 1 on the border and 0 inside")
                        # slicing on array
                        arr[1:-1, 1:-1] = 0
                        print(arr)
                    elif choice == 6:
                        # create array 3x3 with all 1's
                        arr = np.ones((3, 3))
                        print(arr)
                        # add border filled with 0's around existing array
                        arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
                        print(arr)
                    elif choice == 7:
                        arr = np.zeros((8, 8), dtype=int)
                        # fill checkerboard pattern with 1 at every 2 row , 2 col
                        arr[1::2, ::2] = 1
                        # fill checkerboard pattern with 1 at every 2 row, 2 col
                        arr[::2, 1::2] = 1
                        print(arr)
                    elif choice == 8:
                        list1 = [1, 2, 3, 4, 5, 6, 7, 8]
                        print("List : ", list1)
                        # convert any type of input data into array
                        print("Array : ", np.asarray(list1))
                        tuple1 = ([8, 4, 6], [1, 2, 3])
                        print("Tuple : ", tuple1)
                        print("Array : ", np.asarray(tuple1))
                    elif choice == 9:
                        arr = [10, 20, 30]
                        print("Original array : ", arr)
                        # append values at end of array
                        arr = np.append(arr, [[40, 50, 60], [70, 80, 90]])
                        print("After append : ", arr)
                    elif choice == 10:
                        value1 = np.sqrt([1+0j])
                        value2 = np.sqrt([0+1j])
                        print("Original value1 : ", value1)
                        print("Original value2 : ", value2)
                        value3 = value1 + value2
                        print("Real part : ", value3.real)
                        print("Imaginary part : ", value3.imag)
                    elif choice == 0:
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Enter only numbers")
            except Exception as e:
                print(e)


# instantiation of class
NumPyProgram_object = NumPyProgram()
NumPyProgram_object.numpy_operations()
