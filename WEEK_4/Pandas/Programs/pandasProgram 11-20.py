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
        print("13. select the rows where number of attempts in the examination is less than 2"
              " and score greater than 15. ")
        print("14. change the score in row 'd' to 11.5")
        print("15. calculate the sum of the examination attempts by the students. ")
        print("16. calculate the mean score for each different student in DataFrame. ")
        print("17.  append a new row 'k' to data frame with given values for each column."
              "Now delete the new row and return the original DataFrame. ")
        print("18. sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order")
        print("19. replace the 'qualify' column contains the values 'yes' and 'no' with True and False. ")
        print("20. delete the 'attempts' column from the DataFrame")
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
                    elif choice == 13:
                        df = UtilityClass.get_data_frame()
                        print(df, "\n")
                        # get rows where exam attempt is less than 2 and score greater than 15
                        print(df.ix[[9], ['name', 'score']])
                    elif choice == 14:
                        df = UtilityClass.get_data_frame()
                        print(df, "\n")
                        # change the score of row 'd' to 11.5
                        df.loc['d', 'score'] = 11.5
                        print(df)
                    elif choice == 15:
                        df = UtilityClass.get_data_frame()
                        # get sum of examination attempts
                        print("sum of attempts : ", df['attempts'].sum())
                    elif choice == 16:
                        df = UtilityClass.get_data_frame()
                        print(df)
                        # calculating mean value for each student
                        print("Mean for each student: ", df['score'].mean())
                    elif choice == 17:
                        df = UtilityClass.get_data_frame()
                        # original DataFrame
                        print("original DataFrame:""\n")
                        print(df, "\n")
                        # change data in DataFrame
                        data = UtilityClass.change_in_data_frame(df)
                        print("After delete : ""\n", data)
                    elif choice == 18:
                        df = UtilityClass.get_data_frame()
                        print(df, "\n")
                        # sort name column in descending order
                        df = df.sort_values(by=['name'], ascending=False)
                        print("Desc by Name")
                        print(df)
                        print("Asc by score")
                        # sort score data in ascending order
                        df = df.sort_values(by=['score'], ascending=True)
                        print(df)
                    elif choice == 19:
                        df = UtilityClass.get_data_frame()
                        # replacing value of qualify column from yes - True and no - False
                        df['qualify'] = df['qualify'].map({'yes': True, 'no': False})
                        print(df)
                    elif choice == 20:
                        df = UtilityClass.get_data_frame()
                        print(df)
                        print("\n""After deleting attempts column:""\n")
                        # delete column
                        df.pop('attempts')
                        print(df)
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
