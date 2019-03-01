""" Write a Python program to convert an integer to binary keep leading zeros.
    Sample data : 50
    Expected output : 00001100, 0000001100 """


def convert_to_binary(num):
    if num < 0:
        return 0
    else:
        i = 1
        bin1 = 0
        # loop for convert integer to binary number
        while num > 0:
            rem = num % 2
            # get remainder multiply with ith and add to bin1
            bin1 = bin1 + (rem * i)
            # divide num by 2
            num //= 2
            i *= 10
    return bin1


n = 50
# method call
convert = convert_to_binary(n)
print("Binary conversion without leading zero's :", convert)
# format binary number with leading zero's
print("Binary conversion with leading zero's : "+format(n, '08b'))
print("Binary conversion with leading zero's : "+format(n, '010b'))

