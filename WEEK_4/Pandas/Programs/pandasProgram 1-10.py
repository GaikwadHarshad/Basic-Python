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
        print("4. program to get the powers of an array values element-wise")
        print("5. create and display a DataFrame from a specified dictionary data which has the index labels")
        print("6. display a summary of the basic information about a specified Data Frame and its data.")
        print("7. program to get the first 3 rows of a given DataFrame")
        print("8. program to select the 'name' and 'score' columns from the given DataFrame. ")
        print("9. select the specified columns and rows from a given data frame."
              "Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the given data frame")
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
                    elif choice == 4:
                        power = UtilityClass.get_power()
                        print("Power of array value to element wise:")
                        print(power)
                    elif choice == 5:
                        # get data frame for specified data
                        df = UtilityClass.get_data_frame()
                        print(df)
                    elif choice == 6:
                        df = UtilityClass.get_data_frame()
                        print("Summary of basic information about specified data frame")
                        # summary of data frame
                        print(df.info())
                    elif choice == 7:
                        df = UtilityClass.get_data_frame()
                        print("data frame :")
                        print(df, "\n")
                        print("First 3 rows of data frame:")
                        print(df.iloc[:3])
                    elif choice == 8:
                        df = UtilityClass.get_data_frame()
                        # getting name and score column from DataFrame
                        print(df[['name', 'score']])
                    elif choice == 9:
                        df = UtilityClass.get_data_frame()
                        print(df, "\n")
                        print("specified column and row from given DataFrame""\n")
                        # getting specific column and row from DataFrame
                        print(df.iloc[[1, 3, 5, 6], [0, 1]])
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
