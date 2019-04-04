""" Write a program to find probability of drawing an ace from pack of cards """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


# class inheritance
class DrawingAce(ProbabilityStatistics):
    def __init__(self):
        super(DrawingAce, self).__init__()

    # get probability of ace from 52 cards
    def get_probability(self):
        # function calls to drawing an ace
        prob = ProbabilityStatistics.drawing_ace(self)
        print("probability of drawing an ace from pack of cards : ", round(prob, 2))


# instantiation
DrawingAce_object = DrawingAce()
DrawingAce_object.get_probability()
