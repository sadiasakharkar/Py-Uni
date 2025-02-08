# 4. Program to Calculate the Surface Area and Volume of a Cylinder

"""4. Program to Calculate the Surface Area and Volume of a Cylinder
Problem Statement

Given the radius and height of a cylinder, write a program to compute and return both its surface area and volume.

Input

Two positive floating-point or integer numbers:
radius (1 ≤ radius ≤ 10⁶)
height (1 ≤ height ≤ 10⁶)
Output

Two values:
Surface Area of the cylinder
Volume of the cylinder

Formulas
Surface Area = 2 * π * radius * (radius + height)
Volume = π * radius² * height

Example 1

Input:

radius = 5
height = 10
Output:

Surface Area: 471.24
Volume: 785.40
Example 2

Input:

radius = 3.5
height = 8
Output:

Surface Area: 259.19
Volume: 307.88
Constraints

The input values must be positive.
The results should be rounded to two decimal places when necessary.
"""

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

pie = 3.141592653589793

if radius < 0 or height < 0:
    print("Invalid input. Radius and height must be positive.")
else:
    surface = 2*pie*(radius * radius) + 2*pie*radius*height
    volume = pie*(radius*radius)*height
    
    print(f"Surface Area: {surface:.2f}")
    print(f"Volume: {volume:.2f}")