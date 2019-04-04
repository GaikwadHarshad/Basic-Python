""" Write a Python program to count the number occurrence of a specific character in a string. """


def count_char(string_accept):

    # get empty dictionary
    dictionary1 = {}

    # checking each character for getting occurrence
    for i in string_accept:

        # get keys of each values from dictionary
        key = dictionary1.keys()
        if i in key:

            # if key found then increase its occurrence
            dictionary1[i] = dictionary1[i]+1
        else:
            # if key not found then occurrence is 1
            dictionary1[i] = 1
    # return dictionary to caller
    return dictionary1


string = "independence"

# function call and pass string as argument
print("The occurrence of each character : ", count_char(string))

