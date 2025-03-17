# 1.Program to find the square root of a number
# sqrt 25 = 5 because 5*5 = 25

import math #import the math module

number = int(input("Enter a number: ")) # take input from the user
root = int(number ** 0.5) # calculate the square root using ** 
fun = math.sqrt(number) # calculate the square root using math.sqrt()

print(f"The square root of {number} is {root} -- using  **") # print the square root
print(f"The square root of {number} is {fun} -- using math.sqrt()")


"""Problem Statement

Given a non-negative number 
x
x, write a program to compute and return its square root. If the number is not a perfect square, return the square root rounded to two decimal places.

Input


Output

A single floating-point or integer value representing the square root of 
x
x.
If 
x
x is a perfect square, return an integer.
If 
x
x is not a perfect square, return the square root rounded to two decimal places.
Example 1

Input:

x = 25
Output:

5
Example 2

Input:

x = 20
Output:

4.47
Example 3

Input:

x = 0
Output:

0
Constraints

The input number 
x
x is non-negative.
The program should handle large numbers efficiently.
The result should be rounded to two decimal places when necessary.
"""

number = int(input("Enter a number: ")) # take input from the user
if number < 0:
    print("Please enter a non-negative number.")
else:
    root = number ** 0.5

    if root % 1 == 0:
        print(f"The square root of {number} is {int(root)}")
    else:
        print(f"The square root of {number} is {root:.2f}")
