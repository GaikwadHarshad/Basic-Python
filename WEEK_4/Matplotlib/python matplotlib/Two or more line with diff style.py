import matplotlib.pyplot as plt
from myprograms.WEEK_4.Matplotlib.Utility.UtilityModule import Utility


class PlotTwoLineWithDiffStyle:
    # creates utility class object
    utility_obj = Utility()

    def draw_line(self):

        # line 1 points
        x1 = int(input("how many values do u wanna insert in x-axis for line1"))
        x1_list = self.utility_obj.CreateList(x1)
        print(x1_list)

        y1 = int(input("how many values do u wanna insert in y-axis for line1"))
        y1_list = self.utility_obj.CreateList(y1)
        print(y1_list)

        # plotting the line 1 points with dash line style
        plt.plot(x1_list, y1_list, linestyle='dashed', label="line 1")

        # line 2 points
        x2 = int(input("how many values do u wanna insert in x-axis for line2"))
        x2_list = self.utility_obj.CreateList(x2)
        print(x2_list)

        y2 = int(input("how many values do u wanna insert in y-axis for line2"))
        y2_list = self.utility_obj.CreateList(y2)
        print(y2_list)

        # plotting the line 2 points with Dotted line style
        plt.plot(x2_list, y2_list, linestyle=':', label="line 2")

        # line 3 points
        x3 = int(input("how many values do u wanna insert in x-axis for line2"))
        x3_list = self.utility_obj.CreateList(x3)
        print(x3_list)

        y3 = int(input("how many values do u wanna insert in y-axis for line2"))
        y3_list = self.utility_obj.CreateList(y3)
        print(y3_list)

        # plotting the line 3 points with Dash-dot line style
        plt.plot(x3_list, y3_list, linestyle='-.', label="line 2")

        # Set the x axis label
        plt.xlabel('x - axis')
        # Set the y axis label
        plt.ylabel('y - axis')

        # Sets a title
        plt.title('Two or more lines on same plot with suitable legends ')

        # show a legend on the plot
        plt.legend()

        # Display a figure.
        plt.show()


PlotTwoLineWithDiffStyle_obj = PlotTwoLineWithDiffStyle()
PlotTwoLineWithDiffStyle_obj.draw_line()
