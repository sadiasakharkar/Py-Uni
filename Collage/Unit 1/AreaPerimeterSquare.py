# 3.Area and Perimeter of a Square
"""3. Program to Calculate Area and Perimeter of a Square
Problem Statement

Given the side length of a square, write a program to compute and return both its area and perimeter.

Input

A single positive integer or floating-point number:
side (1 ≤ side ≤ 10⁶)
Output

Two values:
Area of the square
Perimeter of the square
Formulas

Area = side * side
 
Perimeter = 4 * side

Example 1

Input:

side = 4
Output:

Area: 16
Perimeter: 16
Example 2

Input:

side = 5.5
Output:

Area: 30.25
Perimeter: 22.0
Constraints

The input side is positive.
The result should be accurate up to two decimal places when necessary."""

side = float(input("Enter the side of the square: "))



if side < 0:
    print("Invalid input. Side length must be positive.")
else: 
    area = side * side
    perimeter = 4 * side
    
    print(f"Area: {area:.2f}" if area % 1 else f"Area: {int(area)}")
    print(f"Perimeter: {perimeter:.2f}" if perimeter % 1 else f"Perimeter: {int(perimeter)}")
    
