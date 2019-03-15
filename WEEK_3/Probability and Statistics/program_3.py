""" Write a program to find the probability of drawing an ace after drawing an ace on the first draw """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


# class inheritance
class DrawingAceAfterFirstDraw(ProbabilityStatistics):
    def __init__(self):
        super(DrawingAceAfterFirstDraw, self).__init__()

    # get probability of ace from 52 cards
    def get_probability(self):
        # function calls to drawing an ace
        prob1 = ProbabilityStatistics.drawing_ace(self)
        print("Probability of drawing an ace before drawing ace on 1st draw : ", prob1)
        prob2 = ProbabilityStatistics.drawing_ace_after_ace(self)
        print("probability of drawing an ace after drawing king on 1st draw : ", prob2)


# instantiation
DrawingAceAfterFirstDraw_object = DrawingAceAfterFirstDraw()
DrawingAceAfterFirstDraw_object.get_probability()
