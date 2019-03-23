from myprograms.Utility.UtilityDS import validate_num
from myprograms.WEEK_4.Matplotlib.Utility.UtilityModule import Utility

import matplotlib.pyplot as plt


# class to perform graphical representation of data using matplotlib
class DrawLine(Utility):
    choice = 0

    def __init__(self):
        super(DrawLine, self).__init__()

    def line_plotting(self):
        print("1.draw a line with suitable label in the x axis, y axis and a title")
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
                        print("Enter range to draw line:")
                        get_xrange = Utility.get_range(self)
                        # y range values thrice than x
                        y = [value * 3 for value in get_xrange]
                        print("values of x:")
                        print(*get_xrange)
                        print("values of y(thrice of x)")
                        # plot lines to the axes
                        plt.plot(get_xrange, y)
                        # set label for x axes
                        plt.xlabel('x_axix')
                        # set label for y axes
                        plt.ylabel('y_axix')
                        # title for plotting line
                        plt.title('line')
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
DrawLine_object = DrawLine()
DrawLine_object.line_plotting()
