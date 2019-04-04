from myprograms.Utility import UtilityDS


class ExceptionHandle:

    def __init__(self, num):
        self.n = num

        if not UtilityDS.validate_num(self.n):
            self.ValueError = "Enter a number only"





