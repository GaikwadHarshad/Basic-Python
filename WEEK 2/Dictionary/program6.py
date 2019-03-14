""" Write a Python program to remove a key from a dictionary """

from myprograms.Utility import UtilityDS


class RemoveKey:
    # function for perform key operation
    def rm_key(self):
        # create and display dictionary
        dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
        print("Original dictionary : ", dictionary)
        while True:
            try:
                print("1: Remove Key ""\n""2: Exit""\n""3: view dictionary")
                choice = int(input("\n""Enter your choice : "))
                # validating choice number
                ch = UtilityDS.validate_num(choice)
                if ch:
                    # exit from program when choice is 2(Exit)
                    if choice == 2:
                        exit()
                    # execute operation of key removal when choice is 1(Remove key)
                    elif choice == 1:
                        k = input("Which key you want to remove : ")
                        # key removal function
                        remove = UtilityDS.remove_key(dictionary, k)
                        # display message if key not present
                        if remove == 0:
                            print("Key is not present in dictionary")
                        else:
                            print("After removed a key :", remove)
                            # update dictionary after removal of key
                            dictionary = remove
                    # to view dictionary
                    elif choice == 3:
                        print(dictionary)
                    else:
                        print("You entered wrong choice")
                else:
                    print("Please enter valid choice")
            except Exception as e:
                print(e)


remove_object = RemoveKey()
remove_object.rm_key()
