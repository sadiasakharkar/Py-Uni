'''
5. Program to Swap the Values of Two Variables (Any Data Type)
Problem Statement

Given two variables containing any data type (integer, float, string, list, tuple, etc.), write a program to swap their values.

Input

Two variables of any data type:
a
b
Output

The swapped values of a and b.
Example 1 (Integers)

Input:

a = 5  
b = 10  
Output:

After swapping:  
a = 10  
b = 5
Example 2 (Strings)

Input:

a = "Hello"  
b = "World"  
Output:

After swapping:  
a = "World"  
b = "Hello"
Example 3 (Lists)

Input:

a = [1, 2, 3]  
b = ["apple", "banana"]  
Output:

After swapping:  
a = ["apple", "banana"]  
b = [1, 2, 3]
Constraints

The values of a and b can be of any type (integer, float, string, list, tuple, dictionary, etc.).
The program should swap values without using a third variable.'''

a = input("Enter the first variable: ")
b = input("Enter the second variable: ")

print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")