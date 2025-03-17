'''6. Program to Swap the Values of Two Variables Using a Third Variable
Problem Statement

Given two variables of any data type, write a program to swap their values using a third (temporary) variable.

Input

Two variables:
a
b
Output

The swapped values of a and b.
Examples
Example 1 (Swapping Integers)

Input:

a = 5  
b = 10  
Process:

Store a in a temporary variable: temp = a
Assign b to a: a = b
Assign temp to b: b = temp
Output:

After swapping:  
a = 10  
b = 5
Example 2 (Swapping Strings)

Input:

a = "Hello"  
b = "World"  
Output:

After swapping:  
a = "World"  
b = "Hello"
Python Code
# Taking input
a = input("Enter first value: ")
b = input("Enter second value: ")

# Swapping using a third variable
temp = a
a = b
b = temp

# Display the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
Why Use a Third Variable?
Useful in languages without tuple unpacking (e.g., C, Java).
Ensures values are not overwritten before swapping.
Works for all data types (integers, strings, lists, etc.).'''

a = input("Enter the first variable: ")
b = input("Enter the second variable: ")
print(f"Before swapping: a = {a}, b = {b}")

temp = a 
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")