import pandas as pd
from myprograms.Utility.UtilityDS import validate_num
from myprograms.WEEK_4.Pandas.UtilityModule.Utility import UtilityClass


# class for mathematical/logical operation using NumPy
class PandasProgram(UtilityClass):
    choice = 0

    def __init__(self):
        super(PandasProgram, self).__init__()

    def pandas_operations(self):
        # list of programs
        print("1. create and display a 1-D array-like object containing an array of data using Pandas module")
        print("2. convert a Panda module Series to Python list and it's type")
        print("3. program to add, subtract, multiple and divide two Pandas Series")
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
                        n = int(input("How many element you want to add:"))
                        if validate_num(n):
                            num = int(n)
                            # 1D labeled array holding integer type data
                            data = UtilityClass.series_data(self, num)
                            print(data)
                        else:
                            print("Please enter numeric value")
                    elif choice == 2:
                        n = input("How many element you want to add:")
                        if validate_num(n):
                            num = int(n)
                            # getting series of data from pandas module
                            data = UtilityClass.series_data(self, num)
                            print("Pandas Series : ""\n", data)
                            # type of series
                            print("Type of series : ", type(data))
                            # convert series data into python list and display type
                            print("Converted python list : ", data.tolist())
                            print("Type of python list : ", type(data.tolist()))
                        else:
                            print("Please enter numeric value")
                    elif choice == 3:
                        n = input("How many element you want to add:")
                        if validate_num(n):
                            num = int(n)
                            # getting 1st series of data from pandas module
                            data1 = UtilityClass.series_data(self, num)
                            print("First pandas series : ")
                            print("Pandas Series 1:""\n", data1)
                            print("New series : ")
                            # getting 1st series of data from pandas module
                            data2 = UtilityClass.series_data2(self, num)
                            print("Second pandas series : ")
                            print("Pandas Series 2:""\n", data2)
                            add = UtilityClass.series_addition(data1, data2)
                            print("Addition:""\n", add)
                            sub = UtilityClass.series_subtract(data1, data2)
                            print("Subtraction:""\n", sub)
                            mul = UtilityClass.series_multiplication(data1, data2)
                            print("Multiplication:""\n", mul)
                            div = UtilityClass.series_division(data1, data2)
                            print("Division:""\n", div)
                        else:
                            print("Please enter numeric value")
                    elif choice == 0:
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Enter only numbers")
            except Exception as e:
                print(e)


# instantiation
PandasProgram_object = PandasProgram()
PandasProgram_object.pandas_operations()
