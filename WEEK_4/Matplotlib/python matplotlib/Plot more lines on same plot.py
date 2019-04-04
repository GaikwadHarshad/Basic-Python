from myprograms.Utility.UtilityDS import validate_num, create_list
from myprograms.WEEK_4.Matplotlib.Utility.UtilityModule import Utility
import matplotlib.pyplot as plt


# class to perform graphical representation of data using matplotlib
class PlotMoreLineOnSamePlot(Utility):
    choice = 0

    def __init__(self):
        super(PlotMoreLineOnSamePlot, self).__init__()

    def line_plotting(self):
        print("1.plot two or more lines on same plot with suitable legends of each line.")
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
                        print("Enter range to draw line 1:")
                        print("x axix:")
                        x1 = create_list(3)
                        print("Y axix :")
                        y1 = create_list(3)
                        plt.plot(x1, y1, label="line 1")
                        print("values of x:")
                        print(*x1)
                        print("values of y:")
                        print(*y1)
                        print("Enter range to draw line 2:")
                        print("x axix:")
                        x2 = create_list(3)
                        print("Y axix:")
                        y2 = create_list(3)
                        plt.plot(x2, y2, label="line 2")
                        print("values of x:")
                        print(*x2)
                        print("values of y:")
                        print(*y2)
                        # plot lines to the axes

                        # set label for x axes
                        plt.xlabel('x_axix')
                        # set label for y axes
                        plt.ylabel('y_axix')
                        # title for plotting line
                        plt.title('Two lines on same plot')
                        plt.legend()
                        # show the figure
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
PlotMoreLineOnSamePlot_object = PlotMoreLineOnSamePlot()
PlotMoreLineOnSamePlot_object.line_plotting()
