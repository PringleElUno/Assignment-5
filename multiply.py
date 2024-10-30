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
        return num1 # This is the base case, return num1 as string
    else:
        # Creating the recursive case to build the string expression
        return num1 + multiply(num1, num2 -1)

def print_multiplication(num1: int, num2: int):
    """
    Print each line of the multiplication process without direct multiplication
    :param num1: first positive integer
    :param num2: second positive integer
    :return: string representation of the multiplication process
    """
    if num2 == 1:
        # Print the base case
        print(num1, "*", num2, "=", num1)
    else:
        # Print the multiplication step
        print(num1, "*", num2, "=", num1, "+ (", num1, "*", num2 - 1, ")")
        print_multiplication(num1, num2 - 1)

# Defining the result to later print
def final_result(num1: int, num2: int):
    """
    Print final lines of multiplication
    :param num1: first positive integer
    :param num2: second positive integer
    :return: string representation of the multiplication process
    """
    if num2 == 1:
        return str(num1)
    else:
        return str(num1) + " + (" + final_result(num1,num2 - 1) + ")"

# Main function for displaying the arithmetic
def main(num1: int, num2: int):
    print_multiplication(num1, num2)
    result_expression = final_result(num1, num2)
    print("So,", num1, "*", num2, "=", result_expression)

main(7,4)
