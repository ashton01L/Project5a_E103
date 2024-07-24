# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/23/2024
# Description: Define a recursive function named multiply that takes two positive
# integers as parameters and returns the product of those two numbers
# (the result from multiplying them together).

def multiply(x, y):
    if y == 1:
        return x
    else:
        return x + multiply(x, y - 1)

# print(multiply(7,4))
