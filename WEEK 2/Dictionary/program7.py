"""Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}. """

from myprograms.Utility import UtilityDS


class Unique:
    # function definition for performing to get unique values
    def unique_val(self):
        sample = [{"V": "S001"}, {"V": "S002"},
                  {"VI": "S001"}, {"VI": "S005"},
                  {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
        print("Original data : ", sample)
        while 1:
            try:
                print("1: Find unique values in dictionary ""\n""2: Original dictionary""\n""3: Exit")
                ch = int(input("Enter your choice: "))
                # validate choice number
                choice = UtilityDS.validate_num(ch)
                if choice:
                    if ch == 1:
                        # get all unique values in dictionary
                        unique_data = UtilityDS.unique_values(sample)
                        print("Unique value in dictionary : ", unique_data)
                    elif ch == 2:
                        # get original dictionary
                        print("Original Dictionary : ", sample)
                    elif ch == 3:
                        exit()
                    else:
                        print("please enter valid choice")
                else:
                    # if entered literals except int
                    print("please enter number only")
            except Exception as e:
                print(e)


# instance creation
Unique_object = Unique()
Unique_object.unique_val()
