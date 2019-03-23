from myprograms.Utility.UtilityDS import validate_num
import matplotlib.pyplot as plt


# class to perform graphical representation of data using matplotlib
class DrawLineByGivenAxis:
    choice = 0

    def line_plotting(self):
        print()
        print("1.draw a line using given axis values with suitable label in the x axis , y axis and a title")
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
                        # x axis values
                        x = [1, 2, 3]
                        # y axis values
                        y = [2, 4, 1]
                        # plot lines to the axes
                        plt.plot(x, y)
                        # set label for x axes
                        plt.xlabel('x_axis')
                        # set label for y axes
                        plt.ylabel('y_axis')
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


# class instantiation
DrawLineByGivenAxis_object = DrawLineByGivenAxis()
DrawLineByGivenAxis_object.line_plotting()
