# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/29/2024
# Define a recursive function named multiply that takes two positive integers as parameters
# and returns the product of those two numbers

# Defining multiply to begin the recursive function
def multiply(num1: int, num2: int):
    """
    Recursive function to calculate the product of two positive integers  without the use of multiplication
    :param num1: first positive integer
    :param num2: second positive integer
    :return: product of num1 and num2
    """
    if num2 == 1:
        return num1 # This is the base case, return num1 as string
    else:
        return num1 + multiply(num1, num2 -1)
