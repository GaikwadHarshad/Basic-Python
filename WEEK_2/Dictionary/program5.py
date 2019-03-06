""" Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} """

from myprograms.Utility import UtilityDS


class GenerateDict:
    # function to generate script
    def generate_script(self):
        while 1:
            try:
                print("Enter your choice:")
                input_text = int(input("1: Generate Script""\n""2:Exit"" : "))
                # exit the program when choice is 2("Exit")
                if input_text == 2:
                    exit()
                # else generate script and print dictionary
                elif input_text == 1:
                    num = int(input("\n""Enter any Positiver number : "))
                    # validate number
                    sample = UtilityDS.validate_num(num)
                    if sample:
                        # if number is valid then call function for generating script
                        script = UtilityDS.script_generate1(num)
                        print(script)
                    else:
                        print("Enter valid number to generate script")
                # display message when you entered invalid choice
                else:
                    print("You entered wrong choice")
            except Exception as e:
                print(e)


# instance creation
Generate_Dict_obj = GenerateDict()
Generate_Dict_obj.generate_script()
