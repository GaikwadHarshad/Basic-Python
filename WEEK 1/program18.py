""" Write a Python program to get an absolute file path. """


def absolute_path(path_f_name):
    import os
    # return absolute file path
    return os.path.abspath(path_f_name)


# method calling and display absolute path
print("Absolute file path : ", absolute_path('raw.txt'))
