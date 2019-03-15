# class to perform operation on probability and statistics
class ProbabilityStatistics:
    # constructor
    def __init__(self):
        self.ace = 4
        self.king = 4
        self.queen = 4
        self.jack = 4
        self.cards = 52

    # function for getting probability of an ace from 52 cards
    def drawing_ace(self):
        probability = self.ace/self.cards
        return probability
