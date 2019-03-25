""" Write a Python program to display the current axis limits values and set new axis values.  """

import matplotlib.pyplot as plt
from myprograms.WEEK_4.Matplotlib.Utility.UtilityModule import Utility


class SetAxisValues:
    # line 1 points
    utility_obj = Utility()

    def draw_line(self):

        # line 1 points
        x1 = int(input("how many values do u wanna insert in x-axis for line1"))
        x1_list = self.utility_obj.CreateList(x1)
        print(x1_list)

        y1 = int(input("how many values do u wanna insert in y-axis for line1"))
        y1_list = self.utility_obj.CreateList(y1)
        print(y1_list)

        # plotting the line 1 points
        plt.plot(x1_list, y1_list, label="line 1")

        # Set the x axis label
        plt.xlabel('x - axis')
        # Set the y axis label
        plt.ylabel('y - axis')

        # Sets a title
        plt.title('Two or more lines on same plot with suitable legends ')

        # returns current axis values
        print(plt.axis())
        # xmin,xmax,ymin,ymax=plt.axis()

        # accepting values to set new axis values
        print("set new axis limit")
        xmin = int(input("xmin val"))
        xmax = int(input("xmax val"))
        ymin = int(input("ymin val"))
        ymax = int(input("ymax val"))

        # sets new axis values
        plt.axis([xmin, xmax, ymin, ymax])

        # show a legend on the plot
        plt.legend()

        # Display a figure.
        plt.show()


# creates class object
obj = SetAxisValues()
# calling method by using class object
obj.draw_line()
