# 3. Program to Check Whether a Number is a Perfect Number

'''
Problem Statement

Given a positive integer n, write a program to determine whether it is a Perfect Number or not.

Definition of a Perfect Number

A Perfect Number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

Mathematical Representation:
A number n is perfect if:

σ
(
n
)
−
n
=
n
σ(n)−n=n
where 
σ
(
n
)
σ(n) is the sum of all divisors of n (including itself).

Input

A single positive integer:
n (1 ≤ n ≤ 10⁶)
Output

"Perfect Number" if n is a perfect number.
"Not a Perfect Number" otherwise.
Examples
Example 1

Input:

n = 6
Calculation:

Divisors of 6: 1, 2, 3  
Sum of divisors (excluding 6) = 1 + 2 + 3 = 6  
6 == 6 → Perfect Number
Output:

Perfect Number
Example 2

Input:

n = 28
Calculation:

Divisors of 28: 1, 2, 4, 7, 14  
Sum of divisors = 1 + 2 + 4 + 7 + 14 = 28  
28 == 28 → Perfect Number
Output:

Perfect Number
Example 3

Input:

n = 12
Calculation:

Divisors of 12: 1, 2, 3, 4, 6  
Sum of divisors = 1 + 2 + 3 + 4 + 6 = 16  
16 ≠ 12 → Not a Perfect Number
Output:

Not a Perfect Number
Constraints
n will be a positive integer.
The sum of divisors should be computed efficiently to handle large numbers up to 10⁶.
Use optimized algorithms (e.g., checking divisors up to sqrt(n)) to improve performance.

'''

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_divisors = 0
    
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
        