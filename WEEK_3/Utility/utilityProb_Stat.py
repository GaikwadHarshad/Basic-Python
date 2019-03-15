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

# function for getting probability of an ace from 52 cards
    def drawing_ace_after_king(self):
        probability = self.ace/(self.cards-1)
        return probability

# function for getting probability of an ace after drawing ace on 1st draw
    def drawing_ace_after_ace(self):
        probability = (self.ace-1)/(self.cards-1)
        return probability

# function to perform operations on coins
    @staticmethod
    def get_three_heads(sample_space):
        count = 0
        n = 8
        head = 'HHH'
        for prob in sample_space:
            if head == prob:
                count += 1
        if count >= 1:
            # if count >= 1 then get probability
            return count/n
        else:
            return "No Three Heads"

# function for probability of getting exactly one head in sample space
    @staticmethod
    def get_one_head(sample_space):
        count = 0
        total_sample = 8
        success_event = []
        # iterate over sample_space
        for sample in sample_space:
            # iterate each word in sample space
            for word in sample:
                # if word contain char H then count += 1
                if word == 'H':
                    count += 1
            if count == 1:
                # if H occur in 1 time then append word in list
                success_event.append(sample)
            count = 0
        print("Exactly one head : ",  success_event)
        # getting probability of successive event
        probability_of_a = len(success_event)/total_sample
        return probability_of_a

# function for probability of getting exactly one head in sample space
    @staticmethod
    def get_two_head(sample_space):
        count = 0
        total_sample = 8
        success_event = []
        # iterate over sample_space
        for sample in sample_space:
            # iterate each word in sample space
            for word in sample:
                # if word contain char H then count += 1
                if word == 'H':
                    count += 1
            if count >= 2:
                # if H occur in 1 time then append word in list
                success_event.append(sample)
            count = 0
        print("At least two head : ",  success_event)
        # getting probability of successive event
        probability_of_a = len(success_event)/total_sample
        return probability_of_a




