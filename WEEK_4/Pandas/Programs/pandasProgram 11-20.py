from myprograms.Utility.UtilityDS import validate_num
from myprograms.WEEK_4.Pandas.UtilityModule.Utility import UtilityClass


# class for mathematical/logical operation using NumPy
class PandasProgram(UtilityClass):
    choice = 0

    def __init__(self):
        super(PandasProgram, self).__init__()

    def pandas_operations(self):
        # list of programs
        print("11. count the number of rows and columns of a DataFrame")
        print("12. select the rows where the score is missing, i.e. is NaN. ")
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
                    if choice == 11:
                        df = UtilityClass.get_data_frame()
                        print(df, "\n")
                        # get row count from DataFrame
                        rows = len(df.axes[0])
                        # get column count from DataFrame
                        cols = len(df.axes[1])
                        print("Total rows: "+str(rows))
                        print("Total cols: "+str(cols))
                    elif choice == 12:
                        df = UtilityClass.get_data_frame()
                        print(df, "\n")
                        print("rows where the score is missing:""\n")
                        # get rows where score value is missing
                        print(df[df['score'].isnull()])
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
