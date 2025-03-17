# This program calculates the area of a triangle using compound assignment operators.

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
constant = 5  # Adding a constant later

area = 0  # Initialize
area += 0.5 * base * height  # Calculate area using compound assignment
print(f"Area of the triangle: {area}")

# Adding a constant
area += constant
print(f"Area after adding {constant}: {area}")
