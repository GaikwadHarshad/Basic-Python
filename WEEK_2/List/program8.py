""" Write a Python program to find the list of words that are longer than n from a given list of words.  """

from myprograms.Utility import UtilityDS


class List8:
    create = []

    # function to perform operations on list
    def longer_word(self):
        while 1:
            print("---------------------------------------------------")
            print("1.Create List""\n""2. Get words longer than N""\n""3.Exit")
            try:
                choice = int(input("Enter any choice :"))
                # validating choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # create list
                    if choice == 1:
                        print("we are creating list : ")
                        # number of element to add
                        element = int(input("How many element you want to add: "))
                        # validating the number
                        e = UtilityDS.validate_num(element)
                        if e:
                            # if valid then create list
                            self.create = UtilityDS.create_list_all(element)
                            print("List is created : ", self.create)
                    elif choice == 2:
                        # if list is empty
                        if len(self.create) == 0:
                            print("List is empty..create list first.")
                        # if list in not empty then display list of word longer than Num
                        else:
                            num = int(input("Enter the number to get longer words : "))
                            valid_num = UtilityDS.validate_num(num)
                            if valid_num:
                                n = UtilityDS.word_longer(self.create, num)
                                print("Words longer than number : ", n)
                    elif choice == 3:
                        # exit from program
                        exit()
                    else:
                        print("Invalid choice")

            except Exception as e:
                print(e)


# instantiation of class
List8_object = List8()
List8_object.longer_word()
