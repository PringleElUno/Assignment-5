# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/29/2024
# Define a recursive function named multiply that takes two positive integers as parameters
# and returns the product of those two numbers

def multiply(num1: int, num2: int) -> int:
    """
    Recursive function to calculate the product of two positive integers without using multiplication.
    :param num1: first positive integer
    :param num2: second positive integer
    :return: product of num1 and num2
    """
    # Base case: if num2 is 1, simply return num1
    if num2 == 1:
        return num1
    else:
        # Recursive case: add num1 to the result of multiply(num1, num2 - 1)
        return num1 + multiply(num1, num2 - 1)

# Example usage
result = multiply(7, 4)
print("The result is:", result)
