""" A radar unit is used to measure speeds of cars on a motorway. The speeds are normally distributed with
    a mean of 90 km/hr and a standard deviation of 10 km/hr. Write a program to find the probability
    that a car picked at random is travelling at more than 100 km/hr?  """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


class RadarUnit(ProbabilityStatistics):

    def __init__(self):
        super(RadarUnit, self).__init__()
        # speed of car
        self.X = 100
        # mean value
        self.mean = 90
        # standard deviation
        self.std_deviation = 10

    def get_probability(self):
        # find out whether probability of x is higher
        probability = ProbabilityStatistics.get_probability_higher(self, self.X, self.mean, self.std_deviation)
        print("probability that a car picked at random is travelling at more than 100 km/hr: ", probability)


# instantiation
RadarUnit_object = RadarUnit()
RadarUnit_object.get_probability()
