# 1. Program to Find the Factorial of a Given Number

'''Problem Statement

Given a non-negative integer n, write a program to compute and return its factorial.

Factorial Definition

Factorial of a number n (denoted as n!) is the product of all positive integers from 1 to n:

n!=n×(n−1)×(n−2)×...×2×1
By definition:

0!=1
Input

A single non-negative integer:
n (0 ≤ n ≤ 20)
Output

A single integer representing n! (factorial of n).
Examples
Example 1

Input:
n = 5
Calculation:
5! = 5 × 4 × 3 × 2 × 1 = 120
Output:
120

Example 2
Input:
n = 0
Output:
1

Example 3
Input:
n = 7
Calculation:
7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040
Output:
5040
'''

n = int(input("Enter a natural number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(n))