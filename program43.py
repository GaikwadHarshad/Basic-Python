""" Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
    Note: Do not use built-in functions. """


def min_max_number(numbers):
    # consider 1 element as large
    large = numbers[0]
    # consider 1 element as small
    small = numbers[0]

    for n in numbers:
        if n > large:
            # nth element will be large if nth > large
            large = n
        elif n < small:
                # nth element will be small if nth < small
                small = n
    return large, small


print()
seq_num = [22, -5, -3, 55, 32, 61, 25, -1]
# method call and display min,max number amongst
print("Maximum and Minimum number from sequence of numbers : ", min_max_number(seq_num))
