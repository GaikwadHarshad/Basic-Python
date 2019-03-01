""" Write a Python program which accepts the user's first and last name'
    and print them in reverse order with a space between them """

firstName = input("Enter user's first name : ")
lastName = input("Enter user's last name : ")
revFirstName = (firstName[::-1] + " " + lastName[::-1])
print(revFirstName)
