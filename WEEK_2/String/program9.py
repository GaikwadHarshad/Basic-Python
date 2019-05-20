""" Write a Python program to display formatted text (width=50) as output. """

from myprograms.Utility import UtilityDS


class String9:
    string = ''' Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.'''

    # perform operation on string
    def format_string(self):
        while 1:
            print("--------------------------------------------------")
            print("1.Display String""\n""2.Get format result""\n""3.Exit")
            try:
                choice = int(input("Enter choice :"))
                # validate choice
                ch = UtilityDS.validate_num(choice)
                if ch:
                    if choice == 1:
                        print("The String : ", self.string)
                    elif choice == 2:
                        if self.string.__len__() < 1:
                            print("Enter string first")
                        else:
                            # get formatted result of string
                            result = UtilityDS.format_string(self.string)
                            print(result)
                    elif choice == 3:
                        exit()
                    else:
                        print("Invalid choice")
                else:
                    print("Enter choice between 1 - 3")
            except Exception as e:
                print(e)


# instantiation
String9_object = String9()
String9_object.format_string()