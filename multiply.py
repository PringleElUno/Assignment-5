# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/29/2024
# Define a recursive function named multiply that takes two positive integers as parameters
# and returns the product of those two numbers

def multiply(num1: int, num2: int):
    """
    Recursive function to calculate the product of two positive integers  without the use of multiplication
    :param num1: first positive integer
    :param num2: second positive integer
    :return: product of num1 and num2
    """
    if num2 == 1:
        print(str(num1) + " * " + str(num2) + " = " + str(num1))
        return num1 # This is the base case, return num1 as string
    else:
        # Creating the recursive case to build the string expression
        print(str(num1) + " * " + str(num2) + " = " + str(num1) + " + (" + str(num1) + " * " + str(num2 - 1) +")")
        return num1 + multiply(num1, num2 -1)

def main(num1: int, num2: int):
    multiply(num1, num2)
    result_expression = build_result_expression(num1, num2)
    print("So, " + str(num1) + " * " + str(num2) + " = " + result_expression)

def build_result_expression(num1: int, num2: int):
    """
    Print each line of the multiplication process without direct multiplication
    :param num1: first positive integer
    :param num2: second positive integer
    :return: string representation of the multiplication process
    """
    if num2 == 1:
        return str(num1)
    else:
        return str(num1) + " + (" + build_result_expression(num1, num2 - 1) + ")"


main(7,4)
