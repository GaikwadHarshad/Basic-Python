""" Given the following statistics, write a program to find the probability that a woman has cancer
    if she has a positive mammogram result?
        a. One percent of women over 50 have breast cancer.
        b. Ninety percent of women who have breast cancer test positive on mammograms.
        c. Eight percent of women will have false positives. """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


class MammogramResult(ProbabilityStatistics):
    def __init__(self):
        super(MammogramResult, self).__init__()

    def get_probability(self):
        # getting probability
        result = ProbabilityStatistics.mammogram_result(self)
        print("Probability that a woman has a cancer if she has a positive mammogram result : ", result)


# instantiation
MammogramResult_object = MammogramResult()
MammogramResult_object.get_probability()
