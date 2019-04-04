from myprograms.Utility.UtilityDS import validate_num
from myprograms.WEEK_4.Matplotlib.Utility.UtilityModule import Utility
import pandas as pd
import matplotlib.pyplot as plt


# class to perform graphical representation of data using matplotlib
class DrawLineChart(Utility):
    choice = 0

    def __init__(self):
        super(DrawLineChart, self).__init__()

    def line_plotting(self):
        print("1.Draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016")
        print("2. Exit")
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
                        # reading .csv file
                        df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
                        # plotting of fdata.csv file's financial data
                        df.plot()
                        # show figures
                        plt.show()
                    elif choice == 2:
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Enter only numbers")
            except Exception as e:
                print(e)


# instantiation
DrawLineChart_object = DrawLineChart()
DrawLineChart_object.line_plotting()
