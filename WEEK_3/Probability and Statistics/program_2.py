""" Write a program to find the probability of drawing an ace after drawing a king on the first draw """
from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


# class inheritance
class DrawingAce(ProbabilityStatistics):
    def __init__(self):
        super(DrawingAce, self).__init__()

    # get probability of ace from 52 cards
    def get_probability(self):
        # function calls to drawing an ace
        prob1 = ProbabilityStatistics.drawing_ace(self)
        print("Probability of drawing an ace before drawing king : ", prob1)
        prob2 = ProbabilityStatistics.drawing_ace_after_king(self)
        print("probability of drawing an ace after drawing king on 1st draw : ", prob2)


# instantiation
DrawingAce_object = DrawingAce()
DrawingAce_object.get_probability()
