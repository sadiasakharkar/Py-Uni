# 2. Program to Print the Multiplication Table of a Given Number

'''
Problem Statement

Given an integer n, write a program to print its multiplication table up to 10.

Input

A single integer:
n (-10⁶ ≤ n ≤ 10⁶)
Output

The multiplication table of n from 1 to 10.
Examples
Example 1

Input:

n = 5
Output:

5 × 1 = 5  
5 × 2 = 10  
5 × 3 = 15  
5 × 4 = 20  
5 × 5 = 25  
5 × 6 = 30  
5 × 7 = 35  
5 × 8 = 40  
5 × 9 = 45  
5 × 10 = 50  
Example 2

Input:

n = -3
Output:

-3 × 1 = -3  
-3 × 2 = -6  
-3 × 3 = -9  
-3 × 4 = -12  
-3 × 5 = -15  
-3 × 6 = -18  
-3 × 7 = -21  
-3 × 8 = -24  
-3 × 9 = -27  
-3 × 10 = -30  
Constraints
n can be positive, negative, or zero.
The table should be printed up to 10 terms.
Ensure proper formatting (n × i = result).
'''

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n , "x" , i , "=" , n*i)