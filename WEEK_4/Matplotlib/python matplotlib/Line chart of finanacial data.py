"""  Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc.
    between October 3, 2016 to October 7, 2016. Customized the grid lines with rendering with a larger grid (major grid)
     and a smaller grid (minor grid).Turn on the grid but turn off ticks.  """

import matplotlib.pyplot as plt
import pandas as pd


class Financial:

    def read_data(self):

        # reading csv file
        df = pd.read_csv('test2.csv', sep=',', parse_dates=True, index_col=0)
        # plotting lines
        df.plot()
        # Show the figure.
        plt.show()


# creates class object
obj = Financial()
flag = False
# calling method by using class object
obj.read_data()
