# 2.Program to find the area of Rectangle

"""Problem Statement

Given the length and width of a rectangle, write a program to calculate and return its area.

Input

Two positive integers or floating-point numbers:
length (1 ≤ length ≤ 10⁶)
width (1 ≤ width ≤ 10⁶)
Output

A single floating-point or integer value representing the area of the rectangle.
Example 1

Input:

length = 5
width = 10
Output:

50
Example 2

Input:

length = 7.5
width = 4
Output:

30.0"""

num1 = float(input("Enter the length of the rectangle: "))
num2 = float(input("Enter the width of the rectangle: "))

area = num1 * num2

if area % 1 == 0:
    print(f"The area of the rectangle is {int(area)}")
else:
    print(f"The area of the rectangle is {area:.2f}")