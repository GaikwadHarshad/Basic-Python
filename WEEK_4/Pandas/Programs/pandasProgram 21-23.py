from myprograms.Utility.UtilityDS import validate_num
from myprograms.WEEK_4.Pandas.UtilityModule.Utility import UtilityClass


# class for perform data manipulation/data analysis using pandas data structure
class PandasProgram(UtilityClass):
    choice = 0

    def __init__(self):
        # passing child class object to parent class constructor
        super(PandasProgram, self).__init__()
        # getting  DataFrame from Utility Class
        self.df = UtilityClass.get_data_frame()

    def pandas_operations(self):
        # list of programs
        print("21. Insert a new column in existing DataFrame")
        print("22. program to iterate over rows in a DataFrame")
        print("23. get list from DataFrame column headers")
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
                    if choice == 21:

                        print(self.df, "\n")
                        # function to get insert new column in DataFrame
                        new_col = UtilityClass.add_new_col_in_data_frame(self.df)
                        print(new_col)
                    elif choice == 22:
                        # iterate over rows in DataFrame
                        for index, row in self.df.iterrows():
                            print(row['name'], row['score'])
                    elif choice == 23:
                        # get list from DataFrame column headers
                        print(list(self.df.columns.values))
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
